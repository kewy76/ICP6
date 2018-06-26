# Kate Williams
# 6/21/2018

import matplotlib.pyplot as mpl
from sklearn import datasets
import random

irisdataset = datasets.load_iris()  # Load the data set and save it in a variable

theSet = irisdataset.data[:, :2]  # We only take the first two features.
x = []  # List for x variables (sepal length)
y = []  # List for y variable (sepal width)
counter = 0  # Counter variable
while counter < len(theSet):  # Split the data into x and y variables
    x.append(theSet[counter])
    y.append(theSet[counter + 1])
    counter += 2

# Make a random point
point = [random.randint(2, 5), random.randint(2, 5)]

large = []  # Hold our division of points
small = []

# Divide into groups
i = 0
while i < len(x):
    if x[i].max() > 6 and y[i].max() > 6:
        large.append(x[i])
        large.append(y[i])
    else:
        small.append(x[i])
        large.append(y[i])
    i += 1

check = 0
# Classify random point
if point[0] > 6 and point[1] > 6:
    large.append(point)
    check = 1
else:
    small.append(point)

mpl.plot(large, 'bo')
mpl.plot(small, 'ro')
mpl.plot(point, 'go')
mpl.show()

print("The random point is ")
if point == 0:
    print("small")
else:
    print("large")


