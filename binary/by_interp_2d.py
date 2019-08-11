#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np, matplotlib.pyplot as plt
from scipy.interpolate import interp2d
import pandas

thermo_data = pandas.read_csv("data/thin_data.txt", sep=',', header = None)
thermo_mean = thermo_data.mean()
thermo_max = thermo_data.max()
thermo_min = thermo_data.min()
thermo_data = thermo_data.sub(thermo_min,axis = 1)
thermo_data = thermo_data.div(thermo_max-thermo_min,axis = 1)
data_X = np.array(thermo_data.iloc[:,0])
data_Y = np.array(thermo_data.iloc[:,1])
data_Z = np.array(thermo_data.iloc[:,2])
sample_data_range = []
sample_rule=[0,3,10,17,20]
for i in range(len(sample_rule)):
    for j in range(len(sample_rule)):
        sample_data_range.append(sample_rule[i]+sample_rule[j]*21)
sample_data_X = data_X[sample_data_range]
sample_data_Y = data_Y[sample_data_range]
sample_data_Z = data_Z[sample_data_range]
interpolant = interp2d(sample_data_X, sample_data_Y, sample_data_Z, kind='cubic')
predict_Z = []
for i in range(len(data_X)):
    predict_Z.append(interpolant(data_X[i],data_Y[i]))
predict_Z = np.array(predict_Z).reshape((len(predict_Z),))

plt.figure()
items = 21
plot_range=[2,5,12,15,19]
for i in range(len(plot_range)):
    plt.subplot(230+i+1)
    z_range = []
    for j in range(items):
        z_range.append(i*5*21+j)
    plt.plot(range(items), predict_Z[z_range],c='r')
    plt.plot(range(items), data_Z[z_range],c='b')
print(np.max(np.abs(predict_Z-data_Z)))
a = np.abs(predict_Z-data_Z)

plt.figure()
plt.pcolor(sample_data_X, sample_data_Y, interpolant(sample_data_X, sample_data_Y))

plt.show()

