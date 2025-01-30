import asyncio
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class WatchTemplatesHandler(FileSystemEventHandler):
    def __init__(self):
        self.queue = asyncio.Queue()

    def on_modified(self, event):
        asyncio.run_coroutine_threadsafe(self.queue.put(event), loop)

    async def process_events(self):
        while True:
            event = await self.queue.get()
            await self.create_files(file_path=event.src_path)

    @staticmethod
    async def create_files(file_path: str):
        if not Path(file_path).is_dir():
            filepath = file_path.rstrip("~")
            print(f"File modified: {file_path}")
            proc = await asyncio.create_subprocess_shell(
                f"python tools/createfiles/createfiles.py -t {filepath} -o results",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            stdout, stderr = await proc.communicate()
            if stdout:
                print(f"Script output:\n{stdout.decode()}")
            if stderr:
                print(f"Script error:\n{stderr.decode()}")


async def watch_directory(path):
    handler = WatchTemplatesHandler()
    observer = Observer()
    observer.schedule(handler, path, recursive=True)
    observer.start()

    try:
        await handler.process_events()
    finally:
        observer.stop()
        observer.join()


async def main():
    await asyncio.gather(
        watch_directory("./templates"),
        # Add other async tasks here
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
