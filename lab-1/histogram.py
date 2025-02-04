#WAPP to visualize data using Histogram

import numpy as np
import matplotlib.pyplot as plt

# normal(central, standard deviation, no. of values)
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()