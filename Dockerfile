FROM node:current-alpine AS tailwind

WORKDIR /app

COPY tailwind.config.js package.json Makefile ./
COPY /static/input.css ./static/input.css
COPY /templates ./templates

RUN apk add make

RUN npm install
RUN make tw

FROM python:3.11-slim-bookworm

USER root

WORKDIR /app

COPY /app ./app
COPY /static ./static
COPY /templates ./templates
COPY /config ./config

COPY --from=tailwind /app/static/output.css /app/static/output.css

COPY requirements.txt .
COPY package.json .
COPY tailwind.config.js .
COPY Makefile .

RUN apt-get update && apt-get install -y make

RUN make deps

EXPOSE 8000
ENV LISTEN_PORT = 8000

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--proxy-headers"]