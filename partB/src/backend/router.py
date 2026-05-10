from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import get_db
from schemas import UrlCreate, UrlResponse
import service
from typing import List

router = APIRouter()

@router.post("/api/v1/shorten", response_model=UrlResponse)
def shorten_url(data: UrlCreate, db: Session = Depends(get_db)):
    return service.create_short_url(db, data)

@router.get("/api/v1/urls", response_model=List[UrlResponse])
def list_urls(db: Session = Depends(get_db)):
    return service.get_all_urls(db)

@router.get("/api/v1/urls/{short_code}", response_model=UrlResponse)
def get_url(short_code: str, db: Session = Depends(get_db)):
    url = service.get_url_by_code(db, short_code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return url

@router.delete("/api/v1/urls/{short_code}")
def delete_url(short_code: str, db: Session = Depends(get_db)):
    deleted = service.delete_url(db, short_code)
    if not deleted:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"message": "deleted"}

@router.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = service.get_url_by_code(db, short_code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    if service.is_expired(url):
        raise HTTPException(status_code=410, detail="URL expired")
    service.increment_click(db, url)
    return RedirectResponse(url=url.original_url, status_code=302)
