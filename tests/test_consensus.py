from luminark_core.consensus import consensus_label, consensus_score


def test_consensus_weighted():
    score = consensus_score({"sigma": 8, "delta": 7, "omega": 6})
    assert score == 7.15
    assert consensus_label(score) == "CRITICAL"
