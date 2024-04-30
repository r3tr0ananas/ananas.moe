from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import date

from .ctx import ContextBuild
from .routers import routers
from .config import Config

__all__ = ("app",)

app = FastAPI(
    docs_url = None,
    redoc_url = None,
    openapi_url = None
)

for router in routers:
    app.include_router(router)

templates = Jinja2Templates(directory = "./temp")
config = Config()

today = date.today()
year = today.year

@app.get("/")
async def index(request: Request, lang: str = "en"):
    language = await config.get_lang(lang)
    live_config = await config.get_config()

    languages = []

    context = ContextBuild(
        request = request,
        title = "Ananas - Home",
        description = "Homepage",
        image_url = "https://avatars.githubusercontent.com/u/132799819"
    )

    for config_language in live_config["languages"]:
        config_language["selected"] = config_language["language"] == lang
        
        languages.append(config_language)

    if language:
        language["copyright"] = language["copyright"].format(year)

        return templates.TemplateResponse(
            "home.html", {
                "lang": language,
                "languages": languages,

                **context.data
            }
        )
    
    return HTTPException(404)

app.mount("/", StaticFiles(directory = "static"))