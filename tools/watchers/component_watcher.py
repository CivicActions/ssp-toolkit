import asyncio

from watchdog.events import FileClosedEvent, FileSystemEventHandler
from watchdog.observers import Observer


class WatchComponentsHandler(FileSystemEventHandler):
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.debounce_task = None
        self.queue: asyncio.Queue = asyncio.Queue()
        self.loop = loop

    def on_modified(self, event: FileClosedEvent) -> None:
        asyncio.run_coroutine_threadsafe(self.queue.put(event), self.loop)

    async def process_events(self):
        while True:
            event = await self.queue.get()
            if isinstance(event, FileClosedEvent):
                if self.debounce_task and not self.debounce_task.done():
                    self.debounce_task.cancel()

                self.debounce_task = asyncio.create_task(self._debounce())

    async def _debounce(self):
        await asyncio.sleep(0.5)
        success = await self.make_families()
        await asyncio.sleep(0.5)
        if success:
            await self.make_sop()

    @staticmethod
    async def make_families() -> bool:
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

        return True if process.returncode == 0 else False

    @staticmethod
    async def make_sop() -> None:
        process = await asyncio.create_subprocess_shell(
            "python tools/sop/sop.py",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        if stdout:
            print(f"SOP:\n{stdout.decode()}")
        if stderr:
            print(f"sop.py error:\n{stderr.decode()}")


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
