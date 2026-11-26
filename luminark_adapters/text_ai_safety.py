"""Numeric score adapter only; this module does not analyze text or run AI.

The caller supplies MAAT, Guardian-risk, and policy-headroom numbers. The
adapter maps those numbers to the telemetry schema using fixed arithmetic.
It is not an AI safety detector, moderation model, or policy-compliance test.
"""
from __future__ import annotations

from .base import normalize_telemetry


def from_text_safety(maat_score: float, guardian_risk: float, policy_headroom: float):
    severity = 10 - maat_score
    turbulence = guardian_risk
    adaptability = policy_headroom
    return normalize_telemetry({"severity": severity, "turbulence": turbulence, "adaptability": adaptability})
