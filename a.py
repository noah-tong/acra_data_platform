from ingestion.providers.news import NewsProvider

provider = NewsProvider()

df = provider.fetch_news()

print(df.head())

print(len(df))