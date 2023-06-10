import numpy as np
from matplotlib import pyplot as plt
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True)

ax1.set_title('interpolation=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolation=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                 interpolate=True)
ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                 interpolate=True)

x = np.array([0, 1, 2, 3])
zeros = np.array([0, 0, 0, 0])
fy1 = np.array([0, 1, 1, 0])
fy2 = np.array([0, 0.5, 0.5, 0])
xa = np.array([0, 0.5, 2.5, 3])

ax3.set_title('fuzzy trapesium')
ax3.plot(x, fy1, 'o--')
ax3.plot(xa, fy2, 'o--')
ax3.plot(x, zeros, 'o--')
ax3.fill_between(xa, fy2, zeros, color='C1', alpha=0.3)


fy1 = np.array([0, 1, 0, 0])
fy2 = np.array([0, 0.5, 0.5, 0])
xa = np.array([0, 0.5, 1.5, 2])

ax4.set_title('fuzzy triangle')
ax4.plot(x, fy1, 'o--')
ax4.plot(xa, fy2, 'o--')
ax3.plot(x, zeros, 'o--')
ax4.fill_between(xa, fy2, zeros, color='C0', alpha=0.3)


plt.show()