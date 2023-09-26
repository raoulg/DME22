import polars as pl


def prepare_floats(filename, modelsettings) -> pl.DataFrame:
    # the target column is the column we want to predict
    target = modelsettings.target

    df = pl.read_parquet(filename)
    p = (
        # with select we create a context to work on.
        # we want just the float columns and the target column
        df.select(
            [
                pl.col(pl.Float64),  # select float
                pl.col(target),  # and the target column
            ]
        )
        # we melt this selection into a long format
        # the target column is the id column
        .melt(id_vars=target)
        # we create a new context:
        # 1. all cols
        # 2. the mean of the value column, for every variable, renamed to mean/var
        # 3. the std of the value column, for every variable, renamed to std/var
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
        # now we have these new columns, we can calculate a normalized value
        .with_columns(
            [
                pl.struct(["value", "mean/var", "std/var"])
                .apply(lambda x: (x["value"] - x["mean/var"]) / x["std/var"])
                .alias("norm")
            ]
        )
    )  # to normalize the data

    return p
