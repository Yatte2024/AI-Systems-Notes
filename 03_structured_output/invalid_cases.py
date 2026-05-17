from validator import validate_llm_output
from workflow_demo import make_workflow_decision
from mock_llm_output import (
    INVALID_JSON_OUTPUT,
    MISSING_FIELD_OUTPUT,
    NEGATIVE_CONFIDENCE_OUTPUT,
    WRONG_TYPE_OUTPUT,
)


def run_invalid_case(case_name: str, raw_output: str) -> None:
    print("\n" + "=" * 70)
    print(f"INVALID CASE: {case_name}")

    outcome = validate_llm_output(raw_output)
    decision = make_workflow_decision(outcome)

    print("\nValidation Outcome:")
    print(outcome.model_dump())

    print("\nWorkflow Decision:")
    print(decision.model_dump())


def main() -> None:
    run_invalid_case("Invalid JSON", INVALID_JSON_OUTPUT)
    run_invalid_case("Missing required field", MISSING_FIELD_OUTPUT)
    run_invalid_case("Wrong field types", WRONG_TYPE_OUTPUT)
    run_invalid_case("Invalid confidence range", NEGATIVE_CONFIDENCE_OUTPUT)


if __name__ == "__main__":
    main()