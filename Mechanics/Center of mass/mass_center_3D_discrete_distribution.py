from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")

num_masses = 300  # number of particles
z_points = 300 * np.random.random(num_masses)
x_points = 300 * np.random.random(num_masses)
y_points = 300 * np.random.random(num_masses)

print(x_points)
print(y_points)
print(z_points)

m_i = 1
m_points = np.ones(len(z_points)) * m_i  # arreglo con las masas iguales
"""
R_cm= sum (m_i*r_i)/ sum (m_i) 

r_i = x_i,y_i,z_i

**CALCULATIONS ARE MADE FROM THE ORIGIN 
** All masses are equal

"""

R = m_i * [sum(x_points), sum(y_points), sum(z_points)] / sum(m_points)

ax.scatter3D(x_points, y_points, z_points)
x_R, y_R, z_R = R  # COORDENADAS DEL CENTRO DE MASA

ax.scatter3D(x_R, y_R, x_R, s=100)

plt.show()
"""
DIFFERENT MASS CASE"""

# m_diff_points = 100 * np.random.random(num_masses)

# R_diff= [np.dot(m_diff_points,x_points), np.dot(m_diff_points,y_points),
#          np.dot(m_diff_points,z_points)]/sum(m_diff_points)

# x_R_diff,y_R_diff, z_R_diff = R_diff

# ax.scatter3D(x_R_diff, y_R_diff, x_R_diff);
# plt.show()
