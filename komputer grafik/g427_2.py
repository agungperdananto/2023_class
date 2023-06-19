from matplotlib import pyplot as plt 

import numpy as np

x = [0, 10, 20]

y = [0, 10, 0]

y_2 = [0, 6, 6, 0]

x_2 = [0, 6, 14, 20]
y_0 = [0, 0, 0, 0]


plt.plot(x, y)
plt.plot(x_2, y_2)
plt.fill_between(x_2, y_2, y_0)
plt.show()