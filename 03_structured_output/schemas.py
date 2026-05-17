
from typing import List, Optional

from pydantic import BaseModel, Field


class Citation(BaseModel):
    source_id: int
    url: str


class VerificationResult(BaseModel):
    passed: bool
    confidence: float = Field(ge=0.0, le=1.0)
    explanation: str
    citations: List[Citation]


class ValidationOutcome(BaseModel):
    is_valid: bool
    result: Optional[VerificationResult] = None
    error_type: Optional[str] = None
    error_message: Optional[str] = None


class WorkflowDecision(BaseModel):
    action: str
    reviewer_required: bool
    notes: Optional[str] = None