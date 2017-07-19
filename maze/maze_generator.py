import random
import numpy as np

from matplotlib import pyplot as plt
import matplotlib.cm as cm

num_rows = int(input("Rows: "))
num_cols = int(input("Columns: "))


# We'll create an array to hold the information for each cell.
# We'll track the coordinates if a wall exists and also if it has been visited during the search

# M(LEFT, UP, RIGHT, DOWN, CHECK_IF_VISITED)
M = np.zeros((num_rows,num_cols,5), dtype=np.uint8)


# the image contains the map to be displayed
image = np.zeros((num_rows*10,num_cols*10), dtype=np.uint8)

# Set starting row and column
r = 0
c = 0
history = [(r,c)] # These are the visited locations in stack form

# Trace a path through the cells of the maze and open walls along the path.
# This is done with a while loop, until the history is empty
# which means that we have bactracke to the beginning.

while history:
    M[r,c,4] = 1 # set this location as visited
    # check if adjacent cells are valid for moving to
    check = []
