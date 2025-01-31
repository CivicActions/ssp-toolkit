import asyncio

from tools.watchers.component_watcher import watch_components
from tools.watchers.template_watcher import watch_templates


async def main():
    await asyncio.gather(
        watch_templates("./templates", loop=loop),
        watch_components("./results/components", loop=loop),
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
