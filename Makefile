build: deps npm ts tw

deps:
	pip install -r requirements.txt

npm:
	npm i

ts:
	npx tsc ./static/scripts/*.ts --target ES2016

tw:
	npx tailwindcss -i ./static/input.css -o ./static/output.css

tw-watch:
	npx tailwindcss -i ./static/input.css -o ./static/output.css --watch

docker:
	python scripts/docker_build.py

run:
	uvicorn app.main:app --reload --port 8083

test:
	ruff check .
