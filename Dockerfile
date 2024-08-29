FROM python:3.11-alpine

USER root

WORKDIR /app

COPY /app ./app
COPY /static ./static
COPY /templates ./templates
COPY /config ./config

COPY requirements.txt .
COPY tailwind.config.js .

RUN pip install -r requirements.txt

EXPOSE 8000
ENV LISTEN_PORT = 8000

CMD ["fastapi", "run"]
