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

settings = Settings()       # This object should be imported in other modules.

# Configure the 'sinks' of the logger (i.e. the outputs to where log information
# is written to).
logger.add(
    sink=settings.logdir / "log_{time:YYYYMMDD}.log",   # A log file with a date stamp.
    rotation="00:00",       # A new log file is created at midnight.
    enqueue=True
)
logger.add(
    sink=sys.stdout,                    # The screen (standard output 'channel').
    colorize=True,                      # Add colors to the messages.
    format="<green>{time}</green> <level>{message}</level>"
)
logger.add(
    sink=sys.stderr,                    # The screen (standard error 'channel').
    colorize=True,                      
    format="<green>{time}</green> <level>{message}</level>"
)
