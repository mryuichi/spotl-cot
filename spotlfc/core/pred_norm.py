# 述語の同義正規化テーブル（最小）
P_SYNONYM = {
    "opened": "inception",
    "founded": "inception",
    "located in": "located_in",
    "is located in": "located_in",
}

def normalize(rel: str) -> str:
    return P_SYNONYM.get(rel.lower(), rel.lower())
