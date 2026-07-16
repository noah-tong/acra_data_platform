from pyspark.sql import functions as F

def standardize_columns(df):
    for col in df.columns:
        df = df.withColumnRenamed(
            col,
            (
                col.lower()
                .replace(" ", "_")
                .replace("-", "_")
            )
        )
    return df