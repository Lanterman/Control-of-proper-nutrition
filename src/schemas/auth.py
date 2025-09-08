import datetime

from typing import Optional
from pydantic import BaseModel


class BaseToken(BaseModel):
    """Base token - schema"""

    access_token: str
    refresh_token: str
    expires: datetime.datetime
    type: Optional[str] = "Bearer"
