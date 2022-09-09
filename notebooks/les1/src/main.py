import click
from loguru import logger

from settings import Settings
import preprocess

logger.add("logging.log")


@click.command()
@click.option("--file")
def main(file: str) -> None:
    presets = Settings()
    filename = (presets.datadir / file).absolute()

    if not filename.exists():
        logger.warning(f"file {filename} does not exist")
        raise FileNotFoundError
    
    preprocess.clean_file(filename, presets)
    


if __name__ == "__main__":
    main()
