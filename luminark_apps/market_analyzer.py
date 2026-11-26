"""Organizational-score wrapper retained under a historical name.

This function calls the organizational adapter with caller-supplied numbers.
It does not retrieve market prices, market feeds, trading data, or financial
news and should not be represented as a market forecasting service.
"""
from __future__ import annotations

from luminark_adapters import from_org
from luminark_core import LuminarkEngine


def run_market_analyzer(conflict: float, volatility: float, resilience: float):
    engine = LuminarkEngine()
    telemetry = from_org(conflict, volatility, resilience)
    return engine.analyze(telemetry)
