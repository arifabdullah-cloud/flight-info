import httpx

from app.services.flight_parser import parse_flight_state

OPENSKY_URL = "https://opensky-network.org/api/states/all"

MALAYSIA_BOUNDS = {
    "min_lat": 0.5,
    "max_lat": 7.5,
    "min_lon": 99.0,
    "max_lon": 120.0,
}


def is_within_bounds(latitude, longitude, bounds):
    if latitude is None or longitude is None:
        return False

    return (
        bounds["min_lat"] <= latitude <= bounds["max_lat"]
        and bounds["min_lon"] <= longitude <= bounds["max_lon"]
    )


def fetch_flights():
    try:
        response = httpx.get(OPENSKY_URL, timeout=10)

        response.raise_for_status()

        data = response.json()

        states = data.get("states", [])

        malaysia_flights = []

        for state in states:
            longitude = state[5]
            latitude = state[6]

            if is_within_bounds(latitude, longitude, MALAYSIA_BOUNDS):
                parsed_flight = parse_flight_state(state)
                malaysia_flights.append(parsed_flight)

        print(f"Total flights received: {len(states)}")
        print(f"Flights near Malaysia/SEA: {len(malaysia_flights)}")

        for flight in malaysia_flights[:20]:
            print(flight)

    except Exception as error:
        print(f"Error fetching flight data: {error}")


if __name__ == "__main__":
    fetch_flights()
