from datetime import datetime

import pandas as pd

from config.config import BRONZE_PATH
from config.cargo_hubs import CARGO_HUBS

from ingestion.framework.loader import BronzeLoader
from ingestion.providers.openmeteo import WeatherProvider


class WeatherExtractor:

    def __init__(self):

        self.provider = WeatherProvider()

    def _get_latest_airport_file(self):

        airport_root = BRONZE_PATH / "airport"

        folders = sorted(

            airport_root.glob("ingestion_datetime=*"),

            reverse=True

        )

        if not folders:

            raise FileNotFoundError(

                "No Airport Bronze data found."

            )

        return folders[0] / "airport.csv"

    def run(self):

        batch_time = datetime.utcnow()

        self.loader = BronzeLoader(

            "weather",

            batch_time

        )

        airport_file = self._get_latest_airport_file()

        airports = pd.read_csv(airport_file)

        airports = airports[

            airports["iata_code"].isin(CARGO_HUBS)

        ]

        weather_records = []

        for _, airport in airports.iterrows():

            try:

                weather = self.provider.get_weather(

                    airport["latitude_deg"],

                    airport["longitude_deg"]

                )

                hourly = weather["hourly"]

                hours = len(hourly["time"])

                for i in range(hours):

                    weather_records.append({

                        "airport_iata": airport["iata_code"],

                        "airport_name": airport["name"],

                        "latitude": airport["latitude_deg"],

                        "longitude": airport["longitude_deg"],

                        "forecast_time": hourly["time"][i],

                        "temperature_c": hourly["temperature_2m"][i],

                        "precipitation_mm": hourly["precipitation"][i],

                        "rain_mm": hourly["rain"][i],

                        "snowfall_cm": hourly["snowfall"][i],

                        "cloud_cover_percent": hourly["cloud_cover"][i],

                        "visibility_m": hourly["visibility"][i],

                        "wind_speed_kmh": hourly["wind_speed_10m"][i],

                        "wind_direction_deg": hourly["wind_direction_10m"][i]

                    })

            except Exception as e:

                print(

                    f"Weather failed: {airport['iata_code']} - {e}"

                )

        weather_df = pd.DataFrame(weather_records)

        self.loader.save_dataframe(

            weather_df,

            "weather.csv"

        )

        print(

            f"Weather Bronze Completed ({len(weather_df)} records)"

        )