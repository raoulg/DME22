import polars as pl
from typing import List
from pathlib import Path


def prepare_floats(df, target) -> pl.DataFrame:

    p = (
        df.select(
            [
                pl.col(pl.Float64),  # select float
                pl.col(target),  # and the target column
            ]
        )
        .melt(id_vars=target)
        .select(
            [  # melt on target
                pl.col("*"),
                pl.col("value")
                .mean()
                .over("variable")
                .alias("mean/var"),  # create mean
                pl.col("value").std().over("variable").alias("std/var"),  # and std
            ]
        )
        .with_columns(
            [
                pl.struct(["value", "mean/var", "std/var"])
                .apply(lambda x: (x["value"] - x["mean/var"]) / x["std/var"])
                .alias("norm")
            ]
        )
    )  # to normalize the data

    return p

def get_utf_columns(df, maxvalue) -> List[str]:
    df_utf = df.select(pl.col(pl.Utf8))
    df = pl.select([s for s in df_utf if s.n_unique() <= maxvalue])
    return df.columns