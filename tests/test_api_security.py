from fastapi import HTTPException
from starlette.requests import Request

import luminark_interfaces.api.main as api


def make_request(host: str) -> Request:
    return Request({
        "type": "http",
        "http_version": "1.1",
        "method": "POST",
        "scheme": "http",
        "path": "/api/v1/analyze",
        "raw_path": b"/api/v1/analyze",
        "query_string": b"",
        "headers": [],
        "client": (host, 1234),
        "server": ("localhost", 8000),
    })


def test_analysis_api_fails_closed_without_key(monkeypatch):
    monkeypatch.setattr(api, "API_KEY", None)
    monkeypatch.setattr(api, "ALLOW_INSECURE_LOCAL", False)
    try:
        api.require_api_key(make_request("127.0.0.1"), None)
    except HTTPException as exc:
        assert exc.status_code == 503
    else:
        raise AssertionError("API should fail closed without configured authentication")


def test_analysis_api_checks_configured_key(monkeypatch):
    monkeypatch.setattr(api, "API_KEY", "test-secret")
    monkeypatch.setattr(api, "ALLOW_INSECURE_LOCAL", False)
    try:
        api.require_api_key(make_request("203.0.113.5"), "wrong")
    except HTTPException as exc:
        assert exc.status_code == 401
    else:
        raise AssertionError("Wrong API key should be rejected")
    assert api.require_api_key(make_request("203.0.113.5"), "test-secret") is None


def test_loopback_mode_is_explicit_and_limited(monkeypatch):
    monkeypatch.setattr(api, "API_KEY", None)
    monkeypatch.setattr(api, "ALLOW_INSECURE_LOCAL", True)
    assert api.require_api_key(make_request("127.0.0.1"), None) is None
    try:
        api.require_api_key(make_request("203.0.113.5"), None)
    except HTTPException as exc:
        assert exc.status_code == 503
    else:
        raise AssertionError("Non-loopback request must not pass without API key")


def test_text_safety_adapter_only_maps_numeric_scores():
    from luminark_adapters.text_ai_safety import from_text_safety

    result = from_text_safety(8.0, 2.0, 7.0)
    assert result == {"severity": 2.0, "turbulence": 2.0, "adaptability": 7.0}
