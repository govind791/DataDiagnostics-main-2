import pandas as pd
import io

def load_data(file) -> pd.DataFrame:
    """
    Load CSV or Excel file-like object into a DataFrame.
    Supports .csv, .xls, .xlsx.
    """
    name = getattr(file, "name", "").lower()
    if name.endswith(".csv"):
        return pd.read_csv(file)
    if name.endswith(".xlsx") or name.endswith(".xls"):
        return pd.read_excel(file)
    # try sniffing CSV as fallback
    try:
        file.seek(0)
        return pd.read_csv(file)
    except Exception:
        file.seek(0)
        return pd.read_excel(file)

def basic_profile(df: pd.DataFrame) -> dict:
    """
    Return lightweight summary stats for quick diagnostics.
    """
    info = {
        "rows": int(df.shape[0]),
        "cols": int(df.shape[1]),
        "columns": list(df.columns.astype(str)),
        "null_counts": df.isna().sum().to_dict(),
        "dtypes": {c: str(t) for c, t in df.dtypes.items()}
    }
    return info
