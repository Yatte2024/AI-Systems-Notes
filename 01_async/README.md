# Async Notes

## What problem does async solve?

Async helps applications avoid wasting time while waiting for external operations.

Examples:

- API calls
- web requests
- database queries
- file operations
- LLM responses

---

## Common misunderstanding

Async is not the same as parallel computing.

In many AI applications, async mainly improves IO-bound workflows.

The CPU is usually waiting for external services.

---

## Why async is important in AI systems

Modern AI applications often:

- call multiple APIs
- wait for model responses
- stream outputs
- manage long-running workflows
- support many users simultaneously

Without async, these systems can become very slow.

---

## Important keywords

- async def
- await
- asyncio.gather
- asyncio.create_task

---

## My current understanding

The important part is not memorizing APIs.

The important part is understanding:

- why async exists
- where waiting happens
- how workflows are managed
- how systems avoid blocking