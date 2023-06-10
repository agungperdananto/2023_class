import numpy as np
from matplotlib import pyplot as plt
x = np.array([0, 1, 2, 3])
zeros = np.array([0, 0, 0, 0])


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

fy1 = np.array([0, 1, 1, 0])
fy2 = np.array([0, 0.4, 0.4, 0])
xa = np.array([0, 0.4, 2.6, 3])

ax1.set_title('fuzzy trapesium')
ax1.plot(x, fy1, 'o--')
ax1.plot(xa, fy2, 'o--')
ax1.plot(x, zeros, 'o--')
ax1.fill_between(xa, fy2, zeros, color='C1', alpha=0.3)


fy1 = np.array([0, 1, 0, 0])
fy2 = np.array([0, 0.4, 0.4, 0])
xa = np.array([0, 0.4, 1.6, 2])

ax2.set_title('fuzzy triangle')
ax2.plot(x, fy1, 'o--')
ax2.plot(xa, fy2, 'o--')
ax2.plot(x, zeros, 'o--')
ax2.fill_between(xa, fy2, zeros, color='C0', alpha=0.3)

plt.show()