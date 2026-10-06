"""Health check endpoint for monitoring and liveness probes."""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1", tags=["health"])


class HealthResponse(BaseModel):
    """Response schema for the health check endpoint."""

    status: str
    service: str
    version: str


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Return the current health status of the API service.

    :returns: HealthResponse with status, service name, and version.
    """
    from src import __version__

    return HealthResponse(
        status="ok",
        service="research-paper-rag",
        version=__version__,
    )
