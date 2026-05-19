from schemas import ToolCall, ToolResult
from tool_registry import TOOLS


def execute_tool(tool_call: ToolCall) -> ToolResult:
    """
    Execute a tool selected by the LLM router.
    """

    tool_name = tool_call.tool

    if tool_name not in TOOLS:
        return ToolResult(
            tool=tool_name,
            success=False,
            output={},
            error="Tool not found.",
        )

    tool_function = TOOLS[tool_name]

    try:
        result = tool_function(
            **tool_call.arguments
        )

        return ToolResult(
            tool=tool_name,
            success=True,
            output=result,
        )

    except Exception as error:
        return ToolResult(
            tool=tool_name,
            success=False,
            output={},
            error=str(error),
        )