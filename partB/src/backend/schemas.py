from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class UrlCreate(BaseModel):
    original_url: HttpUrl
    expires_at: Optional[datetime] = None

class UrlResponse(BaseModel):
    id: int
    original_url: str
    short_code: str
    click_count: int
    created_at: datetime
    expires_at: Optional[datetime]

    class Config:
        from_attributes = True
