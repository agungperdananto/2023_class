import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 20)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.plot(x, y_sin, 'o--')
ax1.plot(x, y_cos, 'o--')

ax1.fill_between(x, y_sin, y_cos)

x1 = [10, 20, 20, 40, 40, 50]
y1 = [0, 0, 10, 10, 0, 0]
y2  = [-2 for y in x1]

ax2.plot(x1, y1)
ax2.plot(x1, y2)
ax2.fill_between(x1, y1, y2, color='C2', alpha=0.5)

x3 = [0, 2, 4]
y3 = [0, 10, 0]
ax3.plot(x3, y3)
plt.show()