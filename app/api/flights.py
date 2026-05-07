from fastapi import APIRouter

from app.ingestion.opensky_client import fetch_flights

router = APIRouter(prefix="/flights", tags=["flights"])


@router.get("/live")
def get_live_flights():
    flights = fetch_flights()
    return {
        "count": len(flights),
        "flights": flights,
    }
