from loguru import logger
import streamlit as st
import polars as pl

import preprocess
import visualization
from settings import modelsettings


def main():
    filename = (modelsettings.root / modelsettings.processed_dir / modelsettings.filename).resolve()
    df = pl.read_parquet(filename)
    maxvalues = st.slider("maximum unique values", 1, 3, value=2)
    columns = preprocess.get_utf_columns(df, maxvalues)

    pairplot = st.checkbox("Show pairplot")
    target = st.selectbox("select a columnname", columns)

    p = preprocess.prepare_floats(df, target) 
    visualization.boxplots(p, target)

    if pairplot:
        visualization.pairplot(df.to_pandas(), target)


if __name__ == "__main__":
    main()
