import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkitsmplot3d import Axes3D as ax

RADIUS = 1 #constant - dont change!

def anisoenge(x,y,z):
    x1 = np.power(x, 4)
    y1 = np.power(y, 4)
    z1 = np.power(z, 4)
    e1 = (1/2) * (x1 + y1 +z1)
    return e1

def radeng(theta, phi):
    x2 = RADIUS * np.sin(theta) * np.cos(phi)
    y2 = RADIUS * np.sin(theta) * np.sin(phi)
    z2 = RADIUS * np.cos(theta)
    e2 = anisoenge(x2, y2, z2)
    return e2

#array making now:
theta_array = np.arange(0, 6.30, 0.01)
phi_array = np.arange(0, 3.14, 0.01)
theta_grid, phi_grid = np.meshgrid(theta_array, phi_array)

vectorized_radeng = np.vectorize(radeng) #vectorize the function to work over the array (meshgrid is a tuple for arrays)
arreng = vectorized_radeng(theta_grid, phi_grid) #apply the function with the arrays being the inputs
print(arreng)

#time to plot
ax.plot_surface(theta_array, phi_array, arreng, cmap="jet")
