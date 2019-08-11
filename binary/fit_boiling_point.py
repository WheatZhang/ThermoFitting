#!/usr/bin/env python
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv
import pandas
from sklearn import linear_model

nitrogen_bp = pandas.read_csv("data/nitrogen_pressure.txt", sep=',')
thermo_max = nitrogen_bp.max()
thermo_min = nitrogen_bp.min()
nitrogen_bp = nitrogen_bp.sub(thermo_min,axis = 1)
nitrogen_bp = nitrogen_bp.div(thermo_max-thermo_min,axis = 1)
oxygen_bp = pandas.read_csv("data/oxygen_pressure.txt", sep=',')
thermo_max = oxygen_bp.max()
thermo_min = oxygen_bp.min()
oxygen_bp = oxygen_bp.sub(thermo_min,axis = 1)
oxygen_bp = oxygen_bp.div(thermo_max-thermo_min,axis = 1)
items = nitrogen_bp.shape[0]
plt.figure()
plt.subplot(121)
plt.plot(range(items), nitrogen_bp, c='r', label = 'Nitrogen')
plt.legend(loc = 'best')
plt.subplot(122)
plt.plot(range(items), oxygen_bp, c='r', label = 'Oxygen')
plt.legend(loc = 'best')

pressure = np.linspace(100,600,items)
for i in range(len(pressure)):
    pressure[i] = (pressure[i]-100)/500
pressure2 = np.array([])
for i in range(len(pressure)):
    pressure2 = np.append(pressure2, pressure[i]*pressure[i])
pressure3 = np.array([])
for i in range(len(pressure2)):
    pressure3 = np.append(pressure3, pressure2[i]*pressure[i])

linear =linear_model.LinearRegression()
# linear = SVR(kernel='linear', C=1000,max_iter=100000)
data_X = np.stack((pressure,pressure2,pressure3),axis=1)
# data_X = thermo_data.iloc[:,0:2]
data_Y = np.array(nitrogen_bp)
linear.fit(data_X, data_Y)
predict_Y = linear.predict(data_X)
print(np.max(np.abs(data_Y-predict_Y)))
print(linear.coef_,linear.intercept_)
plt.subplot(121)
plt.plot(range(items), predict_Y, c = 'b', label = 'Nitrogen')

linear2 =linear_model.LinearRegression()
# data_X = thermo_data.iloc[:,0:2]
data_Y2 = np.array(oxygen_bp)
linear2.fit(data_X, data_Y2)
predict_Y2 = linear2.predict(data_X)
print(np.max(np.abs(data_Y2-predict_Y2)))
print(linear2.coef_,linear2.intercept_)
plt.subplot(122)
plt.plot(range(items), predict_Y2, c = 'b', label = 'Oxygen')

plt.show()