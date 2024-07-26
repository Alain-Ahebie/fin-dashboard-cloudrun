from fastapi import APIRouter, HTTPException, UploadFile, File
from google.cloud import storage
from database import bucket

router = APIRouter()

@router.post("/{asset}")
async def upload_note(asset: str, file: UploadFile = File(...)):
    try:
        blob_name = f"{asset}/{file.filename}"
        blob = bucket.blob(blob_name)
        blob.upload_from_file(file.file, content_type=file.content_type)
        
        # Remove this line as UBLA does not allow setting object-level ACLs
        # blob.make_public()
        
        # Since the bucket is non-public, you might want to provide another way to access the file, like signing a URL (optional)
        # signed_url = blob.generate_signed_url(expiration=datetime.timedelta(hours=1))

        return {"message": "Note uploaded successfully", "file_url": blob_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload note: {str(e)}")

@router.get("/{asset}")
async def get_notes(asset: str):
    try:
        blobs = bucket.list_blobs(prefix=f"{asset}/")
        notes = [{"name": blob.name, "url": blob.public_url} for blob in blobs]
        return notes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get notes: {str(e)}")

@router.get("/{note_id}")
async def get_note(note_id: str):
    try:
        blob = bucket.blob(note_id)
        if not blob.exists():
            raise HTTPException(status_code=404, detail="Note not found")
        return {"name": blob.name, "url": blob.public_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get note: {str(e)}")

@router.put("/{note_id}")
async def update_note(note_id: str, file: UploadFile = File(...)):
    try:
        blob = bucket.blob(note_id)
        blob.upload_from_file(file.file, content_type=file.content_type)
        blob.make_public()
        return {"message": "Note updated successfully", "file_url": blob.public_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update note: {str(e)}")

@router.delete("/{note_id}")
async def delete_note(note_id: str):
    try:
        blob = bucket.blob(note_id)
        blob.delete()
        return {"message": "Note deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete note: {str(e)}")
