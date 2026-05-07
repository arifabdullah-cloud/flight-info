from app.db.database import SessionLocal
from app.db.flight_repository import save_flights
from app.ingestion.opensky_client import fetch_flights


def fetch_and_store_flights():
    db = SessionLocal()

    try:
        flights = fetch_flights()

        save_flights(db, flights)

        print(f"Stored {len(flights)} flights into database.")

    finally:
        db.close()


if __name__ == "__main__":
    fetch_and_store_flights()
