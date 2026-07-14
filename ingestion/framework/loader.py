import json
import shutil

from pathlib import Path
from datetime import datetime

from config.config import BRONZE_PATH


class BronzeLoader:

    def __init__(
        self,
        source,
        batch_time=None
    ):

        self.source = source

        self.batch_time = (
            batch_time
            if batch_time is not None
            else datetime.utcnow()
        )

        self.folder = (
            BRONZE_PATH
            / self.source
            / f"ingestion_datetime={self.batch_time.strftime('%Y-%m-%dT%H-%M-%S')}"
        )

        self.folder.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_csv(
        self,
        source_file,
        filename
    ):

        shutil.copy(
            source_file,
            self.folder / filename
        )

    def save_bytes(
        self,
        filename,
        content
    ):

        with open(
            self.folder / filename,
            "wb"
        ) as f:

            f.write(content)

    def save(
        self,
        airport,
        data
    ):

        with open(
            self.folder / f"{airport}.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def save_dataframe(
        self,
        dataframe,
        filename
    ):

        dataframe.to_csv(
            self.folder / filename,
            index=False
        )