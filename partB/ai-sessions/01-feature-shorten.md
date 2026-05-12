# Session 01 — URL Богиносгох Feature

## Огноо: 2025-05-10

---

**Би:** FastAPI-д URL богиносгох endpoint хэрхэн хийх вэ? Short code үүсгэх хамгийн сайн арга юу вэ?

**Claude:** `secrets.token_urlsafe(6)` ашиглахыг санал болгож байна. `random.randint` эсвэл `uuid`-аас илүү аюулгүй, URL-д тохиромжтой тэмдэгтүүд ашигладаг. 6 тэмдэгт = 64^6 ≈ 68 тэрбум боломжит хослол.

Давхцлыг шалгах loop:
```python
while True:
    code = secrets.token_urlsafe(6)
    if not db.query(Url).filter(Url.short_code == code).first():
        return code
```

**Би:** Энэ loop хэзээ ч дуусахгүй байж болох уу?

**Claude:** Онолын хувьд тийм, гэхдээ 68 тэрбум боломжит code-той бол практикт тохиолдохгүй. Аюулгүй болгохыг хүсвэл max retry тоо нэм.

**Шийдвэр:** Энгийн loop хэрэглэсэн — аппын scale-д хангалттай.

---

**Би:** Redirect хийхдээ 301 уу 302 уу ашиглах вэ?

**Claude:** 302 (Found) ашиглах нь зөв. 301 бол browser cache хийдэг тул click count буруу тоологдоно. URL shortener-т 302 стандарт.

**Шийдвэр:** 302 ашигласан.
