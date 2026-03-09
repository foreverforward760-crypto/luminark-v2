from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Dict, Iterable, Tuple

TelemetryVector = Tuple[float, float, float]


@dataclass(frozen=True)
class Stage:
    index: int
    name: str
    centroid: TelemetryVector
    multiplier: float


STAGES = (
    Stage(1, "NOMINAL", (1.0, 1.0, 1.0), 0.8),
    Stage(2, "STABLE", (2.0, 2.0, 1.5), 0.9),
    Stage(3, "WATCH", (3.0, 3.0, 2.5), 1.0),
    Stage(4, "ANOMALOUS", (4.0, 4.0, 3.5), 1.1),
    Stage(5, "DEGRADED", (5.0, 5.0, 4.5), 1.2),
    Stage(6, "FRACTURE", (6.0, 6.0, 5.5), 1.35),
    Stage(7, "PRECASCADE", (7.0, 7.0, 6.5), 1.5),
    Stage(8, "THUBAN", (8.0, 8.0, 2.0), 1.75),
    Stage(9, "TERMINAL", (9.0, 9.0, 8.5), 2.0),
)


def infer_stage(telemetry: Dict[str, float]) -> Stage:
    point = (telemetry["severity"], telemetry["turbulence"], telemetry["adaptability"])

    def dist(a: Iterable[float], b: Iterable[float]) -> float:
        return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

    return min(STAGES, key=lambda stage: dist(point, stage.centroid))
