from pathlib import Path
from typing import Dict, List, Tuple

from pydantic import BaseModel


class Settings(BaseModel):
    datadir: Path = Path("data/raw")
    outputdir: Path = Path("data/processed")
    imagedir: Path = Path("reports/img")
    scatter: Dict = {"x": "sepal_length", "y": "sepal_width"}
    growth: Dict = {"title" : "Average growth (width/length)",
    "xlab" : "width/length"}
    speciesorder: List[str] = ["virginica", "versicolor", "setosa"]
    palette: str = "Set1"
    alpha: float = 0.7
    target: str = "species"
    title: str = "Iris dataset"
    figsize: Tuple = (17,8)
