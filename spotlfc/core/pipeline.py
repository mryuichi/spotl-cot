from .schema import CheckRequest, CheckResponse
from . import text_spotl, image_spotl
from .retriever import retrieve_evidence_spotl
from .evidence_norm import normalize_evidence
from .align_score import score
from .cot_judge import judge
from .explain import build as build_explain

SUPPORT_THRESHOLD = 0.65


def run_check(req: CheckRequest) -> CheckResponse:
    claim_spotl = text_spotl.extract(req.post_text, req.lang)
    img_spotl = image_spotl.extract(req.images)

    # SPOTLマージ（最小：非空を優先）
    # 将来は厳密な統合手順に置換
    if img_spotl.S: claim_spotl.S += img_spotl.S
    if img_spotl.P: claim_spotl.P += img_spotl.P
    if img_spotl.O: claim_spotl.O += img_spotl.O
    if img_spotl.T: claim_spotl.T += img_spotl.T
    if img_spotl.L: claim_spotl.L += img_spotl.L

    evs = retrieve_evidence_spotl(claim_spotl)
    evs = normalize_evidence(evs)

    role_scores, top_ev = score(claim_spotl, evs)
    jr = judge(claim_spotl, evs, role_scores)

    resp = CheckResponse(
        verdict={"label": jr.label, "score": max(role_scores.values() or [0.0])},
        evidence=[top_ev] if top_ev else [],
        role_scores=role_scores,
        explanation=build_explain(role_scores, top_ev),
    )
    return resp
