# URL Shortener

URL богиносгох веб апп — Python FastAPI + React

## Технологи
- Backend: Python 3.11+, FastAPI, SQLAlchemy, SQLite
- Frontend: React, Vite
- Test: Pytest

## Суулгах

```bash
# Backend
cd partB/src/backend
pip install -r requirements.txt
uvicorn main:app --reload
# http://localhost:8000

# Frontend
cd partB/src/frontend
npm install
npm run dev
# http://localhost:5173
```

## Тест ажиллуулах

```bash
cd partB
pytest tests/ -v
```

## API Docs
Backend ажиллаж байхад http://localhost:8000/docs хаягаар Swagger UI нээгдэнэ.

## Feature-ууд
- URL богиносгох
- Redirect хийх
- Click тоолох
- URL expiration
- Жагсаалт харах
