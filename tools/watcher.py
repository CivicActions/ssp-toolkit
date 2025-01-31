import asyncio

from tools.watchers.templates import watch_templates


async def main():
    await asyncio.gather(
        watch_templates("./templates", loop=loop),
        # Add other async tasks here
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
