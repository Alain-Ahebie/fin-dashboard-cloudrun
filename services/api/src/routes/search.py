from fastapi import APIRouter, HTTPException
from google.cloud import firestore
from database import db, bucket

router = APIRouter()

@router.get("/trades")
async def search_trades(asset: str, start_date: str, end_date: str):
    try:
        trades = []
        asset_ref = db.collection(asset)
        docs = asset_ref.stream()
        for doc in docs:
            week_start_date = doc.id
            if start_date <= week_start_date <= end_date:
                trades_ref = asset_ref.document(week_start_date).collection("trades").stream()
                trades.extend([trade.to_dict() for trade in trades_ref])
        return trades
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to search trades: {str(e)}")

@router.get("/notes")
async def search_notes(keyword: str):
    try:
        blobs = bucket.list_blobs()
        notes = [{"name": blob.name, "url": blob.public_url} for blob in blobs if keyword in blob.name]
        return notes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to search notes: {str(e)}")
