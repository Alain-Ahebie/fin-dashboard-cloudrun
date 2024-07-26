from fastapi import APIRouter, HTTPException
from google.cloud import firestore
from models import Trade, PaginationMetadata, TradesResponse
from database import db

router = APIRouter()

@router.post("/{asset}/{week_start_date}", response_model=Trade)
async def create_trade(asset: str, week_start_date: str, trade: Trade):
    try:
        trade_ref = db.collection(asset).document(week_start_date).collection("trades").document()
        trade_ref.set(trade.dict())
        return trade
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create trade: {str(e)}")

@router.get("/{asset}/{week_start_date}", response_model=TradesResponse)
async def get_trades(asset: str, week_start_date: str, skip: int = 0, limit: int = 10):
    try:
        trades_ref = db.collection(asset).document(week_start_date).collection("trades").offset(skip).limit(limit).stream()
        trades = [trade.to_dict() for trade in trades_ref]
        total_count = len(trades)
        metadata = PaginationMetadata(total_count=total_count, skip=skip, limit=limit)
        return TradesResponse(trades=trades, metadata=metadata)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get trades: {str(e)}")

@router.get("/{asset}/{week_start_date}/{trade_id}", response_model=Trade)
async def get_trade(asset: str, week_start_date: str, trade_id: str):
    try:
        trade_ref = db.collection(asset).document(week_start_date).collection("trades").document(trade_id).get()
        if not trade_ref.exists:
            raise HTTPException(status_code=404, detail="Trade not found")
        return trade_ref.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get trade: {str(e)}")

@router.put("/{asset}/{week_start_date}/{trade_id}", response_model=Trade)
async def update_trade(asset: str, week_start_date: str, trade_id: str, trade: Trade):
    try:
        trade_ref = db.collection(asset).document(week_start_date).collection("trades").document(trade_id)
        trade_ref.set(trade.dict(), merge=True)
        return trade
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update trade: {str(e)}")

@router.delete("/{asset}/{week_start_date}/{trade_id}")
async def delete_trade(asset: str, week_start_date: str, trade_id: str):
    try:
        trade_ref = db.collection(asset).document(week_start_date).collection("trades").document(trade_id)
        trade_ref.delete()
        return {"message": "Trade deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete trade: {str(e)}")
