
import json

from pydantic import ValidationError

from schemas import ValidationOutcome, VerificationResult


def validate_llm_output(raw_output: str) -> ValidationOutcome:
    """
    Parse and validate raw LLM output.

    This function simulates a common AI systems pattern:

    raw model output
        -> JSON parsing
        -> schema validation
        -> typed result or structured error
    """

    try:
        parsed_json = json.loads(raw_output)

    except json.JSONDecodeError as error:
        return ValidationOutcome(
            is_valid=False,
            error_type="json_parse_error",
            error_message=str(error),
        )

    try:
        result = VerificationResult.model_validate(parsed_json)

    except ValidationError as error:
        return ValidationOutcome(
            is_valid=False,
            error_type="schema_validation_error",
            error_message=str(error),
        )

    return ValidationOutcome(
        is_valid=True,
        result=result,
    )