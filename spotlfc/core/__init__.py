from . import schema  # noqa: F401
from . import pipeline  # type: ignore  # added at runtime via this file

# 動的importを避けたい場合は pipeline.py を通常のモジュールとして置いてください。
