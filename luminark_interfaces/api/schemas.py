from __future__ import annotations

from pydantic import BaseModel, Field


class TelemetryInput(BaseModel):
    severity: float = Field(ge=0, le=10)
    turbulence: float = Field(ge=0, le=10)
    adaptability: float = Field(ge=0, le=10)


class TextSafetyInput(BaseModel):
    maat_score: float = Field(ge=0, le=10)
    guardian_risk: float = Field(ge=0, le=10)
    policy_headroom: float = Field(ge=0, le=10)
