# STACK-COMPARISON.md

## Харьцуулсан 3 Stack

| | Stack A | Stack B | Stack C |
|---|---|---|---|
| Backend | Node.js + Express | Python + FastAPI | Go + Gin |
| Frontend | React | React | Vanilla JS |
| Database | SQLite | SQLite | SQLite |
| Test | Jest | Pytest | Go test |
| Type safety | TypeScript | Pydantic | Built-in |
| Хурд (dev) | Дунд | Дунд | Хурдан |
| Сурах хялбар | Хялбар | Хялбар | Хэцүү |
| Auto docs | Swagger plugin | Built-in Swagger | Manual |
| Хэрэглэгчийн туршлага | Сайн | Маш сайн | Дунд |

## Сонголт: Stack B — Python + FastAPI + React

### Шалтгаан

**FastAPI давуу тал:**
- OpenAPI / Swagger автоматаар үүсдэг — бие даалтын шаардлага биелнэ
- Pydantic-аар input validation хялбар
- Type hint-ийг шууд ашигладаг тул кодын чанар өндөр
- Async support built-in

**Pytest давуу тал:**
- Fixture system хүчтэй
- Тест бичих синтакс энгийн
- FastAPI-тай TestClient-ийн интеграц сайн

**Stack A-г орхисон шалтгаан:**
- FastAPI-д Swagger автомат байдаг — Express-т plugin хэрэгтэй болдог

**Stack C-г орхисон шалтгаан:**
- Go syntax танил биш, сурах хугацаа их шаардана
- 2 долоо хоногт хийж дуусгахад эрсдэлтэй
