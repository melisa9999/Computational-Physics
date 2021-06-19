
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

# SPHERE PARAMETRIC EQUATIONS

u, v = np.mgrid[0:2.01 * np.pi:0.1, 0:np.pi:0.1]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)

# TOROID
# u, v = np.mgrid[0:2*np.pi:0.1, 0:2*np.pi:0.1]
# x = (2+ np.cos(v))*np.cos(u)
# y = (2+ np.cos(v))*np.sin(u)
# z = np.sin(v)
# WEIRD

# u, v = np.mgrid[0:2*np.pi:0.5, 0:2*np.pi:0.5]
# x = (np.cos(v))*np.cos(u)+3*np.cos(u)*np.cos(v)
# y = ( np.cos(v))*np.sin(u)+3*np.sin(v)*np.cos(u)
# z = np.sin(v)+ 2*np.cos(5*u/2)

ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)

# graph style

# ax.contour3D(x, y, z, cmap='hot')
ax.plot_wireframe(x, y, z, color='black')
# ax.plot_surface(x, y, z, cmap='hot')
"""
DIFFERENT MASS VERSION"""

num_masses = len(x)
m_i = np.ones(z.shape[0] * z.shape[1])
m_diff_points = 100 * np.random.random(num_masses)
R_diff = 1 * [sum(sum(i)) for i in (x, y, z)] / sum(m_i)
x_R_diff, y_R_diff, z_R_diff = R_diff

# GRAPH
ax.scatter3D(x_R_diff, y_R_diff, x_R_diff, color='red', s=150)

ax.view_init(0, 45)
plt.ion()
plt.show()
