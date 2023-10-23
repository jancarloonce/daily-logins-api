import pandas as pd


def date_cleaner(path):
    df = pd.read_csv(path)
    df['timestamp_dt'] = pd.to_datetime(
        df['timestamp'], errors='coerce', utc=True)
    df = df.dropna()
    return df
