import streamlit as st
import pandas as pd
from utils import load_data, basic_profile

st.set_page_config(page_title="DataDiagnostics", page_icon="🩺", layout="wide")

st.title("🩺 DataDiagnostics")
st.caption("Fast, lightweight data checks and visualizations.")

with st.expander("About", expanded=False):
    st.write("Upload a CSV/Excel file to get started. Your data stays in your session only.")

# File uploader
uploaded = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx", "xls"], accept_multiple_files=False)

# Sample data option
samples = {
    "— choose a sample —": None,
    "Iris (classification)": "iris",
    "Tips (regression-like)": "tips"
}
sample_choice = st.selectbox("...or load a sample dataset", list(samples.keys()))

if uploaded:
    df = load_data(uploaded)
    st.session_state["df"] = df
    st.success(f"Loaded: {uploaded.name}  •  shape: {df.shape}")
elif sample_choice and samples[sample_choice]:
    from sklearn import datasets
    if samples[sample_choice] == "iris":
        iris = datasets.load_iris(as_frame=True)
        df = iris.frame
    elif samples[sample_choice] == "tips":
        # lightweight inline tips dataset
        import seaborn as sns
        df = sns.load_dataset("tips")
    st.session_state["df"] = df
    st.success(f"Loaded sample: {sample_choice}  •  shape: {df.shape}")
else:
    if "df" not in st.session_state:
        st.info("No data loaded yet. Upload a file or pick a sample to continue.")

# Quick peek + profile
if "df" in st.session_state:
    df = st.session_state["df"]
    st.subheader("👀 Preview")
    st.dataframe(df.head(50), use_container_width=True)

    st.subheader("🧾 Quick profile")
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

    st.caption("Navigate to **Data Analysis** or **Data Visualization** from the sidebar.")
