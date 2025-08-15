# ベンチ統合は後段。ここでは単純なローカルCSVを読むスタブ。
from dataclasses import dataclass
from spotlfc.core.schema import CheckRequest
from spotlfc.core.pipeline import run_check

@dataclass
class Item:
    text: str
    expected: str

SAMPLE = [
    Item("Ueno Zoo is located in Kyoto", "REFUTED"),
    Item("Ueno Zoo is located in Tokyo", "SUPPORTED"),
]

def run():
    ok = 0
    for it in SAMPLE:
        res = run_check(CheckRequest(post_text=it.text))
        pred = res.verdict["label"]
        ok += int(pred == it.expected)
        print(it.text, "→", pred, "(expected:", it.expected, ")")
    print(f"Acc: {ok}/{len(SAMPLE)} = {ok/len(SAMPLE):.2f}")

if __name__ == "__main__":
    run()
