import httpx

OPENSKY_URL = "https://opensky-network.org/api/states/all"


def fetch_flights():
    try:
        response = httpx.get(OPENSKY_URL, timeout=10)

        response.raise_for_status()

        data = response.json()

        states = data.get("states", [])

        print(f"Total flights received: {len(states)}")

        for flight in states[:10]:
            icao24 = flight[0]
            callsign = flight[1]
            origin_country = flight[2]
            longitude = flight[5]
            latitude = flight[6]
            altitude = flight[7]
            velocity = flight[9]

            print(
                {
                    "icao24": icao24,
                    "callsign": callsign,
                    "country": origin_country,
                    "longitude": longitude,
                    "latitude": latitude,
                    "altitude": altitude,
                    "velocity": velocity,
                }
            )

    except Exception as error:
        print(f"Error fetching flight data: {error}")


if __name__ == "__main__":
    fetch_flights()
