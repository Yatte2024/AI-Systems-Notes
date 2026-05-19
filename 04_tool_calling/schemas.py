from typing import Dict, Optional

from pydantic import BaseModel


class ToolCall(BaseModel):
    tool: str
    arguments: Dict


class ToolResult(BaseModel):
    tool: str
    success: bool
    output: Dict
    error: Optional[str] = None
