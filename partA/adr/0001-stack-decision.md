# ADR-001: Stack сонголт

## Статус
Баталсан

## Огноо
2025-05-09

## Контекст
URL Shortener апп хийхэд backend, frontend, database технологи сонгох шаардлага гарлаа. Гурван сонголтыг харьцуулан шалгасан.

## Шийдвэр
Python + FastAPI + React + SQLite stack-ийг сонгосон.

## Үндэслэл
- FastAPI нь OpenAPI spec автоматаар үүсгэдэг — бие даалтын шаардлагыг биелүүлнэ
- Pydantic validation built-in тул аюулгүй байдал сайн
- Pytest + FastAPI TestClient-ийн хослол тест бичихэд хялбар
- SQLite — жижиг апп-д хангалттай, тохиргоо шаардахгүй

## Үр дагавар
- Go-ийн performance давуу талыг алдана — гэхдээ энэ хэмжээний апп-д хамаагүй
- Node ecosystem-ийн npm library олон байдлыг ашиглахгүй
- Python мэдлэг шаардагдана
