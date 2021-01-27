# Simple K-Means  
![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)
![License](https://img.shields.io/badge/Code%20License-MIT-blue.svg)

This repository hosts a simple solution to the problem to be addressed.  Note that you are dealing with a simplification of the K-Means algorithm [K-means](KmeansDGG/).

# Problem

Given a set of two dimensional points `P (e.g. [(1.1, 2.5), (3.4,1.9)...]`, write a function that calculates simple `K-means`. The expected returned value from the function is: 

1. A set of cluster id that each point belongs to.
2. The coordinates of centroids at the end of iteration.
# Solution

* The solution is a simplification of the K-means algorithm implemented in Sklearn written in Python
* The solution implemented works for n-dimensional clusters for two-dimensional points.
* There are a `fit`, `predict`  and `fit_predict` interfaces similar to Sklearn.
* Euclidean distance has been used in the algorithm.

Considerations: 

The Test.py uses the KMeansDGG Class and It will plot some examples.


## Installation

There are different ways of installing and running this code.

### Git

The easiest way to download and install these tutorials is by using git from the command-line:

    git clone https://github.com/DPGGES/K-Means.git

This will create the directory `K-Means` and download all the files to it.


### Download Zip-File

You can also [download](https://github.com/DPGGES/K-Means/archive/main.zip)
the contents of the GitHub repository as a Zip-file and extract it manually.


### Required Packages

The K-Means require several Python packages to be installed. The packages are listed in
[requirements.txt](https://github.com/DPGGES/K-Means//blob/main/requirements.txt)

To install the required Python packages and dependencies run the following command
in a terminal:

    pip install -r requirements.txt


## How To Run

If you have followed the above installation instructions, you should
now be able to run the software::

    cd ~/K-Means-main
    python Test.py

This should start the K-Means testing.


## License (MIT)

This source-code is published under the [MIT License](https://github.com/DPGGES/K-Means/blob/main/LICENSE)
which allows very broad use for both academic and commercial purposes.

