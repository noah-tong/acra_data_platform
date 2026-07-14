import requests


class WeatherProvider:

    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_weather(
        self,
        latitude,
        longitude
    ):

        params = {

            "latitude": latitude,

            "longitude": longitude,

            "hourly": ",".join([

                "temperature_2m",
                "precipitation",
                "rain",
                "snowfall",
                "cloud_cover",
                "visibility",
                "wind_speed_10m",
                "wind_direction_10m"

            ]),

            "daily": ",".join([

                "weather_code",
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_sum",
                "wind_speed_10m_max"

            ]),

            "forecast_days": 7,

            "timezone": "UTC"

        }

        response = requests.get(

            self.BASE_URL,

            params=params,

            timeout=30

        )

        response.raise_for_status()

        return response.json()