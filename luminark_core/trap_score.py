from __future__ import annotations


def compute_trap_score(severity: float, turbulence: float, adaptability: float, stage_multiplier: float) -> float:
    score = severity * turbulence * (1 - adaptability / 10) * stage_multiplier
    return round(max(score, 0.0), 4)
