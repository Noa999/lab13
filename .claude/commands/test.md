# /test

Generate pytest tests for the selected code.

Cover:
- Happy path
- Edge cases (empty input, None, zero, negative)
- Error cases (invalid URL, duplicate short code, expired URL)
- Boundary conditions

Use FastAPI TestClient for API tests. Include fixtures where needed.
