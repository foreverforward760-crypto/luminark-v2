# Architecture Guardrails

1. Core modules must remain deterministic and side-effect free.
2. Adapters may transform source signals, but must output canonical telemetry.
3. Interfaces must expose numeric telemetry controls; avoid quiz/slider-only UX.
4. Alert matrix is fixed: NOMINAL → WATCH → WARNING → CRITICAL → EMERGENCY.
5. Text/AI-safety support remains in adapter layer (Ma'at + Guardian mapped to telemetry).
6. Signature matching must support lead-time forecasting metadata.
7. Tests must protect all core modules and core formulas.

 
## Current repository boundary

The Next.js frontend is a separate five-slider self-reflection/journaling application. It calculates a stage by averaging user-entered values and does not call the Python telemetry API. The Python API uses three numeric telemetry inputs and nine operational labels. These two tracks are not integrated and must not be described as one deployed engine.

The Python text/AI-safety adapter only maps caller-supplied numeric scores. It does not inspect text, call an AI model, detect harmful content, or verify policy compliance.

The guardrails above apply to future operational telemetry interfaces; they do not describe capabilities already present in the current frontend.
