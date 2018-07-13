# Master Title

![](./images/custom-logo.png) 

Welcome to the GitHub repository for (subject). This is a (theme) designed to (goal). 

## Getting Started

### Binder

(Consider this option only if WiFi is stable)

If you don't want the hassle of getting setup, you can use the Binder service to experience this tutorial. Just click on the button below:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ericmjl/Network-Analysis-Made-Simple/master)

### Local Setup

For those of you who would like to get setup beforehand and keep a local copy of the repository on your machine, follow along here.

#### Easiest way: Anaconda Distribution of Python

If you have the Anaconda distribution of **Python 3** installed on a Unix-like machine (Linux, macOS, etc.), then run `make conda`, which wraps the commands below.

1. `$ conda env create -f environment.yml`
1. `$ source activate nams`
1. `$ python checkenv.py`

If you do not have the Anaconda distribution, I would highly recommend getting it for [Windows][2], [Mac][3] or [Linux][4]. It provides an isolated Python computing environment that will not interfere with your system Python installation, and comes with a very awesome package manager (`conda`) that makes installation of new packages a single `conda install pkgname` away.

If you're not using Python 3, then check out @jakevdp's talk at SciPy2015 to find out why!

#### Alternative to Anaconda: `pip install`

For those who do not have the capability of installing the Anaconda Python 3 distribution on their computers, please follow the instructions below.

Run `make venv`, which wraps up the commands below. Special thanks to @matt-land for putting this script together.

1. Create a virtual environment for this tutorial, so that the installed packages do not mess with your regular Python environment.
    2. `$ pip install virtualenv`
    3. `$ virtualenv network`
    4. `$ source network/bin/activate`
5. `$ pip install matplotlib networkx pandas hiveplot numpy jupyter`

Check your environment:

1. `$ python checkenv.py`

#### Manual Build

For this tutorial, you will need the following packages:

1. Python 3
2. `matplotlib`
3. `networkx`
4. `pandas`
5. `hiveplot` - `conda install -c conda-forge hiveplot` or `pip install hiveplot`.
1. `nxviz` - `conda install -c conda-forge nxviz`.  (This implements Circos plots; HivePlots are being migrated over.)
6. `numpy`
7. `scipy`
8. `jupyter`

Then, clone the repository locally.

1. `$ cd /path/to/your/directory`
1. Clone the repository to disk:
    1. `$ git clone https://github.com/ericmjl/Network-Analysis-Made-Simple.git`
1. `$ cd Network-Analysis-Made-Simple`


### Run the Jupyter Notebook

    $ jupyter notebook

Your browser will open to an index page where you can click on a notebook to run it. Test that everything runs fine by executing all of the cells in the Instructor versions of the notebooks.

### Run the Jupyter Lab

    $ jupyter lab

Your browser will open to an index page where you can click on a notebook to run it. Test that everything runs fine by executing all of the cells in the Instructor versions of the notebooks.

# Feedback

If you've attended this workshop, please leave [feedback][7]! It's important to help me improve the tutorial for future iterations.

# Issues

## Known Issues

If you get a "Python is not installed as a framework" error with matplotlib, please check out [this issue][8] for instructions to resolve it.

## New Issues

If you're facing difficulties, please report it as an [issue][1] on this repository.

# Credits

1. [Divvy Data Challenge](https://www.divvybikes.com/datachallenge)
1. [Konect Network Analysis Datasets](http://konect.uni-koblenz.de/networks/)

# Resources

1. Jon Charest's use of Circos plots to visualize networks of Metal music genres. [blog post][5] | [notebook][6]
1. Gain further practice by taking this course online at [DataCamp](http://www.datacamp.com/)!
1. A gentle introduction to graph theory on [Vaidehi Joshi's website](https://dev.to/vaidehijoshi/a-gentle-introduction-to-graph-theory)

[1]: https://github.com/ericmjl/Network-Analysis-Made-Simple/issues
[2]: http://repo.continuum.io/archive/Anaconda3-4.0.0-Windows-x86_64.exe
[3]: http://repo.continuum.io/archive/Anaconda3-4.0.0-MacOSX-x86_64.pkg
[4]: http://repo.continuum.io/archive/Anaconda3-4.0.0-Linux-x86_64.sh
[5]: http://jonchar.net/2016/05/20/exploring-metal-subgenres-with-python.html
[6]: http://jonchar.net/notebooks/MA-Exploratory-Analysis#Enter-the-Circos-plot
[7]: https://ericma1.typeform.com/to/aCljQl
[8]: https://github.com/ericmjl/Network-Analysis-Made-Simple/issues/8

## Test your setup

To validate your installation, switch (CD) into the cloned repository in the previous step 
and type:

```python check_setup.py``` 

On my computer, I see (but your version numbers may differ):

```
[✓] scikit-image  0.14.0
[✓] numpy         1.14.5
[✓] scipy         1.1.0
[✓] matplotlib    2.2.2
[✓] notebook      5.4.0
[✓] scikit-learn  0.19.1<br>
```

# Troubleshooting

If you experience an out-of-memory error, you can increase the memory available:
```
NODE_OPTIONS=--max_old_space_size=4096 jupyter lab build
```
or
```
NODE_OPTIONS=--max_old_space_size=4096 jupyter labextension install ...
```
This increases the available memory for the build process to 4Gb

# Data Downloads

The data for this tutorial is not included in the repository.  We will be
using several data sets during the tutorial: most are built-in to
scikit-learn, which
includes code that automatically downloads and caches these
data.

**Because the wireless network
at conferences can often be spotty, it would be a good idea to download these
data sets before arriving at the conference.
Please run**
```bash
python fetch_data.py
```
**to download all necessary data beforehand.**

The download size of the data files are approx. 280 MB, and after `fetch_data.py`
extracted the data on your disk, the ./notebook/dataset folder will take 480 MB
of your local hard drive.