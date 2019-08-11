#!/usr/bin/env python
#-*- coding:utf-8 -*-
from scipy.optimize import minimize
import numpy as np
import pandas
import matplotlib.pyplot as plt
from fit_tools import create_cubic_polyfit,create_4th_polyfit,derivative_cubic_polyfit,derivative_4th_polyfit

thermo_data = pandas.read_csv("thin_density_result.txt", sep=',', header = None)
x = np.array(thermo_data.iloc[:,0])
y = np.array(thermo_data.iloc[:,1])
z1 = np.array(thermo_data.iloc[:,2])
z2 = np.array(thermo_data.iloc[:,3])

create_cubic_polyfit(x,y,z1,"vapor_density","pressure","temperature")
import vapor_density
z_hat = np.zeros(shape = z1.shape)
for i in range(z1.size):
    z_hat[i] = vapor_density.vapor_density(x[i],y[i])
print(np.max(np.abs(z1-z_hat))/(np.max(z1)-np.min(z1)))

plt.figure()
items = 21
for i in range(5):
    plt.subplot(230+i+1)
    plt.xlabel("temperature")
    plt.ylabel("vapor density")
    z_range = []
    for j in range(items):
        z_range.append(i*5*21+j)
    plt.plot(range(items), z1[z_range],c='b')
    plt.plot(range(items),z_hat[z_range],c='r')
    plt.plot(range(items), z1[z_range], c='b', label="fit")
    plt.plot(range(items), z_hat[z_range], c='r', label="ideal")
    plt.legend(loc="best")
plt.show()

# create_cubic_polyfit(x,y,z2,"liquid_density","pressure","temperature")
# import liquid_density
# z_hat = np.zeros(shape = z2.shape)
# for i in range(z2.size):
#     z_hat[i] = liquid_density.liquid_density(x[i],y[i])
# print(np.max(np.abs(z2-z_hat)))
#
# plt.figure()
# items = 21
# for i in range(5):
#     plt.subplot(230+i+1)
#     plt.xlabel("temperature")
#     plt.ylabel("liquid density")
#     z_range = []
#     for j in range(items):
#         z_range.append(i*5*21+j)
#     plt.plot(range(items), z2[z_range],c='b',label = "fit")
#     plt.plot(range(items),z_hat[z_range],c='r',label = "ideal")
#     plt.legend(loc="best")
# plt.show()
