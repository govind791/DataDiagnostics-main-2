import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Data Analysis")

if "df" not in st.session_state:
    st.warning("No data found. Go to **Home** and upload or select a sample.")
    st.stop()

df = st.session_state["df"]

st.subheader("Overview")
st.write(f"Shape: **{df.shape[0]} rows × {df.shape[1]} columns**")
st.dataframe(df.head(100), use_container_width=True)

st.subheader("Summary statistics")
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
if num_cols:
    st.write(df[num_cols].describe().T)
else:
    st.info("No numeric columns detected.")

st.subheader("Column-wise nulls")
st.bar_chart(df.isna().sum())

st.subheader("Value counts")
target_col = st.selectbox("Pick a column", df.columns, index=0)
vc = df[target_col].value_counts(dropna=False).head(50)
st.write(vc)

st.subheader("Correlation (numeric)")
if len(num_cols) >= 2:
    corr = df[num_cols].corr(numeric_only=True)
    st.dataframe(corr.style.background_gradient(axis=None), use_container_width=True)
else:
    st.info("Need at least 2 numeric columns for correlation.")
