#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pandas as pd
import read_data
import numpy as np

bilinear = read_data.fittingBaseGroup.binary_fitting_base_A(1)
bisquare = read_data.fittingBaseGroup.binary_fitting_base_A(2)
bicubic = read_data.fittingBaseGroup.binary_fitting_base_A(3)
csv_data = pd.read_csv("data1.csv", sep=',')
data = np.array(csv_data.iloc[:,[0,1,2]])
fitter1 = read_data.general_fitter("test", data, [0,1], 2, bilinear)
fitter1.set_var_name(['var1','var2'],'var3')
func_file = open("order1.py",'w')
func_file.write(fitter1.generate_result())
func_file.close()

fitter2 = read_data.general_fitter("test", data, [0,1], 2, bisquare)
fitter2.set_var_name(['var1','var2'],'var3')
func_file = open("order2.py",'w')
func_file.write(fitter2.generate_result(fitter1))
func_file.close()

fitter3 = read_data.general_fitter("test", data, [0,1], 2, bicubic)
fitter3.set_var_name(['var1','var2'],'var3')
func_file = open("order3.py",'w')
func_file.write(fitter3.generate_result(fitter2))
func_file.close()

import order1
import order2
import order3
predict = np.zeros(shape = (data.shape[0],))
for i in range(data.shape[0]):
    predict[i] = order1.test(data[i,0],data[i,1])
error = predict-data[:,2]
print(max(abs(error)))
for i in range(data.shape[0]):
    predict[i] = order2.test(data[i,0],data[i,1])
error = predict-data[:,2]
print(max(abs(error)))
for i in range(data.shape[0]):
    predict[i] = order3.test(data[i,0],data[i,1])
error = predict-data[:,2]
print(max(abs(error)))
