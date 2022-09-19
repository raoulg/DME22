import click
from loguru import logger

import visualize
from settings import Settings

logger.add("logging.log")


@click.command()
@click.option("--task")
def main(task: str) -> None:
    logger.info(f"Running {task}")
    df = visualize.get_data()
    presets = Settings()
    if task == "scatter":
        visualize.scatter(df, presets, save=True)

    if task == "boxplot":
        visualize.boxplots(df, presets, save=True)

    if task == "linear":
        visualize.linearmodel(df, presets, save=True)

    if task == "growth":
        visualize.growth(df, presets, save=True)
    
    if task == "all":
        visualize.plot_all(df, presets)

if __name__ == "__main__":
    main()
