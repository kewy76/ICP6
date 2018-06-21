# Kate Williams
# 6/21/2018

import pandas as pd
import matplotlib.pyplot as mpl
import numpy as np
from decimal import Decimal

path = 'C:\\Users\Katie Williams\Downloads\Python_Lesson6\Python_Lesson6\sample_stocks.csv'

theData = pd.read_csv(path)

data = []
k = 0
while k < 650:
    data.insert(k, theData)  # Read in data
    k += 1

k = 3  # Number of clusters
i = 0  # Counter variable
centroids = [0, 0, 0, 0, 0, 0]  # Array to hold x and y values of centroids
firstCluster = []
secondCluster = []
thirdCluster = []

while i < k:  # Select (at random) k points
    centroids[i] = np.random.randint(-19, 41)
    i += 1

one = 0
two = 0
three = 0
j = 0  # Counter variable for the points
while j < 649:
    one = np.sqrt(((data[j] + centroids[0])**2) + ((data[j+1] + centroids[1])**2))
    two = np.sqrt(((data[j] + centroids[2])**2) + ((data[j + 1] + centroids[3])**2))
    three = np.sqrt(((data[j] + centroids[4])**2) + ((data[j+1] + centroids[5])**2))
    if one < two and one < three:  # If the point is closest to the first centroid
        firstCluster.append(data[j])
        firstCluster.append(data[j+1])
    elif two < one and two < three:
        secondCluster.append(data[j])
        secondCluster.append(data[j+1])
    else:
        thirdCluster.append(data[j])
        thirdCluster.append(data[j+1])
    j += 2

print(firstCluster)