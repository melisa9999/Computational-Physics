from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
"""Parámetros"""
n = 100  # Number of partitions of the grid
ax = 0  # ax, bx span in x- direction
bx = 10
ay = 0  # ay, by span in y-direction
by = 10
T0x = 100  # TOx, TOy initial temperatures
T0y = 100
Tfx = 20  # Tfx, Tfy final  temperatures
Tfy = 20
tf = 60
k = 0.0001  # thermal diffusivity of the medium

dx = (bx - ax) / n
dy = (by - ay) / n
dt = tf / n

# each dimension's grid

x = np.linspace(ax, bx, n + 1)
y = np.linspace(ay, by, n + 1)
t = np.linspace(0, tf, n + 1)

# Inicialization of the temprature's meshgrid
T = np.zeros((n + 1, n + 1))

# BOUNDARY CONDITIONS

T[0, :] = T0x
T[-1, :] = Tfx
T[:, 0] = T0y
T[:, -1] = Tfy
dT = np.empty((n + 1, n + 1))

TEMP = []
ii = 0
while ii < 100:
    for s in range(1, len(t)):
        for i in range(1, n):
            for j in range(1, n):
                dT[i,
                   j] = (1 / dx**2) * (T[i + 1, j] + T[i - 1, j] +
                                       T[i, j + 1] + T[i, j - 1] - 4 * T[i, j])
        T = T + k * dt * dT
        TEMP.append(T)
    #plt.imshow(T, cmap='hot')
    # plt.show()
    ii += 1

fig = plt.figure()
pcm = plt.pcolormesh(TEMP[0], cmap='hot')
plt.colorbar()

# Function called to update the graphic


def step(i):
    if i >= len(TEMP):
        return
    pcm.set_array(TEMP[i].ravel())
    plt.draw()


anim = animation.FuncAnimation(fig, step, interval=50, frames=10000)

anim.save('heat2D.mp4', fps=500)
plt.show()
