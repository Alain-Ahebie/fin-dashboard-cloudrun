from fastapi import APIRouter, HTTPException, UploadFile, File
from google.cloud import storage
from datetime import timedelta
from database import bucket
import uuid

router = APIRouter()

@router.post("/{asset}/{year}/{month_week}/{trade_id}")
async def upload_note(asset: str, year: int, month_week: str, trade_id: str, file: UploadFile = File(...)):
    try:
        blob_name = f"{asset}/{year}/{month_week}/{trade_id}/{file.filename}"
        blob = bucket.blob(blob_name)
        blob.upload_from_file(file.file, content_type=file.content_type)
        
        return {"message": "Note uploaded successfully", "file_url": blob.public_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload note: {str(e)}")

@router.get("/{asset}")
async def get_notes_by_asset(asset: str):
    try:
        blobs = bucket.list_blobs(prefix=f"{asset}/")
        notes = [{"name": blob.name, "url": blob.public_url} for blob in blobs]
        return notes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get notes: {str(e)}")

@router.get("/{asset}/{year}/{month_week}")
async def get_notes_by_asset_month_week(asset: str, year: int, month_week: str):
    try:
        blobs = bucket.list_blobs(prefix=f"{asset}/{year}/{month_week}/")
        notes = [{"name": blob.name, "url": blob.public_url} for blob in blobs]
        return notes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get notes: {str(e)}")

@router.get("/{asset}/{year}/{month_week}/{note_id}")
async def get_note(asset: str, year: int, month_week: str, note_id: str):
    try:
        blob_name = f"{asset}/{year}/{month_week}/{note_id}"
        blob = bucket.blob(blob_name)
        if not blob.exists():
            raise HTTPException(status_code=404, detail="Note not found")
        
        return {"name": blob.name, "url": blob.public_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get note: {str(e)}")

@router.put("/{asset}/{year}/{month_week}/{note_id}")
async def update_note(asset: str, year: int, month_week: str, note_id: str, file: UploadFile = File(...)):
    try:
        blob_name = f"{asset}/{year}/{month_week}/{note_id}"
        blob = bucket.blob(blob_name)
        blob.upload_from_file(file.file, content_type=file.content_type)
        
        return {"message": "Note updated successfully", "file_url": blob.public_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update note: {str(e)}")

@router.delete("/{asset}/{year}/{month_week}/{note_id}")
async def delete_note(asset: str, year: int, month_week: str, note_id: str):
    try:
        blob_name = f"{asset}/{year}/{month_week}/{note_id}"
        blob = bucket.blob(blob_name)
        blob.delete()
        return {"message": "Note deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete note: {str(e)}")

@router.get("/download/{asset}/{year}/{month_week}/{note_id}")
async def download_note(asset: str, year: int, month_week: str, note_id: str):
    try:
        blob_name = f"{asset}/{year}/{month_week}/{note_id}"
        blob = bucket.blob(blob_name)
        if not blob.exists():
            raise HTTPException(status_code=404, detail="Note not found")

        # Download the content
        content = blob.download_as_bytes()
        return {"content": content.decode('utf-8')}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to download note: {str(e)}")
