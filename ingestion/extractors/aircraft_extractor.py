from datetime import datetime

from ingestion.framework.loader import BronzeLoader
from ingestion.providers.aircraft import AircraftProvider


class AircraftExtractor:

    def __init__(self):

        self.provider = AircraftProvider()

    def run(self):

        batch_time = datetime.utcnow()

        self.loader = BronzeLoader(

            "aircraft",

            batch_time

        )

        print(

            "Loading Aircraft Reference..."

        )

        aircraft = self.provider.get_aircraft_types()

        self.loader.save_dataframe(

            aircraft,

            "aircraft_reference.csv"

        )

        print(

            "Aircraft Bronze Completed."

        )