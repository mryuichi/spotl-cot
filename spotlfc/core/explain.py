from .schema import EvidenceSPOTL

def build(role_scores: dict[str,float], ev: EvidenceSPOTL | None) -> str:
    url = getattr(ev, "url", None) if ev else None
    return (
        f"S={role_scores.get('S',0):.2f}, P={role_scores.get('P',0):.2f}, "
        f"T={role_scores.get('T',0):.2f}, L={role_scores.get('L',0):.2f} | "
        f"evidence={url or 'N/A'}"
    )
