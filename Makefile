.PHONY: venv install dev run test lint fmt up down

PY?=python3
VENV=.venv
ACTIVATE=$(VENV)/bin/activate

venv:
	$(PY) -m venv $(VENV)

install: venv
	. $(ACTIVATE) && pip install -U pip
	. $(ACTIVATE) && pip install -r requirements.txt

dev: install
	. $(ACTIVATE) && pip install -r requirements-dev.txt

run:
	. $(ACTIVATE) && uvicorn spotlfc.api.main:app --reload --port 8000

lint:
	. $(ACTIVATE) && ruff check spotlfc
	. $(ACTIVATE) && black --check spotlfc

fmt:
	. $(ACTIVATE) && black spotlfc

test:
	. $(ACTIVATE) && pytest -q

up:
	docker compose up --build -d

down:
	docker compose down
