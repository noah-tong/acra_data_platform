from datetime import datetime

import pandas as pd
import requests

from config.holiday_config import COUNTRIES


class HolidayProvider:

    BASE_URL = "https://date.nager.at/api/v3/PublicHolidays"

    def fetch_holidays(self):

        rows = []

        current_year = datetime.utcnow().year

        years = [

            current_year,

            current_year + 1

        ]

        for country in COUNTRIES:

            for year in years:

                url = f"{self.BASE_URL}/{year}/{country}"

                try:

                    response = requests.get(

                        url,

                        timeout=30

                    )

                    
                    if response.status_code == 204:

                        print(f"No holiday data: {country} {year}")

                        continue

                    
                    response.raise_for_status()

                    holidays = response.json()

                    for holiday in holidays:

                        rows.append({

                            "country": country,

                            "date": holiday.get("date"),

                            "local_name": holiday.get("localName"),

                            "english_name": holiday.get("name"),

                            "global": holiday.get("global"),

                            "launch_year": holiday.get("launchYear"),

                            "types": ",".join(

                                holiday.get(

                                    "types",

                                    []

                                )

                            )

                        })

                except requests.exceptions.JSONDecodeError:

                    print(f"Invalid JSON: {country} {year}")

                except Exception as e:

                    print(f"{country} {year}: {e}")

        return pd.DataFrame(rows)