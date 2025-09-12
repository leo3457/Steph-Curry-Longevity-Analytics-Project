import pandas as pd
import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Curry Longevity", layout="wide")
st.title("Steph Curry vs League — Longevity Dashboard")

df = pd.read_csv("data/processed/curry_vs_league_by_season.csv")

metric = st.selectbox("Metric", ["FG3_PCT","TS_PCT","PTS"])
league_map = {"FG3_PCT":"LEAGUE_FG3_PCT_MEAN","TS_PCT":"LEAGUE_TS_PCT_MEAN","PTS":"LEAGUE_PTS_MEAN"}
gap_map = {
    "FG3_PCT": "GAP_FG3_PCT",
    "TS_PCT": "GAP_TS_PCT",
    "PTS": "GAP_PTS",  # or leave out if you don’t want gap points
}
gap_col = gap_map[metric]  # align naming

# Chart
st.line_chart(df.set_index("SEASON")[[metric, league_map[metric]]])

# Build age if not present
if "age" not in df.columns:
    df["year_start"] = df["SEASON"].str.slice(0,4).astype(int)
    df["age"] = df["year_start"] - 1988 + 21 - (2009 - df["year_start"])

use = df.dropna(subset=[gap_col]).copy()
if not use.empty:
    X = use[["age"]].values; y = use[gap_col].values
    model = LinearRegression().fit(X, y)
    ages_future = np.arange(int(use["age"].max())+1, int(use["age"].max())+6).reshape(-1,1)
    pred_gap = model.predict(ages_future)
    crossover_age = next((int(a) for a,g in zip(ages_future.flatten(), pred_gap) if g<0), None)
    st.subheader("Baseline Projection")
    st.write(f"Slope (gap per year): **{model.coef_[0]:.4f}**")
    st.write(f"Projected crossover age: **{crossover_age if crossover_age else 'Not within horizon'}**")
else:
    st.info("Not enough data for regression.")
