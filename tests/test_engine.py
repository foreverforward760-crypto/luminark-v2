from luminark_core import LuminarkEngine


def test_engine_output_shape():
    result = LuminarkEngine().analyze({"severity": 8, "turbulence": 8, "adaptability": 2})
    assert result["stage"]["index"] >= 1
    assert "trap_score" in result
    assert "consensus" in result
