import numpy as np
import matplotlib.pyplot as plt
 
theta = np.linspace( 0 , 2 * np.pi , 150 )
print(theta)
 
radius = 0.4
 
a = radius * np.cos( theta )
b = radius * np.sin( theta )
 
figure, axes = plt.subplots( 1 )
 
axes.plot( a, b )
axes.fill_between(a, b)
a = 0.8 * np.cos( theta ) + 0.4
b = 0.8 * np.sin( theta ) + 0.2

axes.plot( a, b )
axes.set_aspect( 1 )

plt.title( 'Parametric Equation Circle' )
plt.show()