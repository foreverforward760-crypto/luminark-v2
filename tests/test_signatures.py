from luminark_core.signatures import match_signatures


def test_signature_match():
    out = match_signatures({"severity": 7.6, "turbulence": 8.1, "adaptability": 2.2})
    assert out
    assert out[0]["name"] == "GRID_CASCADE_PRECURSOR"
