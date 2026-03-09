from __future__ import annotations


def escalation_level(consensus_label: str, trap_score: float) -> str:
    if consensus_label == "EMERGENCY" or trap_score >= 95:
        return "EMERGENCY"
    if consensus_label == "CRITICAL" or trap_score >= 45:
        return "CRITICAL"
    if consensus_label == "WARNING" or trap_score >= 25:
        return "WARNING"
    if consensus_label == "WATCH" or trap_score >= 10:
        return "WATCH"
    return "NOMINAL"


def yunus_protocol_required(level: str) -> bool:
    return level in {"CRITICAL", "EMERGENCY"}
