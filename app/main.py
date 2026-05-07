from fastapi import FastAPI

from app.api.flights import router as flights_router

app = FastAPI(title="Flight Info")

app.include_router(flights_router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
