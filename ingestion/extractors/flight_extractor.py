import time
from datetime import datetime

from config.cargo_hubs import CARGO_HUBS

from ingestion.framework.loader import BronzeLoader
from ingestion.framework.metadata import MetadataWriter
from ingestion.framework.logger import get_logger
from ingestion.providers.aerodatabox import AeroDataBoxProvider

logger = get_logger(__name__)


class FlightExtractor:

    def __init__(self):

        self.provider = AeroDataBoxProvider()

        self.metadata = MetadataWriter()

    def run(self):

        start_time = datetime.utcnow()

        batch_time = start_time

        self.loader = BronzeLoader(
            "flight",
            batch_time
        )

        today = datetime.utcnow().date()

        success = []

        failed = []

        total_records = 0

        logger.info("Starting Flight Extraction...")

        for airport in CARGO_HUBS:

            try:

                logger.info(f"Downloading {airport}")

                all_departures = []

                time_ranges = [

                    (
                        f"{today}T00:00",
                        f"{today}T11:59"
                    ),

                    (
                        f"{today}T12:00",
                        f"{today}T23:59"
                    )

                ]

                for from_local, to_local in time_ranges:

                    result = self.provider.fetch_departures(

                        airport_iata=airport,

                        from_local=from_local,

                        to_local=to_local

                    )

                    departures = result.get(
                        "departures",
                        []
                    )

                    all_departures.extend(
                        departures
                    )

                    time.sleep(1)

                self.loader.save(

                    airport,

                    all_departures

                )

                total_records += len(
                    all_departures
                )

                success.append(
                    airport
                )

                logger.info(

                    f"{airport}: {len(all_departures)} flights"

                )

            except Exception as e:

                failed.append(
                    airport
                )

                logger.error(

                    f"{airport}: {e}"

                )

        end_time = datetime.utcnow()

        self.metadata.write(

            source="flight",

            start_time=start_time,

            end_time=end_time,

            success=success,

            failed=failed,

            total_records=total_records

        )

        logger.info(
            "Flight Extraction Finished"
        )

        logger.info(
            f"Success: {len(success)}"
        )

        logger.info(
            f"Failed: {len(failed)}"
        )

        logger.info(
            f"Total Flights: {total_records}"
        )