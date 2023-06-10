import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 50)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(x, y_sin)
ax1.plot(x, y_cos)
ax1.fill_between(x, y_sin, y_cos)

x1 = [0, 10, 10, 20, 20]
y1 = [0, 0, 10, 10, 0]
y2 = [-1 for x in x1]

ax2.plot(x1, y1, 'o--')
ax2.plot(x1, y2, 'o--')
ax2.fill_between(x1, y1, y2, color='C2', alpha=0.3)

plt.show()
