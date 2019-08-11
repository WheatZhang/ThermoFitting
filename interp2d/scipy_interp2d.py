#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

def f(x,y):
    return np.sin(x) + np.sin(y)

t = np.linspace(-3, 3, 100)
domain = np.meshgrid(t, t)
X, Y = domain
Z = f(*domain)

fig = plt.figure()
ax1 = plt.subplot2grid((2,2), (0,0), aspect='equal')
p = ax1.pcolor(X, Y, Z)
fig.colorbar(p)
CP = ax1.contour(X, Y, Z, colors='k')
ax1.clabel(CP)
ax1.set_title('Contour plot')

nodes = 6 * np.random.rand(50, 2) - 3
xi = nodes[:, 0]
yi = nodes[:, 1]
zi = f(xi, yi)

ax2 = plt.subplot2grid((2,2), (0,1), aspect='equal')
p2 = ax2.pcolor(X, Y, Z)
ax2.scatter(xi, yi, 25, zi)
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)
ax2.set_title('Node selection')

ax3 = plt.subplot2grid((2,2), (1,0), projection='3d', colspan=2, rowspan=2)
#ax3.plot_surface(X, Y, Z, alpha=0.25)
#ax3.scatter(xi, yi, zi, s=25)
cset = ax3.contour(X, Y, Z, zdir='z', offset=-4)
cset = ax3.contour(X, Y, Z, zdir='x', offset=-5)
ax3.set_xlim3d(-5, 3)
ax3.set_ylim3d(-3, 5)
ax3.set_zlim3d(-4, 2)
ax3.set_title('Surface plot')
fig.tight_layout()
plt.show()

from scipy.interpolate import interp2d
interpolant = interp2d(xi, yi, zi, kind='cubic')
plt.figure()
plt.axes().set_aspect('equal')
plt.pcolor(X, Y, interpolant(t, t))
plt.scatter(xi, yi, 25, zi)
CP = plt.contour(X, Y, interpolant(t, t), colors='k')
plt.clabel(CP)
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.title('Piecewise linear interpolation')
plt.show()