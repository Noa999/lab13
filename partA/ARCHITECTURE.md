# ARCHITECTURE.md

## System Architecture

```mermaid
graph TB
    User["Browser (React)"]
    API["FastAPI Backend"]
    DB["SQLite Database"]

    User -->|"POST /api/v1/shorten"| API
    User -->|"GET /api/v1/urls"| API
    User -->|"GET /{short_code}"| API
    API -->|"redirect 302"| User
    API -->|"read/write"| DB
```

## Module Description

```mermaid
graph LR
    subgraph Frontend
        App["App.jsx"]
        ShortenForm["ShortenForm.jsx"]
        UrlList["UrlList.jsx"]
    end

    subgraph Backend
        Main["main.py"]
        Router["router.py"]
        Models["models.py"]
        Schemas["schemas.py"]
        Service["service.py"]
    end

    App --> ShortenForm
    App --> UrlList
    ShortenForm -->|"API call"| Router
    UrlList -->|"API call"| Router
    Router --> Service
    Service --> Models
```

## Layers

| Layer | Technology | Role |
|---|---|---|
| Frontend | React + Vite | UI, form, URL жагсаалт |
| API | FastAPI | HTTP handler, validation |
| Service | Python class | Business logic |
| Data | SQLAlchemy + SQLite | Persistence |

## Data Flow

1. Хэрэглэгч URL оруулна → ShortenForm POST хийнэ
2. FastAPI Pydantic-аар validate хийнэ
3. Service layer random short code үүсгэнэ
4. SQLite-д хадгална, response буцаана
5. Богино URL дээр дарахад → redirect 302
6. Click count нэмэгдэнэ
