from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routers import routers

__all__ = ("app",)

app = FastAPI(
    docs_url = None,
    redoc_url = None,
    openapi_url = None
)

for router in routers:
    app.include_router(router)

templates = Jinja2Templates(directory = "./temp")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        "home.html", {
            "request": request,
        }
    )

@app.get("/ip")
async def ip(request: Request):
    return PlainTextResponse(request.client.host)

app.mount("/", StaticFiles(directory = "static"))