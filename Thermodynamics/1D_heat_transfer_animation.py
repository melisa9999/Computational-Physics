# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:04:05 2021

@author: SSMM1
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


"""Physical parameters"""
L = 0.1            # Length of modeled domain [m]
n = 100            # Number of partitions
T0 = 0             #Initial temperature
T1s = 40           # T1s and T2s extreme final temperatures
T2s = 20
h = L / n          #Step size
alpha = 0.0001     #thermal diffusivity of the medium
tf = 60            # final time 
dt = 0.1

dTdt = np.empty(n)
x = np.linspace(h / 2, L - h / 2, n)
T = np.ones(n) * T0

t = np.arange(0, tf, dt)
TEMP = []


for j in range(1, len(t)):
    for i in range(1, n - 1):
        dTdt[i] = alpha * (-(T[i] - T[i - 1]) / h**2 + (T[i + 1] - T[i]) / h**2
                           )  # este for crea la sln para un t
    dTdt[0] = alpha * (-(T[0] - T1s) / h**2 +
                       (T[1] - T[0]) / h**2)  # condicion de frontera 1
    dTdt[n - 1] = alpha * (-(T[n - 1] - T[n - 2]) / h**2 +
                           (T2s - T[n - 1]) / h**2)  # frontera 2
    T = T + dTdt * dt
    TEMP.append(T)

    # plt.figure(1)
    # plt.plot(x,T)
    # plt.axis([0,L,0,50])
    # plt.xlabel('Distance [m]')
    # plt.ylabel("Temperature [°C]")
    # plt.show()
    
# TO MAKE THE ANIMATION


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 0.1), ylim=(0, 50))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame

def init():
    line.set_data([], [])
    return line,


# animation function.  This is called sequentially

def animate(i):
    x = np.linspace(h / 2, L - h / 2, n)
    y = TEMP[i]  # acá va la información del estado en cada tiempo
    line.set_data(x, y)
    return line,


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig,
                               animate,
                               init_func=init,
                               frames=400,
                               interval=100,
                               blit=True)

anim.save('basic_animation.mp4', fps=30)
