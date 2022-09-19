import click
from loguru import logger

# from settings import Settings

logger.add("logging.log")


@click.command()
@click.option("--task")
def main(task) -> None:
    # presets = Settings()
    pass



if __name__ == "__main__":
    main()
