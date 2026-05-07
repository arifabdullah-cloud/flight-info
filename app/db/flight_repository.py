from sqlalchemy.orm import Session

from app.models.flight import Flight


def save_flights(db: Session, flights: list):
    for flight_data in flights:
        flight = Flight(
            icao24=flight_data["icao24"],
            callsign=flight_data["callsign"],
            origin_country=flight_data["origin_country"],
            longitude=flight_data["longitude"],
            latitude=flight_data["latitude"],
            baro_altitude=flight_data["baro_altitude"],
            velocity=flight_data["velocity"],
            true_track=flight_data["true_track"],
            vertical_rate=flight_data["vertical_rate"],
            geo_altitude=flight_data["geo_altitude"],
            squawk=flight_data["squawk"],
            on_ground=flight_data["on_ground"],
        )

        db.add(flight)

    db.commit()
