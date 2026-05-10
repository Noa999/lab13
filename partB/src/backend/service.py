import secrets
from datetime import datetime
from sqlalchemy.orm import Session
from models import Url
from schemas import UrlCreate

def generate_short_code(db: Session) -> str:
    while True:
        code = secrets.token_urlsafe(6)
        existing = db.query(Url).filter(Url.short_code == code).first()
        if not existing:
            return code

def create_short_url(db: Session, data: UrlCreate) -> Url:
    code = generate_short_code(db)
    url = Url(
        original_url=str(data.original_url),
        short_code=code,
        expires_at=data.expires_at
    )
    db.add(url)
    db.commit()
    db.refresh(url)
    return url

def get_url_by_code(db: Session, short_code: str):
    return db.query(Url).filter(Url.short_code == short_code).first()

def get_all_urls(db: Session):
    return db.query(Url).order_by(Url.created_at.desc()).all()

def increment_click(db: Session, url: Url):
    url.click_count += 1
    db.commit()

def is_expired(url: Url) -> bool:
    if url.expires_at is None:
        return False
    return datetime.utcnow() > url.expires_at

def delete_url(db: Session, short_code: str) -> bool:
    url = get_url_by_code(db, short_code)
    if not url:
        return False
    db.delete(url)
    db.commit()
    return True
