from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi_tailwind import tailwind
from contextlib import asynccontextmanager

from .ctx import ContextBuild
from .routers import routers
from .config import Config

__all__ = ("app",)

static_files = StaticFiles(directory = "static")

@asynccontextmanager
async def lifespan(_: FastAPI):
    process = tailwind.compile(
        static_files.directory + "/output.css",
        tailwind_stylesheet_path = "./static/input.css"
    )

    yield

    process.terminate()

app = FastAPI(
    docs_url = None,
    redoc_url = None,
    openapi_url = None,
    lifespan = lifespan
)

for router in routers:
    app.include_router(router)

templates = Jinja2Templates(directory = "./templates")
config = Config()

@app.get("/")
async def index(request: Request):
    context = ContextBuild(
        request = request,
        title = "Ananas - Home",
        description = "Homepage",
        image_url = "https://avatars.githubusercontent.com/u/132799819"
    )

    return templates.TemplateResponse(
        "home.html", {
            **context.data
        }
    )

@app.get("/projects")
async def index(request: Request):
    context = ContextBuild(
        request = request,
        title = "Ananas - Projects",
        description = "A list of my projects",
        image_url = "https://avatars.githubusercontent.com/u/132799819"
    )

    return templates.TemplateResponse(
        "projects.html", {
            **context.data,
            "projects": config.projects
        }
    )

@app.get("/blog")
async def index(request: Request):
    context = ContextBuild(
        request = request,
        title = "Ananas - Soon",
        description = "Coming Soon",
        image_url = "https://avatars.githubusercontent.com/u/132799819"
    )

    return templates.TemplateResponse(
        "blog.html", {
            **context.data,
        }
    )

@app.get("/blog/{id}")
async def index(request: Request, id: str):
    ...

app.mount("/", static_files)