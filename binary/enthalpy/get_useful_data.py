#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import pandas
from sklearn import  linear_model

thermo_data = pandas.read_csv("data/enthalpy_result.csv", sep=',')
liquid_data = thermo_data.loc[thermo_data['vaporFraction']==0,:]
# print(liquid_data.info())
useful_data = []
for name, group in liquid_data.groupby(['pressure', 'temperature']):
    if group.shape[0] < 2:
        continue
    else:
        x = group.loc[:,'nitrogen']
        y = group.loc[:,'enthalpy']
        linear = linear_model.LinearRegression()
        linear.fit(np.array(x).reshape(-1,1), y)
        predict_Y = linear.predict(np.array([0,1]).reshape(-1,1))
        nitrogen_enthalpy = predict_Y[0]
        oxygen_enthalpy = predict_Y[1]
        useful_data.append([name[0],name[1],nitrogen_enthalpy,oxygen_enthalpy])
df = pandas.DataFrame(useful_data, columns=['pressure','temperature','nitrogen','oxygen'])
df.to_csv( "data/enthalpy_liquid.csv",sep=',',index = False)

vapor_data = thermo_data.loc[thermo_data['vaporFraction']==1,:]
# print(liquid_data.info())
useful_data = []
for name, group in vapor_data.groupby(['pressure', 'temperature']):
    if group.shape[0] < 2:
        continue
    else:
        x = group.loc[:,'nitrogen']
        y = group.loc[:,'enthalpy']
        linear = linear_model.LinearRegression()
        linear.fit(np.array(x).reshape(-1,1), y)
        predict_Y = linear.predict(np.array([0,1]).reshape(-1,1))
        nitrogen_enthalpy = predict_Y[0]
        oxygen_enthalpy = predict_Y[1]
        useful_data.append([name[0],name[1],nitrogen_enthalpy,oxygen_enthalpy])
df = pandas.DataFrame(useful_data, columns=['pressure','temperature','nitrogen','oxygen'])
df.to_csv( "data/enthalpy_vapor.csv",sep=',',index = False)