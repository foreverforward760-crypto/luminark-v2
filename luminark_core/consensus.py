from __future__ import annotations

from typing import Dict


WEIGHTS = {"sigma": 0.4, "delta": 0.35, "omega": 0.25}


def consensus_score(scores: Dict[str, float]) -> float:
    weighted = sum(scores[k] * WEIGHTS[k] for k in WEIGHTS)
    return round(weighted, 4)


def consensus_label(score: float) -> str:
    if score < 2.5:
        return "NOMINAL"
    if score < 4.0:
        return "WATCH"
    if score < 6.0:
        return "WARNING"
    if score < 8.5:
        return "CRITICAL"
    return "EMERGENCY"
