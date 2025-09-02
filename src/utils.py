import pandas as pd

def load_data(path, parse_dates=None):
    df = pd.read_csv(path)
    if parse_dates:
        for c in parse_dates:
            try:
                df[c] = pd.to_datetime(df[c], errors="coerce")
            except Exception:
                pass
    return df