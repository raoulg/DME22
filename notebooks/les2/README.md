# Setup

The setup of this lesson is like this

├── 1-demo.ipynb                <- notebooks
├── 2-explore_excercise.ipynb
├── 3-explore_solutions.ipynb
├── README.md                   <- this file
├── data                        <- datafolder
│   ├── processed                   <- to save processed data 
│   └── raw
│       └── diamonds.csv
├── reports                     <- to save pdfs / reports
│   └── img                     <- to save generated images, used in reports
│       ├── all_20220919-1151.png
│       ├── boxplot_20220919-1150.png
│       ├── growth_20220919-1151.png
│       ├── linearmodel_20220919-1150.png
│       └── scatter_20220919-1150.png
└── src
    ├── __init__.py
    ├── main.py                 <- This reproduces all plots used in the report
    ├── settings.py             <- all settings to generate the plots
    └── visualize.py            <- all visualisation code


The demo shows you how to explore the iris dataset. It just showcases different tips&tricks
with seaborn / matplotlib.

You will NOT send a jupyter notebook to your client!
As we have said before: notebooks are just for testing / prototyping.
To make reproducable code, we use the main.py file. 

To generate the individual plots, you first need to spwan the shell with the python environment:

$ poetry shell

After that, you can run the different tasks:

$python src/main.py --task=scatter
$python src/main.py --task=boxplot
$python src/main.py --task=linear
$python src/main.py --task=growth

And, finally, a plot that puts three plots inside a subplot:
$python src/main.py --task=all