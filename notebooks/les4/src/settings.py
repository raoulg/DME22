from pathlib import Path

from pydantic import BaseModel


class Models(BaseModel):
    root: Path = Path("~/code/DME22/").expanduser()
    processed_dir: Path = Path("data/processed/")
    filename: Path = Path("processed.parq")
    target: str = "species"


modelsettings = Models()