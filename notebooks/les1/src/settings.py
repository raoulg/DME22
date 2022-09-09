from pathlib import Path

from pydantic import BaseModel


class Settings(BaseModel):
    datadir: Path = Path("data/raw")
    outputdir: Path = Path("data/processed")
    namecol: str = "name"
