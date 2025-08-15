from .schema import SPOTL, EvidenceSPOTL

def score(claim: SPOTL, evs: list[EvidenceSPOTL]) -> tuple[dict[str,float], EvidenceSPOTL | None]:
    # 最小: SとLが両方非空ならそれぞれ0.5ずつ加点
    s = 1.0 if (claim.S and evs and evs[0].S) else 0.0
    l = 1.0 if (claim.L and evs and evs[0].L) else 0.0
    role_scores = {"S": s, "P": 0.5 if claim.P else 0.0, "O": 0.0, "T": 0.0, "L": l}
    return role_scores, (evs[0] if evs else None)
