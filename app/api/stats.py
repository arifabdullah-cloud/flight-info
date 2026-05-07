from collections import Counter

from fastapi import APIRouter

from app.ingestion.opensky_client import fetch_flights

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/")
def get_flight_stats():
    flights = fetch_flights()

    total_flights = len(flights)

    country_counter = Counter()

    airborne_count = 0
    on_ground_count = 0

    for flight in flights:
        country = flight["origin_country"]

        country_counter[country] += 1

        if flight["on_ground"]:
            on_ground_count += 1
        else:
            airborne_count += 1

    top_countries = dict(country_counter.most_common(10))

    return {
        "total_flights": total_flights,
        "airborne": airborne_count,
        "on_ground": on_ground_count,
        "top_countries": top_countries,
    }
