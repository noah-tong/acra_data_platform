from datetime import datetime

from ingestion.providers.ourairports import (
    OurAirportsProvider
)

from ingestion.framework.loader import (
    BronzeLoader
)


class AirportExtractor:

    def __init__(self):

        self.provider = OurAirportsProvider()

    def run(self):

        batch_time = datetime.utcnow()

        self.loader = BronzeLoader(

            "airport",

            batch_time

        )

        print("Downloading Airport Database...")

        csv_bytes = self.provider.fetch()

        self.loader.save_bytes(

            filename="airport.csv",

            content=csv_bytes

        )

        print("Airport Bronze Completed.")