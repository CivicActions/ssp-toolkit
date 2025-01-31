import asyncio
from pathlib import Path

from watchdog.events import FileClosedEvent, FileSystemEventHandler
from watchdog.observers import Observer


class WatchTemplatesHandler(FileSystemEventHandler):
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.debounce_task = None
        self.file_path: str = ""
        self.queue: asyncio.Queue = asyncio.Queue()
        self.loop = loop

    def on_modified(self, event: FileClosedEvent) -> None:
        asyncio.run_coroutine_threadsafe(self.queue.put(event), self.loop)

    async def process_events(self):
        while True:
            event = await self.queue.get()
            if isinstance(event, FileClosedEvent):
                self.file_path = event.src_path
                if self.debounce_task and not self.debounce_task.done():
                    self.debounce_task.cancel()

                self.debounce_task = asyncio.create_task(self._debounce())

    async def _debounce(self):
        await asyncio.sleep(0.5)
        await self.create_files(file_path=self.file_path)

    @staticmethod
    async def create_files(file_path: str):
        if not Path(file_path).is_dir():
            filepath = file_path.rstrip("~")
            process = await asyncio.create_subprocess_shell(
                f"python tools/createfiles/createfiles.py -t {filepath} -o results",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await process.communicate()
            if stdout:
                print(f"Script output:\n{stdout.decode()}")
            if stderr:
                print(f"Script error:\n{stderr.decode()}")

    @staticmethod
    async def delete_file(file_path: str):
        deleted_file = Path(file_path.rstrip("~"))
        to_delete = Path("results").joinpath(*deleted_file.parts[1:])
        to_delete_path = to_delete.parent
        to_delete = (
            to_delete_path.joinpath(to_delete.stem)
            if to_delete.suffix == ".j2"
            else to_delete
        )
        if to_delete.is_file():
            to_delete.unlink()


async def watch_templates(path: str, loop: asyncio.AbstractEventLoop):
    handler = WatchTemplatesHandler(loop=loop)
    observer = Observer()
    observer.schedule(handler, path, recursive=True)
    observer.start()

    try:
        await handler.process_events()
    finally:
        observer.stop()
        observer.join()
