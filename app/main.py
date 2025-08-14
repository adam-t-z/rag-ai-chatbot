from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from pydantic import BaseModel
import pathlib

from app.services.query_engine import QueryEngine
from app.config import STATIC_DIR


engine = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global engine
    print("[LIFESPAN] Starting app...")
    engine = QueryEngine()
    print("[LIFESPAN] Engine loaded.")
    yield
    print("[LIFESPAN] Shutting down app...")


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

BASE_DIR = pathlib.Path(__file__).parent


@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_path = STATIC_DIR / "index.html"
    return index_path.read_text(encoding="utf-8")


class QueryRequest(BaseModel):
    question: str


@app.post("/query")
def query(request: QueryRequest):
    result = engine.query(request.question)
    return result





