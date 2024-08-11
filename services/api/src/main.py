import os
from fastapi import FastAPI
from routes import trades, notes, search, health
import debugpy

# debugpy.listen(("0.0.0.0", 5678))

app = FastAPI()

app.include_router(trades.router, prefix="/trades", tags=["trades"])
app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(search.router, prefix="/search", tags=["search"])
app.include_router(health.router, prefix="/health", tags=["health"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Trading Journal API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4000)
