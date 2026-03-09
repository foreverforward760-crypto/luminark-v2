from luminark_core.alerts import escalation_level, yunus_protocol_required


def test_alert_matrix():
    assert escalation_level("CRITICAL", 50) == "CRITICAL"
    assert yunus_protocol_required("CRITICAL") is True
