import runpy
from pathlib import Path

import uvicorn


def test_running_app_py_starts_uvicorn(monkeypatch):
    app_path = Path(__file__).resolve().parents[1] / "src" / "app.py"
    called = {}

    def fake_run(app, host, port):
        called["app"] = app
        called["host"] = host
        called["port"] = port

    monkeypatch.setattr(uvicorn, "run", fake_run)

    runpy.run_path(str(app_path), run_name="__main__")

    assert called["app"].title == "Mergington High School API"
    assert called["host"] == "0.0.0.0"
    assert called["port"] == 8000
