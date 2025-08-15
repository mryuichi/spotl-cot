import re
from .schema import SPOTL, RoleItem

# 超簡易: "X is located in Y" のみ検出（PoCの最小）
_LOC_RE = re.compile(r"^(?P<S>.+?)\s+is\s+located\s+in\s+(?P<L>.+?)\.?$", re.I)

def extract(text: str, lang: str = "en") -> SPOTL:
    m = _LOC_RE.match(text.strip())
    if not m:
        return SPOTL()
    s = m.group("S").strip()
    l = m.group("L").strip()
    return SPOTL(
        S=[RoleItem(name=s)],
        P=[RoleItem(rel="located_in")],
        O=[],
        T=[],
        L=[RoleItem(name=l)],
    )
