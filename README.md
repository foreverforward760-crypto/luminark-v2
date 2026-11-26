# LUMINARK v2 — Mixed Self-Reflection UI and Telemetry Prototype

## Conceptual provenance

The project owner states that the underlying LUMINARK / 0-9-0 concepts and product ideas originated with him. AI systems generated the implementation code and suggested technical mechanisms. NSDT and the Container Rule are AI-added supporting mechanisms within the owner's framework, not independent conceptual foundations. This records the owner's account and is not a legal determination of rights or inventorship.

## Important repository distinction

This repository currently contains two separate implementations that are not integrated with one another:

1. **Next.js self-reflection application** — a five-slider personal reflection UI with stage descriptions and journaling. Its current stage calculation is a simple rounded average of five user-entered values. Journal entries are saved in browser localStorage.
2. **Python telemetry API and core** — a separate three-input rule/centroid classifier for severity, turbulence, and adaptability. It has nine operational labels (NOMINAL through TERMINAL), a fixed trap-score formula, weighted consensus arithmetic, static signature matching, and alert thresholds. It does not currently implement the same 0–9 frontend stage calculation or an explicit Stage 0 / return-to-zero cycle.

Do not describe the frontend as using the Python telemetry engine. No integration between the two is implemented in the current code.

## Frontend: self-reflection application

### Current behavior

- Five user-controlled inputs: complexity, stability, tension, adaptability, and coherence.
- Current stage is calculated as the rounded average of those five values mapped to 0–9.
- Stage descriptions and guidance are static content in data/systemData.ts.
- Journal entries, reflections, selected domains, and vector scores are saved in localStorage.
- The app does not call the Python telemetry API.

The slider scores and stage output are project-defined reflection prompts, not validated psychological or physiological measurements. The app is not a diagnostic or treatment tool. localStorage is not encrypted by this application; do not use it for highly sensitive journal content on a shared device.

## Python telemetry engine: actual behavior

The Python core accepts three numeric inputs on a 0–10 scale:

- severity
- turbulence
- adaptability

It selects the nearest of nine manually defined centroids using Euclidean distance. It then computes:

- a trap score using severity × turbulence × (1 − adaptability/10) × stage multiplier;
- a weighted score from severity, turbulence, and inverse adaptability;
- an alert label using fixed thresholds;
- a boolean protocol flag derived from that alert label;
- matches against static signature rules.

These are deterministic formulas and manually selected thresholds. The scores are not calibrated probabilities, validated risk estimates, or proven predictions. The API receives caller-supplied numbers; no live grid, HVAC, market, vehicle, organizational, or AI-system data connection is established.

### Adapter limitations

- Grid and HVAC adapters rename and normalize caller-supplied numbers; they do not connect to sensors or control systems.
- The market analyzer wrapper currently calls an organizational adapter; it does not retrieve market data.
- The text/AI-safety adapter maps three caller-supplied numeric scores. It does not inspect text, run an AI model, detect harmful content, or verify policy compliance.
- Consensus is a fixed weighted arithmetic combination of three values, not independent multi-agent consensus.
- Signature matching uses static rules, not a trained anomaly detector.

## API security

The analysis endpoints now require LUMINARK_V2_API_KEY. For local development only, LUMINARK_V2_ALLOW_INSECURE_LOCAL=true permits requests from loopback addresses. Do not enable that mode on a network-facing host.

Example local run:

```bash
pip install -r requirements.txt
LUMINARK_V2_ALLOW_INSECURE_LOCAL=true uvicorn luminark_interfaces.api.main:app --host 127.0.0.1 --port 8000
```

Network deployment requires a strong LUMINARK_V2_API_KEY, HTTPS termination, rate limiting, monitoring, and a separate security review.

## Tests and evidence

Python unit tests exercise formulas, thresholds, adapters, and output structure. The Next.js build workflow checks compilation. Passing these tests demonstrates software behavior for selected inputs only; it does not validate the underlying framework, stage labels, risk thresholds, or real-world outcomes.

## Commercial assessment

The frontend is a functioning self-reflection/journaling prototype. The Python package is a separate rule-based telemetry prototype. Neither is a validated operational decision product. Before commercial development, choose which product direction to pursue, reconcile the two models, establish the intended stage mapping, and test against independently sourced domain data.