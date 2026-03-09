from luminark_core.trap_score import compute_trap_score


def test_trap_score_formula():
    assert compute_trap_score(8, 8, 2, 1.75) == 89.6
