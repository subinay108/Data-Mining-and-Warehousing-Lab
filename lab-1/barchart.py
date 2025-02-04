#WAPP to visualize data using Bar Chart

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6]
y = [1, 5, 3, 5, 7, 8]

plt.bar(x, y)
plt.title('Title of the Chart')
plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.show()