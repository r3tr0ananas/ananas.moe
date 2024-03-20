build: deps npm tw

deps:
	pip install -r requirements.txt

npm:
	npm i

tw:
	npx tailwindcss -i ./static/input.css -o ./static/output.css

tw-watch:
	npx tailwindcss -i ./static/input.css -o ./static/output.css --watch

d-build:
	python scripts/docker_build.py

d-compose:
	docker compose up

run:
	uvicorn app.main:app --reload --port 8083

test:
	ruff check .

venv:
	pip3 install virtualenv
	virtualenv .venv

