#WAPP to visualize data in subplots

import matplotlib.pyplot as plt

# Plot 1
x = [0, 1, 2, 3]
y = [3, 8, 1, 10]

# subplot(row, col, index)
plt.subplot(1, 2, 1)
plt.plot(x, y)

# Plot 2
x = [0, 1, 2, 3]
y = [10, 20, 30, 40]

plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show()