from pathlib import Path
from typing import List, Tuple

from pydantic import BaseModel


class Settings(BaseModel):
    imagedir: Path = Path("reports/img")
    mu: List[float] = [0., 10.]
    sd: List[float] = [1., 1.]
    figsize: Tuple = (10, 10)
    groups: int = 5
    difference: float = 0.2
    slope: float = 2
    var: float = 0.3
