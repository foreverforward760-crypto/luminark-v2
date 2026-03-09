from luminark_core.nsdt import infer_stage


def test_infer_stage_thuban():
    stage = infer_stage({"severity": 8, "turbulence": 8, "adaptability": 2})
    assert stage.index == 8
