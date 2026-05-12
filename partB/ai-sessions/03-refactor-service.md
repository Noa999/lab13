# Session 03 — Service Layer Refactor

## Огноо: 2025-05-13

---

**Би:** router.py дотор business logic байж болох уу? service.py гэж тусад нь файл хийх хэрэгтэй юу?

**Claude:** Router дотор logic байвал тест бичихэд хэцүү болно. Service layer тусдаа байвал:
- Unit test хийхэд DB mock хийх шаардлагагүй болно
- Logic дахин ашиглагдана
- Router нь зөвхөн HTTP хариуцна

**Шийдвэр:** service.py тусдаа үүсгэсэн.

---

**Би:** delete_url функцэд soft delete хийх үү, hard delete хийх үү?

**Claude:** Энэ жижиг апп-д hard delete хангалттай. Soft delete нь `deleted_at` column нэмэх, query бүрд filter хийх — complexity нэмдэг. Analytics хэрэгтэй болвол soft delete-г хожим нэмж болно.

**Шийдвэр:** Hard delete хийсэн — энгийн, хурдан.

---

**Би:** generate_short_code функц дотор infinite loop боломжтой юу? Хэрхэн хязгаарлах вэ?

**Claude:** Онолын хувьд боломжтой, гэхдээ 68 тэрбум боломжит code-той бол практикт тохиолдохгүй. Гэсэн ч max_attempts нэмж болно:

```python
for _ in range(10):
    code = secrets.token_urlsafe(6)
    if not existing:
        return code
raise RuntimeError("could not generate unique code")
```

**Шийдвэр:** Энгийн while loop хэвээр хадгалсан — оюутны апп-д хангалттай.
