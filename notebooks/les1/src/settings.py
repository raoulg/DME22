from pathlib import Path

from loguru import logger
from pydantic import BaseModel


class Settings(BaseModel):
    basedir: Path = Path.cwd()
    datadir: Path = Path("data/raw")
    outputdir: Path = Path("data/processed")
    logdir: Path = basedir / "log"

    namecol: str = "name"


settings = Settings()  # This object should be imported in other modules.
logger.add("logfile.log")
