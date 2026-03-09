from __future__ import annotations

from statistics import mean
from typing import Iterable


def trend_slope(samples: Iterable[float]) -> float:
    arr = list(samples)
    if len(arr) < 2:
        return 0.0
    baseline = mean(arr[:-1])
    return round(arr[-1] - baseline, 4)
