from datetime import datetime
from pathlib import Path

from config.config import BRONZE_PATH
from config.source_config import SOURCE_CONFIG

# Development Mode
DEBUG = True


class Scheduler:

    def should_run(self, source: str) -> bool:

        if DEBUG:
            return True

        refresh_hours = SOURCE_CONFIG[source]["refresh_hours"]

        source_folder = BRONZE_PATH / source

        if not source_folder.exists():
            return True

        folders = sorted(source_folder.glob("ingestion_datetime=*"))

        if not folders:
            return True

        latest_folder = folders[-1]

        latest_time = latest_folder.name.replace(
            "ingestion_datetime=",
            ""
        )

        latest_datetime = datetime.strptime(
            latest_time,
            "%Y-%m-%dT%H-%M-%S"
        )

        now = datetime.utcnow()

        elapsed_hours = (
            now - latest_datetime
        ).total_seconds() / 3600

        return elapsed_hours >= refresh_hours