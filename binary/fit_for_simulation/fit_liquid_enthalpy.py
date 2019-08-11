#!/usr/bin/env python
#-*- coding:utf-8 -*-
from scipy.optimize import minimize
import numpy as np
import pandas
import matplotlib.pyplot as plt
from fit_tools import create_cubic_polyfit,create_4th_polyfit,derivative_cubic_polyfit,derivative_4th_polyfit

thermo_data = pandas.read_csv("../data/thin_enthalpy_liquid.csv", sep=',')
x = np.array(thermo_data.loc[:,'pressure'])
y = np.array(thermo_data.loc[:,'temperature'])
z1 = np.array(thermo_data.loc[:,'nitrogen'])
z2 = np.array(thermo_data.loc[:,'oxygen'])

create_cubic_polyfit(x,y,z2,"liquid_oxygen_enthalpy","pressure","temperature")
import liquid_oxygen_enthalpy
plt.figure()
z_hat = np.zeros(shape = z2.shape)
for i in range(z2.size):
    z_hat[i] = liquid_oxygen_enthalpy.liquid_oxygen_enthalpy(x[i],y[i])
print(np.max(np.abs(z2-z_hat)))

derivative_cubic_polyfit("liquid_oxygen_enthalpy_mod.txt","x")
derivative_cubic_polyfit("liquid_oxygen_enthalpy_mod.txt","y")

create_cubic_polyfit(x,y,z1,"liquid_nitrogen_enthalpy","pressure","temperature")
import liquid_nitrogen_enthalpy
plt.figure()
z_hat = np.zeros(shape = z1.shape)
for i in range(z1.size):
    z_hat[i] = liquid_nitrogen_enthalpy.liquid_nitrogen_enthalpy(x[i],y[i])
print(np.max(np.abs(z1-z_hat)))


derivative_cubic_polyfit("liquid_nitrogen_enthalpy_mod.txt","x")
derivative_cubic_polyfit("liquid_nitrogen_enthalpy_mod.txt","y")

plt.show()
