from fastapi import FastAPI

app = FastAPI(title="ToDo API", version="0.1.0")


@app.get("/health")
async def health():
    """Simple healthcheck endpoint"""
    return {"status": "ok", "message": "API is running 🚀"}
