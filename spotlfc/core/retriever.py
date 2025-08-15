# まずは固定文献を返すスタブ。後でBM25/Embedに差し替え。
from .schema import EvidenceSPOTL, RoleItem

def retrieve_evidence_spotl(claim_spotl) -> list[EvidenceSPOTL]:
    # デモ用: いつでも「Ueno Zoo is in Tokyo」の証拠を返す
    ev = EvidenceSPOTL(
        source="stub",
        url="https://en.wikipedia.org/wiki/Ueno_Zoo",
        lines="1-1",
        S=[RoleItem(name="Ueno Zoo")],
        P=[RoleItem(rel="located_in")],
        L=[RoleItem(name="Tokyo")],
    )
    return [ev]
