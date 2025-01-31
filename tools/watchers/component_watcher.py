import asyncio

from watchdog.events import FileCreatedEvent, FileModifiedEvent, FileSystemEventHandler
from watchdog.observers import Observer


class WatchComponentsHandler(FileSystemEventHandler):
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.processed_files: set[str] = set()
        self.queue: asyncio.Queue = asyncio.Queue()
        self.loop = loop

    def on_modified(self, event: FileModifiedEvent) -> None:
        asyncio.run_coroutine_threadsafe(self.queue.put(event), self.loop)

    def on_created(self, event: FileCreatedEvent) -> None:
        asyncio.run_coroutine_threadsafe(self.queue.put(event), self.loop)

    async def process_events(self):
        while True:
            event = await self.queue.get()
            if isinstance(event, (FileModifiedEvent, FileCreatedEvent)):
                file_path = event.src_path
                if file_path not in self.processed_files:
                    self.processed_files.add(file_path)
                    await self.make_families()

                    await asyncio.sleep(1)
                    self.processed_files.remove(file_path)

    @staticmethod
    async def make_families():
        process = await asyncio.create_subprocess_shell(
            "python tools/makefamilies/makefamilies.py",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        if stdout:
            print(f"MakeFamilies:\n{stdout.decode()}")
        if stderr:
            print(f"makefamilies.py error:\n{stderr.decode()}")


async def watch_components(path: str, loop: asyncio.AbstractEventLoop):
    handler = WatchComponentsHandler(loop=loop)
    observer = Observer()
    observer.schedule(handler, path, recursive=True)
    observer.start()

    try:
        await handler.process_events()
    finally:
        observer.stop()
        observer.join()
