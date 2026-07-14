import requests

OURAIRPORTS_URL = "https://davidmegginson.github.io/ourairports-data/airports.csv"


class OurAirportsProvider:

    def fetch(self):

        response = requests.get(
            OURAIRPORTS_URL,
            timeout=60
        )

        response.raise_for_status()

        return response.content