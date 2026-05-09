# AI Planning Session — partA

## Огноо: 2025-05-09

## Stack харьцуулалт

**Би:** URL shortener хийхэд ямар stack тохиромжтой вэ? Node+Express, Python+FastAPI, Go+Gin-г харьцуул.

**Claude:** Гурван сонголтыг харьцуулъя...
- Node+Express: JavaScript ecosystem, npm library олон, гэхдээ OpenAPI manual
- Python+FastAPI: Swagger автомат, Pydantic validation, pytest хялбар
- Go+Gin: хамгийн хурдан, гэхдээ syntax хэцүү, сурах хугацаа их

FastAPI-г зөвлөж байна — OpenAPI auto-generation нь бие даалтын шаардлагыг шууд биелүүлнэ.

**Шийдвэр:** Python + FastAPI + React

---

## Architecture

**Би:** Энэ апп-д ямар layer-үүд хэрэгтэй вэ?

**Claude:** 4 layer санал болгож байна:
1. Frontend — React + Vite
2. API layer — FastAPI router
3. Service layer — business logic (short code үүсгэх, redirect)
4. Data layer — SQLAlchemy + SQLite

**Би:** Short code хэрхэн үүсгэх вэ?

**Claude:** `secrets.token_urlsafe(6)` — 6 тэмдэгтийн URL-safe random string. Давхцлыг шалгаад дахин үүсгэх loop хийх.

---

## Folder бүтэц

**Би:** Folder бүтцийг яаж зохион байгуулах вэ?

**Claude:**
```
partB/src/
├── backend/
│   ├── main.py
│   ├── router.py
│   ├── models.py
│   ├── schemas.py
│   ├── service.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   ├── components/
    └── package.json
```

**Шийдвэр:** Санал болгосон бүтцийг хүлээн авсан.
