
from schemas import ToolCall


def route_query(user_query: str) -> ToolCall:
    """
    Simulate how an LLM might decide which tool to call.
    """

    query = user_query.lower()

    if "calculate" in query:
        # This is a fixed demo argument, not a real natural-language parser.
        return ToolCall(
            tool="calculator",
            arguments={
                "expression": "25 * 4"
            },
        )

    if "verify" in query:
        return ToolCall(
            tool="verify_claim",
            arguments={
                "claim": user_query
            },
        )

    return ToolCall(
        tool="search_web",
        arguments={
            "query": user_query
        },
    )
