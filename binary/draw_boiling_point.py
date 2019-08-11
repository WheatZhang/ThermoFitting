#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv
import pandas


nitrogen_bp = pandas.read_csv("data/nitrogen_pressure.txt", sep=',')
oxygen_bp = pandas.read_csv("data/oxygen_pressure.txt", sep=',')

items = nitrogen_bp.shape[0]
plt.figure()
plt.plot(range(items), nitrogen_bp, c='r', label = 'Nitrogen')
plt.plot(range(items), oxygen_bp, c='b', label = 'Oxygen')
plt.legend(loc = 'best')

thermo_data = pandas.read_csv("data/thermo_test.txt", sep=',')
fig = plt.figure()
data_label = ['vapor_n','vapor_o','liquid_n','liquid_o','enthalpy_v','enthalpy_l']
x = thermo_data.iloc[::40,0]
y = thermo_data.iloc[::40,1]
for i in range(1):
    z = thermo_data.iloc[::40,i+2]
    ax = fig.add_subplot(110+i+1, projection='3d')
    ax.scatter3D(x, y, z, s=1)
    ax.set_xlabel('pressure')
    ax.set_ylabel('temperature')
    ax.set_zlabel(data_label[i])
plt.show()
# fig = plt.figure()
# plt.plot(thermo_data.iloc[0:200,1],thermo_data.iloc[0:200,2])
# plt.xlabel('temperature')
# plt.ylabel('vapor_nitrogen')
# fig = plt.figure()
# plt.plot(thermo_data.iloc[100::201,0],thermo_data.iloc[100::201,2])
# plt.xlabel('pressure')
# plt.ylabel('vapor_nitrogen')
# plt.show()