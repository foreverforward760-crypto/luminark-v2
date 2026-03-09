from __future__ import annotations

from typing import Dict

from .alerts import escalation_level, yunus_protocol_required
from .consensus import consensus_label, consensus_score
from .nsdt import infer_stage
from .signatures import match_signatures
from .trap_score import compute_trap_score


class LuminarkEngine:
    def analyze(self, telemetry: Dict[str, float]) -> Dict[str, object]:
        stage = infer_stage(telemetry)
        trap = compute_trap_score(
            telemetry["severity"], telemetry["turbulence"], telemetry["adaptability"], stage.multiplier
        )
        evaluator_scores = {
            "sigma": telemetry["severity"],
            "delta": telemetry["turbulence"],
            "omega": 10 - telemetry["adaptability"],
        }
        consensus = consensus_score(evaluator_scores)
        c_label = consensus_label(consensus)
        level = escalation_level(c_label, trap)
        signatures = match_signatures(telemetry)
        return {
            "stage": {"index": stage.index, "name": stage.name},
            "trap_score": trap,
            "consensus": {"score": consensus, "label": c_label, "evaluators": evaluator_scores},
            "alert_level": level,
            "yunus_protocol": yunus_protocol_required(level),
            "signature_matches": signatures,
        }
