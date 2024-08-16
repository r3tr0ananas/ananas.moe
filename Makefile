build: deps

deps:
	pip install -r requirements.txt

docker:
	python scripts/docker_build.py

run:
	uvicorn app.main:app --reload --port 8083

test:
	ruff check .
