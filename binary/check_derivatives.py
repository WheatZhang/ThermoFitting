#!/usr/bin/env python
#-*- coding:utf-8 -*-
from scipy.optimize import minimize
import numpy as np
import pandas
import matplotlib.pyplot as plt
import fit_data_2
from fit_tools import create_cubic_polyfit,create_4th_polyfit,derivative_cubic_polyfit,derivative_4th_polyfit

derivative_cubic_polyfit("fit_data_2_mod.txt","x")
derivative_cubic_polyfit("fit_data_2_mod.txt","y")
import fit_data_2_Dx
thermo_data = pandas.read_csv("data/thin_data.txt", sep=',', header = None)
x = np.array(thermo_data.iloc[:,0])
y = np.array(thermo_data.iloc[:,1])
z = np.array(thermo_data.iloc[:,2])
z_hat = np.zeros(shape = z.shape)
for i in range(z.size):
    z_hat[i] = fit_data_2_Dx.fit_data_2_Dx(x[i],y[i])
z_cal = np.zeros(shape = z.shape)
for i in range(z.size):
    z_cal[i] = (fit_data_2.fit_data_2(x[i], y[i]) - fit_data_2.fit_data_2(x[i]- 0.1, y[i] )) / 0.1
plt.figure()
items = 21
for i in range(5):
    plt.subplot(230+i+1)
    z_range = []
    for j in range(items):
        z_range.append(i*5*21+j)
    plt.plot(range(items), z_cal[z_range],c='b')
    plt.plot(range(items),z_hat[z_range],c='r')

import fit_data_2_Dy
z_hat = np.zeros(shape = z.shape)
for i in range(z.size):
    z_hat[i] = fit_data_2_Dy.fit_data_2_Dy(x[i],y[i])
z_cal = np.zeros(shape = z.shape)
for i in range(z.size):
    z_cal[i] = (fit_data_2.fit_data_2(x[i],y[i])-fit_data_2.fit_data_2(x[i],y[i]-0.01))/0.01
plt.figure()
items = 21
for i in range(5):
    plt.subplot(230+i+1)
    z_range = []
    for j in range(items):
        z_range.append(i*5*21+j)
    plt.plot(range(items), z_cal[z_range],c='b')
    plt.plot(range(items),z_hat[z_range],c='r')
plt.show()