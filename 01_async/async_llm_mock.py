import asyncio
import random


async def mock_llm_call(agent_name: str):
    wait_time = random.randint(1, 4)

    print(f"[{agent_name}] Sending request to model...")

    await asyncio.sleep(wait_time)

    print(f"[{agent_name}] Response received after {wait_time}s")

    return {
        "agent": agent_name,
        "status": "completed",
        "wait_time": wait_time,
    }


async def main():
    tasks = [
        mock_llm_call("research-agent"),
        mock_llm_call("analysis-agent"),
        mock_llm_call("verification-agent"),
    ]

    results = await asyncio.gather(*tasks)

    print("\nFinal Results:")

    for result in results:
        print(result)


asyncio.run(main())