import feedparser
import pandas as pd

from config.news_sources import RSS_SOURCES


class NewsProvider:

    def fetch_news(self):

        rows = []

        for source, url in RSS_SOURCES.items():

            feed = feedparser.parse(url)

            for item in feed.entries:

                rows.append({

                    "guid":
                        item.get(
                            "id",
                            item.get(
                                "guid",
                                item.get(
                                    "link",
                                    ""
                                )
                            )
                        ),

                    "source":
                        source,

                    "title":
                        item.get(
                            "title",
                            ""
                        ),

                    "summary":
                        item.get(
                            "summary",
                            ""
                        ),

                    "published_at":
                        item.get(
                            "published",
                            ""
                        ),

                    "link":
                        item.get(
                            "link",
                            ""
                        ),

                    "category":
                        ",".join(

                            [

                                tag.term

                                for tag in item.get(
                                    "tags",
                                    []
                                )

                            ]

                        )

                })

        return pd.DataFrame(rows)