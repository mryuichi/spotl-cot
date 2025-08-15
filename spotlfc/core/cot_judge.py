# PoCではLLM呼び出しを省略し、ローカル規則で verdict を返す。
# 後で OpenAI/Anthropic/Gemini を差し込める構造にしておく。

from typing import Literal
from .schema import SPOTL, EvidenceSPOTL

VerdictLabel = Literal["SUPPORTED","REFUTED","NEI"]

class JudgeResult:
    def __init__(self, label: VerdictLabel, reason: str):
        self.label = label
        self.reason = reason


def judge(claim: SPOTL, evs: list[EvidenceSPOTL], role_scores: dict[str,float]) -> JudgeResult:
    # 超単純: SとLが揃っていればSUPPORT、それ以外はNEI
    if role_scores.get("S",0) > 0 and role_scores.get("L",0) > 0:
        return JudgeResult("SUPPORTED", "SとLが一致（簡易ルール）")
    return JudgeResult("NEI", "決定的証拠なし（PoCルール）")
