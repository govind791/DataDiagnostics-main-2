import streamlit as st
import pandas as pd
import numpy as np

# Try importing shared helpers if present
try:
    from utils import load_data, basic_profile
except Exception:
    # Fallbacks if utils.py isn't available for some reason
    def load_data(file) -> pd.DataFrame:
        name = getattr(file, "name", "").lower()
        if name.endswith(".csv"):
            return pd.read_csv(file)
        if name.endswith(".xlsx") or name.endswith(".xls"):
            return pd.read_excel(file)
        # best-effort sniff
        try:
            file.seek(0)
            return pd.read_csv(file)
        except Exception:
            file.seek(0)
            return pd.read_excel(file)

    def basic_profile(df: pd.DataFrame) -> dict:
        return {
            "rows": int(df.shape[0]),
            "cols": int(df.shape[1]),
            "columns": list(df.columns.astype(str)),
            "null_counts": df.isna().sum().to_dict(),
            "dtypes": {c: str(t) for c, t in df.dtypes.items()}
        }

st.set_page_config(page_title="DataDiagnostics — Introduction", page_icon="🩺", layout="wide")

st.title("🩺 DataDiagnostics")
st.caption("A quick, friendly landing page to load your dataset and jump into analysis & visualization.")

with st.expander("What is this?", expanded=False):
    st.markdown(
        "- **Upload** a CSV/Excel file\n"
        "- **Preview** the data and see quick **nulls/dtypes**\n"
        "- Then use the sidebar to open **Data Analysis** or **Data Visualization** pages"
    )

# -------------------------
# Data input
# -------------------------
st.subheader("1) Load data")

left, right = st.columns([2, 1])
with left:
    uploaded = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx", "xls"], accept_multiple_files=False)
with right:
    st.write("Or use a sample dataset:")
    sample = st.selectbox("Sample", ["(none)", "Iris (classification)", "Tips (tabular)"], index=0)

df = None

if uploaded is not None:
    try:
        df = load_data(uploaded)
        st.session_state["df"] = df
        st.success(f"Loaded: {uploaded.name}  •  shape: {df.shape}")
    except Exception as e:
        st.error(f"Could not read the file: {e}")

elif sample != "(none)":
    # lightweight samples
    if sample.startswith("Iris"):
        from sklearn import datasets
        iris = datasets.load_iris(as_frame=True)
        df = iris.frame
    elif sample.startswith("Tips"):
        import seaborn as sns
        df = sns.load_dataset("tips")
    st.session_state["df"] = df
    st.success(f"Loaded sample: {sample}  •  shape: {df.shape}")

# -------------------------
# Data preview & quick profile
# -------------------------
st.subheader("2) Preview & quick profile")
if "df" in st.session_state:
    df = st.session_state["df"]
    with st.container(border=True):
        st.write("**Preview (top 50 rows)**")
        st.dataframe(df.head(50), use_container_width=True)

    prof = basic_profile(df)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Rows", prof["rows"])
        st.metric("Columns", prof["cols"])
    with c2:
        st.write("**Dtypes**")
        st.json(prof["dtypes"])
    with c3:
        st.write("**Null counts**")
        st.json(prof["null_counts"])

    # Small visuals
    st.subheader("3) Quick visuals")
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if num_cols:
        st.write("Numeric summary (describe):")
        st.dataframe(df[num_cols].describe().T, use_container_width=True)
        st.write("Nulls by column (bar):")
        st.bar_chart(df.isna().sum())
    else:
        st.info("No numeric columns detected.")

    st.info("Use the **sidebar** to open: **Data Analysis** or **Data Visualization** pages.")
else:
    st.info("No data loaded yet. Upload a file or select a sample to continue.")
