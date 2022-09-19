import sys
from pathlib import Path

from loguru import logger
from pydantic import BaseSettings


class Settings(BaseSettings):
    basedir: Path = Path.cwd()
    datadir: Path = Path("data/raw")
    outputdir: Path = Path("data/processed")
    logdir: Path = basedir / "log"

    namecol: str = "name"

settings = Settings()

logger.add(
    sink=settings.logdir / "log_{time:YYYYMMDD}.log",
    rotation="00:00",
    enqueue=True
)
logger.add(
    sink=sys.stdout, 
    colorize=True, 
    format="<green>{time}</green> <level>{message}</level>"
)
logger.add(
    sink=sys.stderr,
    colorize=True,
    format="<green>{time}</green> <level>{message}</level>"
)
