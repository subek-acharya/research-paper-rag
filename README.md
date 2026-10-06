# Research Paper RAG

An agentic Retrieval-Augmented Generation (RAG) system for discovering and querying research papers. Built incrementally from scratch to learn production-grade RAG system design end to end.

**Status:** Phase 0 — Foundation ✅

## Project Vision

A production-grade RAG system that automatically ingests research papers (initially from arXiv, extensible to other sources), parses them, indexes them with hybrid search (BM25 + vector embeddings), and answers natural-language questions through an agentic LangGraph workflow.

## Tech Stack (Target Architecture)

| Layer | Technology |
|---|---|
| API | FastAPI, Pydantic |
| Database | PostgreSQL, SQLAlchemy |
| Search | OpenSearch (BM25 + vector) |
| Embeddings | Jina AI (or sentence-transformers) |
| LLM | Ollama (local), with llama3.2 |
| Orchestration | Apache Airflow |
| Agent Framework | LangGraph |
| Cache | Redis |
| Observability | Langfuse |
| Containerization | Docker + Docker Compose |
| Package Manager | uv |

## Build Phases

- [x] **Phase 0:** Foundation — FastAPI skeleton, uv, Git, GitHub
- [ ] **Phase 1:** FastAPI + PostgreSQL in Docker Compose
- [ ] **Phase 2:** arXiv API client + ingestion script
- [ ] **Phase 3:** PDF parsing with Docling
- [ ] **Phase 4:** Airflow orchestration for daily ingestion
- [ ] **Phase 5:** OpenSearch + BM25 keyword search
- [ ] **Phase 6:** Hybrid search (BM25 + vector embeddings)
- [ ] **Phase 7:** LLM generation with Ollama (complete RAG)
- [ ] **Phase 8:** Redis caching + Langfuse observability
- [ ] **Phase 9:** Agentic reasoning with LangGraph
- [ ] **Phase 10:** Custom features and extensions

## Prerequisites

- macOS, Linux, or WSL2
- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- Docker Desktop (used from Phase 1 onwards)
- Git + GitHub CLI

## Quick Start (Phase 0)

```bash
# Clone the repository
git clone https://github.com/subek-acharya/research-paper-rag.git
cd research-paper-rag

# Install dependencies (uv auto-creates .venv/)
uv sync

# Run the API
uv run uvicorn src.main:app --reload

# Verify
curl http://localhost:8000/api/v1/health
# Expected: {"status":"ok","service":"research-paper-rag","version":"0.1.0"}

# Run tests
uv run pytest
```

## Project Structure

```
research-paper-rag/
├── src/                    # Application source code
│   ├── __init__.py
│   ├── main.py             # FastAPI entry point
│   └── routers/            # API route handlers
│       ├── __init__.py
│       └── health.py       # /api/v1/health endpoint
├── tests/                  # Pytest test suite
│   ├── __init__.py
│   └── test_health.py
├── docs/                   # Phase-by-phase documentation
│   └── phase-0-foundation.md
├── notebooks/              # Jupyter notebooks for exploration
├── .env.example            # Environment variable template
├── .gitignore
├── .python-version         # Python version pin (uv)
├── pyproject.toml          # Project config + dependencies
├── uv.lock                 # Locked dependency versions
└── README.md
```

## Development Workflow

This project follows a feature branch workflow:

- `main` branch holds the latest stable, working code.
- Each phase is developed on a `feature/phase-N-description` branch.
- Feature branches merge back to `main` after acceptance tests pass.

```bash
# Start a new phase
git checkout main
git pull
git checkout -b feature/phase-N-description

# Work, commit, push
git add .
git commit -m "feat(phaseN): description"
git push -u origin feature/phase-N-description

# Open PR via gh CLI
gh pr create --fill
```

## Author

Subek Acharya
MS Computer Science, University of Rhode Island
RSAIL Lab — Research in Adversarial Machine Learning & AI Security

## License

MIT (see LICENSE file — to be added)

## Acknowledgements

This project was inspired by the open-source agentic-rag-course by Jam With AI. The implementation here is rebuilt from scratch for deep learning, with custom extensions for adversarial ML and AI security research.
