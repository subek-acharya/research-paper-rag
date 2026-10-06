"""FastAPI application entry point for Research Paper RAG."""

from fastapi import FastAPI

from src import __version__
from src.routers import health

app = FastAPI(
    title="Research Paper RAG",
    description="Agentic RAG system for research paper discovery and Q&A.",
    version=__version__,
)

app.include_router(health.router)


@app.get("/")
async def root() -> dict:
    """Return a welcome message at the root path.

    :returns: Dict containing a welcome message and documentation URL.
    """
    return {
        "message": "Welcome to Research Paper RAG",
        "docs": "/docs",
        "health": "/api/v1/health",
    }
