from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Trade(BaseModel):
    tradedate: Optional[datetime] = None
    entry_price: Optional[float] = Field(None, gt=0)
    exit_price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, gt=0)
    ratio: Optional[float] = None
    TP: Optional[float] = None
    SL: Optional[float] = None
    result: Optional[str] = None
    notes: Optional[str] = None

class NoteUpload(BaseModel):
    filename: str
    content: str

class Metadata(BaseModel):
    total_count: int
    asset: str
    week_start_date: str

class PaginationMetadata(BaseModel):
    total_count: int
    skip: int
    limit: int

class TradesResponse(BaseModel):
    trades: List[Trade]
    metadata: PaginationMetadata
