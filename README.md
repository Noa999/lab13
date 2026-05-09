# Бие даалт 13 — URL Shortener

AI-assisted software construction — Python FastAPI + React

## Бүтэц
- `partA/` — Төлөвлөлт (architecture, stack, ADR)
- `partB/` — Хэрэгжилт (backend, frontend, tests)
- `partC/` — Эргэцүүлэл (AI usage report, ADR-002, self-evaluation)
- `CLAUDE.md` — Build commands, conventions
- `.claude/commands/` — Custom slash commands

## Хурдан эхлэх

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
