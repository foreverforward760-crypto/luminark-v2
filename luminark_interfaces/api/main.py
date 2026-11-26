"""FastAPI interface for the experimental LUMINARK telemetry prototype.

The API accepts caller-supplied numeric telemetry. It has no live data
connectors, persistent database, or independently validated risk model.
Analysis endpoints require API-key or explicit loopback-only development mode.
"""
from __future__ import annotations

import os
import secrets
from typing import Optional
from fastapi import FastAPI, Depends, Header, HTTPException, Request

from luminark_adapters import from_text_safety
from luminark_core import LuminarkEngine
from luminark_core.nsdt import STAGES
from luminark_core.signatures import SIGNATURES

from .schemas import TelemetryInput, TextSafetyInput

app = FastAPI(title="Luminark Interfaces API — Prototype", description="Rule-based telemetry scoring prototype; no live data or validated operational predictions.", version="1.0.0")
API_KEY = os.getenv("LUMINARK_V2_API_KEY")
ALLOW_INSECURE_LOCAL = os.getenv("LUMINARK_V2_ALLOW_INSECURE_LOCAL", "").lower() == "true"


def require_api_key(request: Request, x_api_key: Optional[str] = Header(default=None)):
    if API_KEY:
        if not x_api_key or not secrets.compare_digest(x_api_key, API_KEY):
            raise HTTPException(status_code=401, detail="Invalid or missing API key")
        return
    host = request.client.host if request.client else ""
    if ALLOW_INSECURE_LOCAL and host in {"127.0.0.1", "::1", "localhost", "testclient"}:
        return
    raise HTTPException(status_code=503, detail="API authentication is not configured. Set LUMINARK_V2_API_KEY; local development may explicitly enable LUMINARK_V2_ALLOW_INSECURE_LOCAL.")
engine = LuminarkEngine()


@app.post("/api/v1/analyze", dependencies=[Depends(require_api_key)])
def analyze(payload: TelemetryInput):
    result = engine.analyze(payload.model_dump())
    result["analysis_notice"] = "Prototype only. This is a fixed rule/centroid calculation on caller-supplied numeric inputs, not a calibrated risk probability or validated operational alert."
    return result


@app.post("/api/v1/analyze/text", dependencies=[Depends(require_api_key)], description="Maps caller-supplied numeric scores; this endpoint does not read text or perform AI safety detection.")
def analyze_text(payload: TextSafetyInput):
    telemetry = from_text_safety(payload.maat_score, payload.guardian_risk, payload.policy_headroom)
    result = engine.analyze(telemetry)
    result["analysis_notice"] = "Prototype only. This endpoint maps numeric scores supplied by the caller; it does not inspect text, detect harmful content, or validate AI safety."
    return result


@app.get("/health")
def health():
    return {"status": "ok", "mode": "prototype", "operational_validation": False}


@app.get("/api/v1/stages")
def stages():
    return [{"index": s.index, "name": s.name, "multiplier": s.multiplier, "centroid": s.centroid} for s in STAGES]


@app.get("/api/v1/signatures")
def signatures():
    return SIGNATURES
