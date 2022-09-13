import re
from datetime import datetime
from pathlib import Path
from typing import List

import pandas as pd
from loguru import logger

from settings import Settings

# precompiling the regex is good practice
# it speeds things up
reg = re.compile("^[\w]+")


def clean_name(msg: str) -> str:
    return re.search(reg, msg).group()


def clean_file(filename: Path, presets: Settings) -> None:
    namecol: str = presets.namecol
    outputdir: Path = presets.outputdir
    logger.info(f"reading file {filename}")
    df = pd.read_csv(filename)

    logger.info(f"Cleaning {namecol}")
    df[namecol] = df[namecol].apply(clean_name)

    logger.info(f"Dropping nas")
    select: List[bool] = list(df.isna().sum() > 0)
    before: int = len(df)
    df = df.dropna(subset=df.columns[select], axis="rows")
    after: int = len(df)
    logger.info(f"Dropped {before-after} rows.")

    tag: str = datetime.now().strftime("%Y%m%d-%H%M") + ".csv"
    output = outputdir / tag
    logger.info(f"Writing file to {output}")
    df.to_csv(output, index=False)
