import httpx

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

        for flight in states:
            longitude = flight[5]
            latitude = flight[6]

            if is_within_bounds(latitude, longitude, MALAYSIA_BOUNDS):
                malaysia_flights.append(flight)

        print(f"Total flights received: {len(states)}")
        print(f"Flights near Malaysia/SEA: {len(malaysia_flights)}")

        for flight in malaysia_flights[:20]:
            print(
                {
                    "icao24": flight[0],
                    "callsign": flight[1],
                    "country": flight[2],
                    "longitude": flight[5],
                    "latitude": flight[6],
                    "altitude": flight[7],
                    "velocity": flight[9],
                }
            )

    except Exception as error:
        print(f"Error fetching flight data: {error}")


if __name__ == "__main__":
    fetch_flights()
