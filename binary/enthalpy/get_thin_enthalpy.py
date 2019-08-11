#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import pandas

liquid_data = pandas.read_csv("data/enthalpy_liquid.csv", sep=',')
vapor_data = pandas.read_csv("data/enthalpy_vapor.csv", sep=',')

def get_samples(data, n_samples):
    data = np.sort(data)
    n_data = data.shape[0]
    span = (n_data-1)/(n_samples-1)
    samples = []
    for i in range(n_samples-1):
        samples.append(data[int(i*span)])
    samples.append(data[n_data-1])
    return np.array(samples)

thin_data = []
pressures = liquid_data.loc[:,'pressure'].unique()
pressure_samples = get_samples(pressures, 21)
for name, group in liquid_data.groupby('pressure'):
    if name in pressure_samples:
        temperatures = group.loc[:, 'temperature'].unique()
        n_temps = temperatures.size
        temperature_samples = get_samples(temperatures, int(n_temps/2))
        for index, row in group.iterrows():
            if row['temperature'] in temperature_samples:
                thin_data.append([row['pressure'], row['temperature'], row['nitrogen'], row['oxygen']])
df = pandas.DataFrame(thin_data, columns=['pressure','temperature','nitrogen','oxygen'])
df.to_csv( "data/thin_enthalpy_liquid.csv",sep=',',index = False)

thin_data = []
pressures = vapor_data.loc[:,'pressure'].unique()
pressure_samples = get_samples(pressures, 21)
for name, group in vapor_data.groupby('pressure'):
    if name in pressure_samples:
        temperatures = group.loc[:, 'temperature'].unique()
        n_temps = temperatures.size
        temperature_samples = get_samples(temperatures, int(n_temps/2))
        for index, row in group.iterrows():
            if row['temperature'] in temperature_samples:
                thin_data.append([row['pressure'], row['temperature'], row['nitrogen'], row['oxygen']])
df = pandas.DataFrame(thin_data, columns=['pressure','temperature','nitrogen','oxygen'])
df.to_csv( "data/thin_enthalpy_vapor.csv",sep=',',index = False)