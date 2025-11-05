import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📈 Data Visualization")

if "df" not in st.session_state:
    st.warning("No data found. Go to **Home** and upload or select a sample.")
    st.stop()

df = st.session_state["df"]

st.subheader("Pick variables")
cols = df.columns.tolist()
x = st.selectbox("X axis", cols, index=0)
y = st.selectbox("Y axis (optional)", ["(none)"] + cols, index=0)
color = st.selectbox("Color (optional)", ["(none)"] + cols, index=0)

plot_type = st.selectbox("Plot type", ["Scatter", "Line", "Histogram", "Box", "Bar"], index=0)

kw = {}
if color != "(none)":
    kw["color"] = color

fig = None
try:
    if plot_type == "Scatter" and y != "(none)":
        fig = px.scatter(df, x=x, y=y, **kw)
    elif plot_type == "Line" and y != "(none)":
        fig = px.line(df, x=x, y=y, **kw)
    elif plot_type == "Histogram":
        fig = px.histogram(df, x=x, **kw)
    elif plot_type == "Box":
        fig = px.box(df, x=x, **kw)
    elif plot_type == "Bar":
        if y != "(none)":
            fig = px.bar(df, x=x, y=y, **kw)
        else:
            # count plot
            fig = px.bar(df[x].value_counts().reset_index(), x="index", y=x)
    else:
        st.info("Select a valid combination of axes.")
except Exception as e:
    st.error(f"Plot failed: {e}")

if fig is not None:
    st.plotly_chart(fig, use_container_width=True)
