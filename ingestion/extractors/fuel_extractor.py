from datetime import datetime

from ingestion.framework.loader import BronzeLoader
from ingestion.providers.eia import FuelProvider


class FuelExtractor:

    def __init__(self):

        self.provider = FuelProvider()

    def run(self):

        batch_time = datetime.utcnow()

        self.loader = BronzeLoader(

            "fuel",

            batch_time

        )

        print(

            "Downloading Jet Fuel Price..."

        )

        fuel = self.provider.fetch_jet_fuel_price()

        self.loader.save_dataframe(

            fuel,

            "jet_fuel_price.csv"

        )

        print(

            f"Fuel Bronze Completed ({len(fuel)} records)"

        )