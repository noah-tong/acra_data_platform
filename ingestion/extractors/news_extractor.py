import json

from pathlib import Path
from datetime import datetime

from ingestion.providers.news import NewsProvider
from ingestion.framework.loader import BronzeLoader
from ingestion.framework.metadata import MetadataWriter


class NewsExtractor:

    def __init__(self):

        self.provider = NewsProvider()

        self.metadata = MetadataWriter()

        self.guid_file = Path(
            "bronze/news/processed_guid.json"
        )

    def load_guid(self):

        if not self.guid_file.exists():

            return set()

        with open(

            self.guid_file,

            "r",

            encoding="utf-8"

        ) as f:

            return set(

                json.load(f)

            )

    def save_guid(

        self,

        guid

    ):

        self.guid_file.parent.mkdir(

            parents=True,

            exist_ok=True

        )

        with open(

            self.guid_file,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                list(guid),

                f,

                indent=4

            )

    def run(self):

        start_time = datetime.utcnow()

        batch_time = start_time

        self.loader = BronzeLoader(

            "news",

            batch_time

        )

        print(

            "Downloading News..."

        )

        news = self.provider.fetch_news()

        processed = self.load_guid()

        news = news[

            ~news["guid"].isin(

                processed

            )

        ]

        self.loader.save_dataframe(

            news,

            "news.csv"

        )

        processed.update(

            news["guid"]

        )

        self.save_guid(

            processed

        )

        end_time = datetime.utcnow()

        self.metadata.write(

            source="news",

            start_time=start_time,

            end_time=end_time,

            success=["rss"],

            failed=[],

            total_records=len(news)

        )

        print(

            f"News Bronze Completed ({len(news)} records)"

        )