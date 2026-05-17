
VALID_OUTPUT = """
{
  "passed": true,
  "confidence": 0.94,
  "explanation": "All citations match the referenced sources.",
  "citations": [
    {
      "source_id": 1,
      "url": "https://example.com/source-1"
    },
    {
      "source_id": 2,
      "url": "https://example.com/source-2"
    }
  ]
}
"""


LOW_CONFIDENCE_OUTPUT = """
{
  "passed": true,
  "confidence": 0.72,
  "explanation": "The citation appears related, but the evidence is not very strong.",
  "citations": [
    {
      "source_id": 1,
      "url": "https://example.com/source-1"
    }
  ]
}
"""


FAILED_OUTPUT = """
{
  "passed": false,
  "confidence": 0.35,
  "explanation": "The citation does not support the claim.",
  "citations": [
    {
      "source_id": 1,
      "url": "https://example.com/source-1"
    }
  ]
}
"""


MISSING_FIELD_OUTPUT = """
{
  "passed": true,
  "confidence": 0.91,
  "citations": [
    {
      "source_id": 1,
      "url": "https://example.com/source-1"
    }
  ]
}
"""


WRONG_TYPE_OUTPUT = """
{
  "passed": "yes",
  "confidence": "high",
  "explanation": "Looks correct.",
  "citations": []
}
"""


INVALID_JSON_OUTPUT = """
{
  "passed": true,
  "confidence": 0.88,
  "explanation": "Malformed JSON example"
  "citations": []
}
"""


NEGATIVE_CONFIDENCE_OUTPUT = """
{
  "passed": true,
  "confidence": -0.5,
  "explanation": "Invalid confidence score.",
  "citations": []
}
"""