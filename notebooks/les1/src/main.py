import click
from loguru import logger

# this imports the complete preprocess.py file namespace
import preprocess
# this imports from the settings.py file
from settings import Settings

# this logs to a file
logger.add("logging.log")


# this processes the command line arguments as parameters for your function
@click.command()
@click.option("--file")
def main(file: str) -> None:
    # initializing settings.Settings()
    presets = Settings()
    filename = (presets.datadir / file).absolute()

    if not filename.exists():
        logger.warning(f"file {filename} does not exist")
        raise FileNotFoundError

    preprocess.clean_file(filename, presets)


if __name__ == "__main__":
    main()
