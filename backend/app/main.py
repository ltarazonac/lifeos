from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()

@app.get("/api/v1/health")
def health_check():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "healthy"
    }