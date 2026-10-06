"""Tests for the health check endpoint."""

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health_endpoint_returns_200() -> None:
    """Health endpoint should return HTTP 200."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200


def test_health_endpoint_returns_expected_payload() -> None:
    """Health endpoint should return the expected JSON structure."""
    response = client.get("/api/v1/health")
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "research-paper-rag"
    assert "version" in data


def test_root_endpoint_returns_welcome() -> None:
    """Root endpoint should return a welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["docs"] == "/docs"
