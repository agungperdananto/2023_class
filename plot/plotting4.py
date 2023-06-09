import numpy as np
from matplotlib import pyplot as plt
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

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

fy1 = np.array([0, 1, 1, 0])
fy2 = np.array([0.6, 0.6, 0.6, 0.6])
ax3.set_title('fuzzy example')
ax3.plot(x, fy1, 'o--')
ax3.plot(x, fy2, 'o--')
ax3.fill_between(x,fy1, fy2, where=(fy1<fy2), color='C1', alpha=0.3,interpolate=True)


plt.show()