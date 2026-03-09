from __future__ import annotations

from fastapi import FastAPI

from luminark_adapters import from_text_safety
from luminark_core import LuminarkEngine
from luminark_core.nsdt import STAGES
from luminark_core.signatures import SIGNATURES

from .schemas import TelemetryInput, TextSafetyInput

app = FastAPI(title="Luminark Interfaces API", version="1.0.0")
engine = LuminarkEngine()


@app.post("/api/v1/analyze")
def analyze(payload: TelemetryInput):
    return engine.analyze(payload.model_dump())


@app.post("/api/v1/analyze/text")
def analyze_text(payload: TextSafetyInput):
    telemetry = from_text_safety(payload.maat_score, payload.guardian_risk, payload.policy_headroom)
    return engine.analyze(telemetry)


@app.get("/api/v1/stages")
def stages():
    return [{"index": s.index, "name": s.name, "multiplier": s.multiplier, "centroid": s.centroid} for s in STAGES]


@app.get("/api/v1/signatures")
def signatures():
    return SIGNATURES
