import asyncio
from collections import deque


# ---------------------------------------------------
# Basic Queue Example
# ---------------------------------------------------

# %%

def basic_queue_example():
    print("=" * 50)
    print("Basic Queue Example")

    task_queue = deque()

    task_queue.append("research task")
    task_queue.append("summarize task")
    task_queue.append("generate report")

    while task_queue:
        task = task_queue.popleft()
        print(f"Processing: {task}")


# ---------------------------------------------------
# Async Queue Example
# ---------------------------------------------------

async def producer(queue: asyncio.Queue):
    for i in range(5):
        task = f"task-{i}"

        await queue.put(task)

        print(f"[Producer] Added {task}")

        await asyncio.sleep(1)


async def consumer(queue: asyncio.Queue):
    while True:
        task = await queue.get()

        print(f"[Consumer] Processing {task}")

        await asyncio.sleep(2)

        print(f"[Consumer] Finished {task}")

        queue.task_done()


async def async_queue_example():
    print("=" * 50)
    print("Async Queue Example")

    queue = asyncio.Queue()

    consumer_task = asyncio.create_task(consumer(queue))

    await producer(queue)

    await queue.join()

    consumer_task.cancel()


# ---------------------------------------------------
# Streaming Example
# ---------------------------------------------------

async def stream_response():
    print("=" * 50)
    print("Streaming Example")

    response = (
        "Streaming makes AI systems feel more responsive "
        "during long-running workflows."
    )

    for word in response.split():
        print(word, end=" ", flush=True)

        await asyncio.sleep(0.3)

    print()


# ---------------------------------------------------
# Progress Heartbeat Example
# ---------------------------------------------------

async def long_running_task():
    for step in [
        "Planning research steps...",
        "Searching sources...",
        "Generating report...",
        "Evaluating results..."
    ]:
        print(f"[Heartbeat] {step}")

        await asyncio.sleep(2)

    print("[Heartbeat] Workflow completed")


# ---------------------------------------------------
# Main
# ---------------------------------------------------

async def main():

    # streaming
    basic_queue_example()

    await async_queue_example()

    await stream_response()

    await long_running_task()

    # no streaming
    stream_task = asyncio.create_task(stream_response())
    await long_running_task()
    await stream_task

if __name__ == "__main__":
    asyncio.run(main())
# %%
