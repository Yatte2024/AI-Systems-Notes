from mock_llm_router import route_query
from tool_executor import execute_tool


SEARCH_EXAMPLE = "Search for recent AI systems articles"
CALCULATOR_EXAMPLE = "Calculate 25 multiplied by 4"
VERIFY_EXAMPLE = "Verify this claim about AI workflows"


def run_workflow(user_query: str):
    print("\n" + "=" * 70)

    print("\nUSER QUERY")
    print(user_query)

    print("\nROUTING STEP")
    print("The mock LLM router decides which tool should handle this query.")

    tool_call = route_query(user_query)

    print("\nTOOL SELECTED")
    print(tool_call.model_dump())

    tool_result = execute_tool(tool_call)

    print("\nTOOL RESULT")
    print(tool_result.model_dump())

    print("\nWORKFLOW COMPLETE")


def main():
    # The mock router uses keywords in the user query to choose a tool.
    # No keyword match falls back to the search_web tool.
    run_workflow(SEARCH_EXAMPLE)

    # Queries containing "calculate" are routed to the calculator tool.
    run_workflow(CALCULATOR_EXAMPLE)

    # Queries containing "verify" are routed to the verify_claim tool.
    run_workflow(VERIFY_EXAMPLE)


if __name__ == "__main__":
    main()
