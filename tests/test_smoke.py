from spotlfc.core.schema import CheckRequest
from spotlfc.core.pipeline import run_check


def test_smoke_support():
    r = run_check(CheckRequest(post_text="Ueno Zoo is located in Tokyo"))
    assert r.verdict["label"] in {"SUPPORTED","NEI","REFUTED"}
