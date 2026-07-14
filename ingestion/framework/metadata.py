import json

from pathlib import Path

from datetime import datetime

from config.config import BRONZE_PATH


class MetadataWriter:

    def write(

        self,

        source,

        start_time,

        end_time,

        success,

        failed,

        total_records

    ):

        folder = BRONZE_PATH / "metadata"

        folder.mkdir(

            parents=True,

            exist_ok=True

        )

        today = datetime.utcnow().strftime(

            "%Y-%m-%d"

        )

        file = folder / f"{today}.json"

        metadata = {

            "source": source,

            "batch_date": today,

            "start_time": start_time.isoformat(),

            "end_time": end_time.isoformat(),

            "duration_seconds": round(

                (end_time - start_time).total_seconds(),

                2

            ),

            "successful_items": success,

            "failed_items": failed,

            "successful_count": len(success),

            "failed_count": len(failed),

            "total_records": total_records

        }

        with open(

            file,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                metadata,

                f,

                indent=4

            )