# Codex Prompt Template (生成AI向け)

You are a senior Python engineer. Write production-ready code with tests.
We implement SPOTL-based fact checking with LLM-CoT judging.

## Task
- Expand the current stub into robust modules:
  - text_spotl.extract(): use UD/SRL (stanza or spacy) to extract S/P/O/T/L
  - retriever: add BM25 (e.g., elastic / simple in-memory) and embedding retrieval
  - align_score: implement role-wise scoring with synonym tables and temporal/geospatial logic
  - cot_judge: perform JSON-only CoT with temperature=0.1, top_p=0.1; accept claim/evidence SPOTL and return {verdict, role_scores, rationale}

## Constraints
- Follow Pydantic models in spotlfc.core.schema
- Keep functions pure; separate I/O
- Provide unit tests for each module
- Strict JSON output for cot_judge (add schema validation)

## Deliverables
- Updated modules + tests
- Minimal examples and docstrings
