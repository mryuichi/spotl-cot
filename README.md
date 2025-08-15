# SPOTL + COT Rapid Prototype

## Quickstart

```bash
make dev
cp .env.example .env
make run
# 別ターミナルで:
curl -s -X POST 'http://127.0.0.1:8000/check' \
  -H 'Content-Type: application/json' \
  -d '{"post_text":"Ueno Zoo is located in Kyoto","lang":"en"}' | jq .
