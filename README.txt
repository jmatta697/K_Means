Author: Joe Matta
K-means Implementation
12/15/2019

Instructions for running this K-means algorithm

*This program was tested and developed in the PyCharm IDE. The realtime MatPlotLib plot generation did not function well
when the application was run from the command line, so it is suggested that PyCharm is used to run this program.

Version notes (these versions and tools are required to run this program):
    Python 3.7
    matplotlib 3.1.2
    numpy 1.17.4
    pandas 0.25.3

=======================================================
USER GUIDE

Dataset:
    The dataset included with this program (test_data.csv) is a preprocessed version of "segmentation.test" found at
    archive.ics.uci.edu/ml/datasets/Image+Segmentation. The data itself has not been altered, but the file has been
    formatted to work with this K-means algorithm. Please use "test_data.csv" for testing the program.

Test instructions (these instructions are for testing the program. Please follow these instructions the first time
you run the program):

1) Run Main.py
2) At the file input prompt enter "test_data.csv"
    (Any file name can be entered here. As long as the file is properly formatted, the program will process it.)
    After pressing <ENTER>, the first 10 records of the dataset wil be displayed and a menu listing all available
    attributes will be displayed.
3) Choose an attribute for X >>
    Enter "2" to choose REGION-CENTROID-COL as the x value attribute.
4) Choose an attribute for Y >>
    Enter "3" to choose REGION-CENTROID-ROW as the y value attribute.

    *Note: Menu item 1 (1: CLASS) from test_data.csv cannot be used in this program because the attribute values
    are strings (non-numerical).

5) Choose a value for K >>
    Enter "7" to set the number of clusters to 7.
6) Choose the number of iterations >>
    Enter "10" to run ten iterations.
    Pressing <ENTER> here will start the algorithm.
    For each iteration, a plot will be displayed in the PyCharm SciView panel showing the current clusters as well as a
    printout listing the color, centroid location, and list of data points for each resulting cluster for that
    iteration. The plot and printout will be updated each time an iteration finishes and displayed.

    When the algorithm has finished running, sum-squared errors for each cluster will be displayed along with a
    runtime for the algorithm.

