import requests

from config.config import AERODATABOX_API_KEY


class AeroDataBoxProvider:

    BASE_URL = "https://aerodatabox.p.rapidapi.com"

    HEADERS = {
        "x-rapidapi-key": AERODATABOX_API_KEY,
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }

    def fetch_departures(
        self,
        airport_iata,
        from_local,
        to_local
    ):

        url = (
            f"{self.BASE_URL}"
            f"/flights/airports/iata/"
            f"{airport_iata}/"
            f"{from_local}/"
            f"{to_local}"
        )

        params = {
            "withLeg": "true",
            "direction": "Departure",
            "withCancelled": "false",
            "withCodeshared": "false",
            "withCargo": "true",
            "withPrivate": "false",
            "withLocation": "false"
        }

        response = requests.get(
            url,
            headers=self.HEADERS,
            params=params,
            timeout=60
        )

        response.raise_for_status()

        return response.json()