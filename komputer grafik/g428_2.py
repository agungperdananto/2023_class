from matplotlib import pyplot as plt 

import numpy as np

x = [10, 20, 30, 40]

y = [0, 10, 10, 0]

y_1 = [0, 6, 6, 0]
# x_1[1] = 
# x_1[2] = ?
x_1 = [10, 16, 34, 40]
y_2 = [0, 0, 0, 0]



plt.plot(x, y)
plt.plot(x_1, y_1)
plt.plot(x_1, y_2)
plt.fill_between(x_1, y_1, y_2)
plt.show()