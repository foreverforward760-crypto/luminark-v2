from __future__ import annotations

from typing import Iterable


def recurrence_index(events: Iterable[float]) -> float:
    arr = [x for x in events if x > 0]
    if not arr:
        return 0.0
    return round(min(len(arr) / 10, 1.0), 4)
