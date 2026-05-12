# Session 02 — Expiration Bug Debug

## Огноо: 2025-05-12

---

**Би:** expires_at талбарыг шалгахад UTC timezone харьцуулалт буруу болж байна. datetime.utcnow() vs datetime.now() ялгаа юу вэ?

**Claude:** Энэ түгээмэл алдаа. `datetime.now()` нь локал цагийг буцаана, `datetime.utcnow()` нь UTC буцаана. SQLite timezone мэдэхгүй тул хадгалагдсан утга timezone-гүй байна. Хоёуланг нь тогтвортой нэг маягаар ашиглах хэрэгтэй.

Шийдэл: `datetime.utcnow()` хаа сайгүй ашиглах, эсвэл `datetime.now(timezone.utc)` руу шилжих.

**Би:** `datetime.utcnow()` deprecated гэж уншсан.

**Claude:** Зөв, Python 3.12-оос deprecated. `datetime.now(timezone.utc)` ашиглах нь зөв. Гэхдээ SQLite-д хадгалахдаа timezone-aware datetime-ийг serialize хийхдээ анхаарах хэрэгтэй.

**Шийдвэр:** `datetime.utcnow()` хэрэглэсэн хэвээр — SQLite-тэй нийцтэй, аппын хэмжээнд хангалттай. Production-д шилжихэд засах.

---

**Би:** Expired URL-д 404 уу 410 уу буцаах вэ?

**Claude:** 410 Gone илүү зөв. 404 = "байхгүй", 410 = "байсан, одоо байхгүй". URL shortener-т expired URL-д 410 HTTP стандарт.

**Шийдвэр:** 410 ашигласан.
