from __future__ import annotations

from typing import Dict, List

SIGNATURES = {
    "GRID_CASCADE_PRECURSOR": {"severity": 7.5, "turbulence": 8.0, "adaptability": 2.0, "lead_time_h": 3.0},
    "LATENT_CONTROL_DRIFT": {"severity": 5.5, "turbulence": 6.0, "adaptability": 3.5, "lead_time_h": 18.0},
    "THERMAL_RUNAWAY_PATTERN": {"severity": 8.0, "turbulence": 7.0, "adaptability": 2.5, "lead_time_h": 2.0},
    "NETWORK_PARTITION_RISK": {"severity": 6.5, "turbulence": 7.5, "adaptability": 4.0, "lead_time_h": 6.0},
    "ORG_ESCALATION_SPIRAL": {"severity": 7.0, "turbulence": 6.5, "adaptability": 3.0, "lead_time_h": 12.0},
    "MODEL_ALIGNMENT_EROSION": {"severity": 8.5, "turbulence": 8.0, "adaptability": 1.5, "lead_time_h": 1.0},
}


def match_signatures(telemetry: Dict[str, float], tolerance: float = 1.5) -> List[Dict[str, float]]:
    matches = []
    for name, ref in SIGNATURES.items():
        distance = abs(telemetry["severity"] - ref["severity"]) + abs(telemetry["turbulence"] - ref["turbulence"]) + abs(telemetry["adaptability"] - ref["adaptability"])
        if distance <= tolerance * 3:
            matches.append({"name": name, "lead_time_h": ref["lead_time_h"], "distance": round(distance, 4)})
    return sorted(matches, key=lambda item: item["distance"])
