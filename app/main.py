from fastapi import FastAPI
from app.api.v1.router import router as v1_router

app = FastAPI(title="ToDo API", version="0.1.0")


@app.get("/health")
async def health():
    return {"status": "ok", "message": "API is running 🚀"}


app.include_router(v1_router, prefix="/api/v1")
