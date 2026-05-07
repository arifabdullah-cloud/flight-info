from fastapi import FastAPI

from app.api.flights import router as flights_router
from app.api.stats import router as stats_router

app = FastAPI(title="Flight Info")

app.include_router(flights_router)
app.include_router(stats_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
