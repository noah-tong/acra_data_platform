import requests
import pandas as pd

from config.config import EIA_API_KEY


class FuelProvider:

    BASE_URL = "https://api.eia.gov/v2/petroleum/pri/spt/data/"

    def fetch_jet_fuel_price(self):

        params = {

            "api_key": EIA_API_KEY,

            "frequency": "weekly",

            "data[0]": "value",

            "facets[product][]": "EPJK",

            "sort[0][column]": "period",

            "sort[0][direction]": "desc",

            "offset": 0,

            "length": 1

        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=30
        )

        print("=" * 80)
        print("Status Code:", response.status_code)
        print("Response:")
        print(response.text)
        print("=" * 80)

        response.raise_for_status()

        data = response.json()["response"]["data"]

        return pd.DataFrame(data)