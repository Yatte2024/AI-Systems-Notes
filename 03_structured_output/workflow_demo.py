
from schemas import ValidationOutcome, VerificationResult, WorkflowDecision
from validator import validate_llm_output
from mock_llm_output import (
    FAILED_OUTPUT,
    LOW_CONFIDENCE_OUTPUT,
    VALID_OUTPUT,
)


def make_workflow_decision(
    outcome: ValidationOutcome,
) -> WorkflowDecision:
    """
    Convert a validation outcome into a workflow decision.

    This shows how structured outputs can support downstream routing.
    """

    if not outcome.is_valid:
        return WorkflowDecision(
            action="manual_review",
            reviewer_required=True,
            notes=f"Output validation failed: {outcome.error_type}",
        )

    result: VerificationResult = outcome.result

    if result.passed and result.confidence >= 0.90:
        return WorkflowDecision(
            action="approve",
            reviewer_required=False,
            notes="Verification passed with high confidence.",
        )

    if result.passed and result.confidence >= 0.70:
        return WorkflowDecision(
            action="manual_review",
            reviewer_required=True,
            notes="Verification passed, but confidence is not high enough for auto-approval.",
        )

    return WorkflowDecision(
        action="reject",
        reviewer_required=True,
        notes="Verification failed or confidence is too low.",
    )


def run_case(case_name: str, raw_output: str) -> None:
    print("\n" + "=" * 70)
    print(f"CASE: {case_name}")

    outcome = validate_llm_output(raw_output)
    decision = make_workflow_decision(outcome)

    print("\nValidation Outcome:")
    print(outcome.model_dump())

    print("\nWorkflow Decision:")
    print(decision.model_dump())


def main() -> None:
    run_case("Valid high-confidence output", VALID_OUTPUT)
    run_case("Valid low-confidence output", LOW_CONFIDENCE_OUTPUT)
    run_case("Valid failed verification output", FAILED_OUTPUT)


if __name__ == "__main__":
    main()