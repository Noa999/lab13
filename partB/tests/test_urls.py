def test_shorten_valid_url(client):
    res = client.post("/api/v1/shorten", json={"original_url": "https://example.com"})
    assert res.status_code == 200
    data = res.json()
    assert "short_code" in data
    assert data["click_count"] == 0
    assert data["original_url"] == "https://example.com"

def test_shorten_invalid_url(client):
    res = client.post("/api/v1/shorten", json={"original_url": "not-a-url"})
    assert res.status_code == 422

def test_shorten_empty_url(client):
    res = client.post("/api/v1/shorten", json={"original_url": ""})
    assert res.status_code == 422

def test_redirect_increments_click(client):
    res = client.post("/api/v1/shorten", json={"original_url": "https://example.com"})
    code = res.json()["short_code"]

    client.get(f"/{code}", follow_redirects=False)
    client.get(f"/{code}", follow_redirects=False)

    info = client.get(f"/api/v1/urls/{code}")
    assert info.json()["click_count"] == 2

def test_redirect_unknown_code(client):
    res = client.get("/unknown123", follow_redirects=False)
    assert res.status_code == 404

def test_list_urls_empty(client):
    res = client.get("/api/v1/urls")
    assert res.status_code == 200
    assert res.json() == []

def test_list_urls_returns_all(client):
    client.post("/api/v1/shorten", json={"original_url": "https://a.com"})
    client.post("/api/v1/shorten", json={"original_url": "https://b.com"})
    res = client.get("/api/v1/urls")
    assert len(res.json()) == 2

def test_get_url_by_code(client):
    res = client.post("/api/v1/shorten", json={"original_url": "https://example.com"})
    code = res.json()["short_code"]
    res2 = client.get(f"/api/v1/urls/{code}")
    assert res2.status_code == 200
    assert res2.json()["short_code"] == code

def test_get_url_not_found(client):
    res = client.get("/api/v1/urls/doesnotexist")
    assert res.status_code == 404

def test_delete_url(client):
    res = client.post("/api/v1/shorten", json={"original_url": "https://example.com"})
    code = res.json()["short_code"]
    del_res = client.delete(f"/api/v1/urls/{code}")
    assert del_res.status_code == 200
    assert client.get(f"/api/v1/urls/{code}").status_code == 404

def test_delete_nonexistent_url(client):
    res = client.delete("/api/v1/urls/fakecode")
    assert res.status_code == 404

def test_expired_url_returns_410(client):
    from datetime import datetime, timedelta
    past = (datetime.utcnow() - timedelta(hours=1)).isoformat()
    res = client.post("/api/v1/shorten", json={
        "original_url": "https://example.com",
        "expires_at": past
    })
    code = res.json()["short_code"]
    res2 = client.get(f"/{code}", follow_redirects=False)
    assert res2.status_code == 410
