from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from loguru import logger


def get_data() -> pd.DataFrame:
    return sns.load_dataset("iris")


def savefig(prefix, imagedir):
    tag: str = datetime.now().strftime("%Y%m%d-%H%M") + ".png"
    filename = imagedir / (prefix + tag)
    plt.savefig(filename)
    logger.info(f"Saved file to {filename}")


def scatter(df, presets, save:bool, ax=None):
    args = presets.scatter
    sns.scatterplot(
        data=df,
        x=args["x"],
        y=args["y"],
        hue=presets.target,
        hue_order=presets.speciesorder,
        palette=presets.palette,
        alpha=presets.alpha,
        ax=ax
    )
    plt.title(presets.title)
    savefig("scatter_", presets.imagedir)


def boxplots(df, presets, save: bool, ax=None):
    p = df.melt(id_vars=presets.target)
    sns.boxplot(data=p, x="variable", y="value", hue=presets.target, palette=presets.palette, ax=ax)
    if save:
        plt.title(presets.title)
        savefig("boxplot_", presets.imagedir)


def linearmodel(df, presets, save: bool):
    args = presets.scatter
    sns.lmplot(data=df, x = args["x"], y = args["y"], hue=presets.target,
    lowess=False, ci=98, scatter_kws={'facecolors':'none', 'alpha':0.3}, palette=presets.palette)
    if save:
        plt.title(presets.title)
        savefig("linearmodel_", presets.imagedir)

def growth(df, presets, save: bool, ax=None):
    args = presets.scatter
    df['sepal_frac'] = df.apply(lambda row: row[args["y"]] / row[args["x"]], axis=1)
    sns.histplot(data=df, x='sepal_frac', hue=presets.target, palette=presets.palette, ax=ax)
    if save:
        args = presets.growth
        plt.title(args["title"])
        plt.xlabel(args["xlab"])
        savefig("growth_", presets.imagedir)

def plot_all(df, presets):
    fig, axs = plt.subplots(1, 3, figsize=presets.figsize)
    axs = axs.ravel()
    scatter(df, presets, save=False, ax=axs[0])
    boxplots(df, presets, save=False, ax=axs[1])
    growth(df, presets, save=False, ax=axs[2])
    args = presets.growth
    axs[2].set_title(args["title"])
    axs[2].set_xlabel(args["xlab"])
    fig.suptitle(presets.title)
    savefig("all_", presets.imagedir)


