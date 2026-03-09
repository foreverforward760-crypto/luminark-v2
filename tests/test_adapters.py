from luminark_adapters import from_text_safety


def test_text_adapter_mapping():
    t = from_text_safety(maat_score=2, guardian_risk=9, policy_headroom=2)
    assert t["severity"] == 8
    assert t["turbulence"] == 9
    assert t["adaptability"] == 2
