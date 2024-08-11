from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Trade(BaseModel):
    document_id: Optional[str] = None
    type: Optional[str] = None  
    tradedate: Optional[datetime] = None
    entry_price: Optional[float] = Field(None, gt=0)
    exit_price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, gt=0)
    TP: Optional[float] = None
    SL: Optional[float] = None
    ratio: Optional[float] = None  
    profit: Optional[float] = None  
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
