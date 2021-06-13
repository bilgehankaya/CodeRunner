from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Literal
from .repository.repository import get_output
from .schemas.schemas import Request, languages

tags_metadata = [
    {
        "name": "compiler",
        "description": "Run **python** or **java** code!",
    }
]

app = FastAPI(
    title="Online Code Runner",
    description="You can run python and java code!\n",
    version="0.1",
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"message": "success"}


@app.post("/compiler/{language}", tags=["compiler"])
async def generic_compiler(language: Literal[languages], request: Request):
    return get_output(language, request)
