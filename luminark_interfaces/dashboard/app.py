from __future__ import annotations

import streamlit as st

from luminark_core import LuminarkEngine

st.set_page_config(page_title="Luminark Monitoring Panel", layout="wide")
st.title("Luminark Monitoring Panel")

severity = st.number_input("Severity (0-10)", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
turbulence = st.number_input("Turbulence (0-10)", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
adaptability = st.number_input("Adaptability (0-10)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

if st.button("Run Analysis"):
    engine = LuminarkEngine()
    result = engine.analyze({"severity": severity, "turbulence": turbulence, "adaptability": adaptability})
    st.subheader("Stage")
    st.json(result["stage"])
    st.subheader("Consensus")
    st.json(result["consensus"])
    st.metric("TrapScore", result["trap_score"])
    st.metric("Alert Level", result["alert_level"])
    st.metric("Yunus Protocol", "ON" if result["yunus_protocol"] else "OFF")
    st.subheader("Signature Matches")
    st.json(result["signature_matches"])
