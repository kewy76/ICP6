# Kate Williams
# 6/21/2018

import matplotlib.pyplot as mpl
from sklearn import datasets

irisdataset = datasets.load_iris()

x = irisdataset.data[:, :2]  # we only take the first two features.
y = irisdataset.target

mpl.plot(x, y, 'ro')
mpl.show()