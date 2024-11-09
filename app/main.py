from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException

from fastapi_tailwind import tailwind
from contextlib import asynccontextmanager

from markdown import Markdown

from .ctx import ContextBuild
from .routers import blog, files, redirect
from .config import Config

import random

__all__ = ("app",)

static_files = StaticFiles(directory = "static")
markdown = Markdown()

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

for router in [blog, files, redirect]:
    app.include_router(router.router)

templates = Jinja2Templates(directory = "./templates")
config = Config()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    context = ContextBuild(
        request = request,
        title = "Ananas • Error",
        description = exc.detail,
    )

    return templates.TemplateResponse(
        name = "error.html",
        context = {
            **context.data,
            "status": exc.status_code,
            "message": exc.detail
        },
        status_code = exc.status_code
    )

@app.get("/")
async def index(request: Request):
    context = ContextBuild(
        request = request,
        title = "Ananas • Home",
        description = "My website :3",
        image_url = "https://ananas.moe/me.webp"
    )

    with open("./md/about_me.md") as file:
        about_me = markdown.convert(file.read())

    return templates.TemplateResponse(
        "home.html", {
            **context.data,
            "about_me": about_me,
            "latest": blog.blog.blogs[0] if blog.blog.blogs else None
        }
    )

@app.get("/projects")
async def projects(request: Request):
    context = ContextBuild(
        request = request,
        title = "Ananas • Projects",
        description = "A list of my projects :3",
        image_url = "https://ananas.moe/me.webp"
    )

    return templates.TemplateResponse(
        "projects.html", {
            **context.data,
            "projects": config.projects
        }
    )

@app.get("/clouds")
async def clouds(request: Request):
    context = ContextBuild(
        request = request,
        title = "Ananas • Clouds",
        description = "A collection of cloud images :3",
        image_url = random.choice(config.clouds)["image"] if config.clouds else "https://ananas.moe/me.webp"
    )

    return templates.TemplateResponse(
        "clouds.html", {
            **context.data,
            "clouds": config.clouds
        }
    )

app.mount("/", static_files)
