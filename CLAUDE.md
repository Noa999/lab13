# CLAUDE.md

## Project
URL Shortener — Python FastAPI backend + React frontend

## Build Commands
```bash
# Backend
cd partB/src/backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd partB/src/frontend
npm install
npm run dev

# Tests
cd partB
pytest tests/ -v
```

## Conventions
- Python: snake_case, type hints always
- React: functional components, no class components
- API routes: /api/v1/...
- Commits: Conventional Commits (feat, fix, docs, test, refactor, chore)

## No-Go Zones
- No hardcoded secrets or API keys
- No print() for logging — use Python logging module
- No any type in TypeScript
- Do not delete migration files
