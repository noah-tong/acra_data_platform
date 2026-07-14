from pathlib import Path

import pandas as pd


class AircraftProvider:

    def __init__(self):

        self.aircraft_file = Path(
            "config/aircraft_types.csv"
        )

    def get_aircraft_types(self):

        if not self.aircraft_file.exists():

            raise FileNotFoundError(
                self.aircraft_file
            )

        return pd.read_csv(
            self.aircraft_file
        )