# AI Usage Report

## Төсөл: URL Shortener
## Огноо: 2025-05-09 — 2025-05-23

---

## 1. Юуг AI хийсэн, юуг өөрөө хийсэн?

### AI хийсэн зүйлс:

**partA:**
- ARCHITECTURE.md дахь Mermaid diagram-ын бүтэц — AI санал болгосон layer-уудыг би зөвшөөрсөн
- STACK-COMPARISON.md-ийн харьцуулалтын бүтэц — AI гаргасан, би агуулгыг нягталсан
- ADR-001-ийн template — AI өгсөн formatаар бичсэн

**partB:**
- models.py-ийн SQLAlchemy column-уудын тодорхойлолт
- schemas.py-ийн Pydantic model
- conftest.py-ийн test fixture бүтэц — AI санал болгосон, bi ойлгосны дараа ашигласан
- test_urls.py-ийн тестүүдийн ихэнх хэсэг

### Өөрөө хийсэн зүйлс:

- Stack сонголт — Python+FastAPI-г өөрийн шийдвэрээр сонгосон
- service.py-ийн `is_expired`, `delete_url` логик — өөрөө бичсэн
- Frontend-ийн ShortenForm, UrlList компонентуудын UI дизайн
- 301 vs 302 redirect-ийн шийдвэр — судлаад өөрөө шийдсэн
- Тестүүдийг review хийж, утгагүй тестүүдийг хасан зассан

---

## 2. Hallucination жишээ

### Жишээ 1: SQLAlchemy version conflict

AI нь `declarative_base()` ашиглахыг санал болгосон:
```python
from sqlalchemy.ext.declarative import declarative_base
```
Гэвч SQLAlchemy 2.0+ дээр энэ deprecated болсон байсан. Зөв import:
```python
from sqlalchemy.orm import declarative_base
```
Би `pip install sqlalchemy` хийгээд warning харж, docs шалгаж засав.

### Жишээ 2: Pydantic v1 syntax

AI `orm_mode = True` ашиглахыг санал болгосон:
```python
class Config:
    orm_mode = True
```
Гэвч Pydantic v2-д энэ `from_attributes = True` болж өөрчлөгдсөн. AI хуучин syntax санал болгосон байсан. Runtime error гарсны дараа Pydantic docs-оос шалгаж засав.

---

## 3. Security анхаарал

### CORS тохиргоо

AI эхлээд `allow_origins=["*"]` санал болгосон — энэ аюулгүй байдлын алдаа. Ямар ч domain-аас хүсэлт явуулах боломж нээгддэг. Би `/review` slash command ашиглаж шалгасны дараа зөвхөн `http://localhost:5173` зөвшөөрөхөөр засав:

```python
# AI санал болгосон (аюулгүй биш)
allow_origins=["*"]

# Засварласан
allow_origins=["http://localhost:5173"]
```

Production-д environment variable-ээр тохируулах хэрэгтэй гэдгийг тэмдэглэсэн.

---

## 4. AI-аар хурдан хийсэн зүйл

- **Boilerplate код** — FastAPI-ийн CORS middleware, database setup, dependency injection тохиргоог AI маш хурдан гаргаж өгсөн. Өөрөө бичвэл docs-оос хайж 30-40 минут зарцуулах байсан.
- **Test fixture** — conftest.py-ийн in-memory test database тохиргоог AI нэг удаагийн ярилцлагаар гаргасан.
- **Pydantic schema** — HttpUrl validation автоматаар URL format шалгадаг гэдгийг AI санал болгосон, өөрөө regex бичих шаардлагагүй болсон.

---

## 5. AI-аар удаан хийсэн зүйл

- **Expiration logic** — timezone асуудал гарахад AI хэд хэдэн өөр шийдэл санал болгосон, бүгдийг туршиж шалгахад цаг зарцуулагдсан. Эцэст нь хамгийн энгийн шийдлийг сонгосон.
- **301 vs 302 redirect** — AI эхлээд 301 санал болгосон, дараа нь click count-ын асуудлыг тайлбарлахад 302 руу өөрчилсөн. Нэмэлт ярилцлага шаардсан.
- **Test тохиргоо** — conftest.py дахь `app.dependency_overrides` тохиргоо зөв ажиллахын тулд хэд хэдэн удаа засах шаардлагатай болсон.

---

## 6. Skill atrophy эрсдэл

AI-аар хэт их зүйл хийлгэхэд өөрийн мэдлэг суларч болзошгүй гэдгийг анзаарсан. Дараах аргаар зохицуулсан:

- AI код бичсэний дараа заавал өөрөө уншиж ойлгосны дараа ашигласан
- service.py-ийн функцуудыг эхлээд өөрөө бичээд, дараа нь AI-тай харьцуулсан
- `datetime.utcnow()` vs `datetime.now(timezone.utc)` гэх мэт жижиг зүйлсийг AI-гүйгээр docs-оос шалгасан
- Шалгалтад AI байхгүй гэдгийг санаж, кодын бүх хэсгийг тайлбарлаж чадах эсэхийг өөрөө туршсан
