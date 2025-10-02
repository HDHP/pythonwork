import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkitsmplot3d import Axes3D

RADIUS = 1 #constant - dont change!

def anisoenge(x,y,z):
    x1 = x^4
    y1 = y^4
    z1 = z^4
    e1 = (1/2) * (x1 + y1 +z1)
    return e1

def radeng(theta, phi):
    x2 = RADIUS * np.sin(theta) * np.cos(phi)
    y2 = RADIUS * np.sin(theta) * np.sin(phi)
    z = RADIUS * np.cos(theta)
    e2 = anisoenge(x2, y2, z2)
    return e2

#array making now:
theta_array = np.arrange(0, 6.30, 0.01)
phi_array = np.arrange(0, 3.14, 0.01)
theta_grid, phi_grid = np.meshgrid(theta_array, phi_array)
pair_values = 