import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-5, 5, 50)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.plot(x, y_sin, 'o--')
ax1.plot(x, y_cos, 'o--')

ax1.fill_between(x, y_sin, y_cos, color='C2', alpha=0.3)

x1 = [0, 1, 1, 2,2, 3]
y1 = [0, 0, 1, 1, 0, 0]
y0 = [-2 for x in x1]

ax2.plot(x1, y1)
ax2.plot(x1, y0)

ax2.fill_between(x1, y1, y0, color='C4', alpha=0.6)
plt.show()