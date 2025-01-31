import asyncio
from pathlib import Path

from watchdog.events import (
    DirDeletedEvent,
    FileCreatedEvent,
    FileDeletedEvent,
    FileModifiedEvent,
    FileSystemEventHandler,
)
from watchdog.observers import Observer


class WatchTemplatesHandler(FileSystemEventHandler):
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.queue: asyncio.Queue = asyncio.Queue()
        self.loop = loop

    def on_modified(self, event: FileModifiedEvent) -> None:
        asyncio.run_coroutine_threadsafe(self.queue.put(event), self.loop)

    def on_created(self, event: FileCreatedEvent) -> None:
        asyncio.run_coroutine_threadsafe(self.queue.put(event), self.loop)

    def on_deleted(self, event: DirDeletedEvent | FileDeletedEvent) -> None:
        asyncio.run_coroutine_threadsafe(self.queue.put(event), self.loop)

    async def process_events(self):
        while True:
            event = await self.queue.get()
            if isinstance(event, (DirDeletedEvent, FileDeletedEvent)):
                await self.delete_file(file_path=event.src_path)
            elif isinstance(event, (FileCreatedEvent, FileModifiedEvent)):
                await self.create_files(file_path=event.src_path)

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
