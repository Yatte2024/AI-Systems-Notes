import asyncio
import time


async def call_service(task: str) -> str:
    print(f"Start: {task}")
    await asyncio.sleep(2)
    return f"Finished: {task}"


async def main():
    start = time.time()

    results = await asyncio.gather(
        call_service("research"),
        call_service("summarise"),
        call_service("verify"),
    )

    print(results)
    print(f"Elapsed time: {time.time() - start:.2f} seconds")


asyncio.run(main())