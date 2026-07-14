from datetime import datetime

from ingestion.framework.loader import BronzeLoader
from ingestion.framework.metadata import MetadataWriter

from ingestion.providers.holiday import HolidayProvider


class HolidayExtractor:

    def __init__(self):

        self.provider = HolidayProvider()

        self.metadata = MetadataWriter()

    def run(self):

        start_time = datetime.utcnow()

        batch_time = start_time

        self.loader = BronzeLoader(

            "holiday",

            batch_time

        )

        print(

            "Downloading Holidays..."

        )

        holidays = self.provider.fetch_holidays()

        self.loader.save_dataframe(

            holidays,

            "holiday.csv"

        )

        end_time = datetime.utcnow()

        self.metadata.write(

            source="holiday",

            start_time=start_time,

            end_time=end_time,

            success=["holiday"],

            failed=[],

            total_records=len(

                holidays

            )

        )

        print(

            f"Holiday Bronze Completed ({len(holidays)} records)"

        )