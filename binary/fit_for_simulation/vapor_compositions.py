#!/usr/bin/env python
#-*- coding:utf-8 -*-
from scipy.optimize import minimize
import numpy as np
import pandas
import matplotlib.pyplot as plt
from fit_tools import create_cubic_polyfit,create_4th_polyfit,derivative_cubic_polyfit,derivative_4th_polyfit

thermo_data = pandas.read_csv("../data/thin_data.txt", sep=',', header = None)
x = np.array(thermo_data.iloc[:,0])
y = np.array(thermo_data.iloc[:,1])
z = np.array(thermo_data.iloc[:,2])

create_4th_polyfit(x,y,z,"vapor_oxygen_composition","pressure","temperature")
import vapor_oxygen_composition
z_hat = np.zeros(shape = z.shape)
for i in range(z.size):
    z_hat[i] = vapor_oxygen_composition.vapor_oxygen_composition(x[i],y[i])
print(np.max(np.abs(z-z_hat)))

plt.figure()
items = 21
for i in range(5):
    plt.subplot(230+i+1)
    plt.xlabel("temperature")
    plt.ylabel("vapor oxygen fraction")
    z_range = []
    for j in range(items):
        z_range.append(i*5*21+j)
    plt.plot(range(items), z[z_range], c='b', label="fit")
    plt.plot(range(items), z_hat[z_range], c='r', label="ideal")
    plt.legend(loc="best")
plt.show()

derivative_4th_polyfit("vapor_oxygen_composition_mod.txt","x")
derivative_4th_polyfit("vapor_oxygen_composition_mod.txt","y")

plt.show()

