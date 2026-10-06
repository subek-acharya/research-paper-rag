# Phase 0: Foundation

**Goal:** Set up a minimal, working FastAPI application with modern Python tooling (uv), version control (Git + GitHub), and a clean project structure that will scale through all subsequent phases.

**Status:** ✅ Complete

## What Was Built

1. Project scaffolding with `uv init`
2. Minimal FastAPI app with `/api/v1/health` and `/` endpoints
3. Pytest test suite (3 passing tests)
4. Git repository with proper `.gitignore`
5. GitHub remote repository
6. `.env.example` template for future environment variables
7. README with project vision and quickstart
8. Feature branch workflow established

## Dependencies Installed

**Production:**
- `fastapi` — Modern async web framework
- `uvicorn[standard]` — ASGI server
- `pydantic-settings` — Environment variable management

**Development:**
- `pytest` — Testing framework
- `ruff` — Fast Python linter + formatter
- `httpx` — HTTP client (used by TestClient)
- `pytest-asyncio` — Async test support

## How It Works

### Project Entry Point

`src/main.py` creates the FastAPI app and mounts routers. Each router lives in its own module under `src/routers/` for clean separation.

### Routing

`src/routers/health.py` defines a health check endpoint under the `/api/v1` prefix. All future API endpoints will follow this versioned prefix pattern.

### Testing

Tests use FastAPI's `TestClient` (built on `httpx`) to make in-process HTTP requests without starting a real server. This is fast and perfect for unit/integration tests.

## Running Locally

```bash
cd /Users/subekacharya/Developer/research-paper-rag

# Install deps (first time or after pulling changes)
uv sync

# Run the API
uv run uvicorn src.main:app --reload

# In another terminal
curl http://localhost:8000/api/v1/health
curl http://localhost:8000/
open http://localhost:8000/docs  # Interactive API docs (Swagger UI)
```

## Testing

```bash
uv run pytest -v
```

Expected: 3 tests passing.

## Key Decisions

| Decision | Rationale |
|---|---|
| uv over pip/poetry | 10-100x faster, modern standard, replaces venv+pip+poetry+pyenv |
| FastAPI over Flask/Django | Async-first, auto-generated OpenAPI docs, Pydantic validation |
| `/api/v1/` prefix | Future-proofing for API versioning |
| Routers in separate modules | Scalability — avoids a monolithic main.py |
| Pytest from day 1 | Catches regressions early as the system grows |
| Feature branch workflow | Industry standard; separates in-progress work from main |

## What's Next: Phase 1

- Add PostgreSQL as a Docker Compose service
- Define SQLAlchemy models for Paper
- Implement CRUD endpoints: POST /papers, GET /papers/{id}
- Add Alembic for database migrations
- Containerize the FastAPI app itself
