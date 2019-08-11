#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pandas as pd
import read_data
import numpy as np

bicubic = read_data.fittingBaseGroup.bicubic_fitting_base()
csv_data = pd.read_csv("data1.csv", sep=',')
data = np.array(csv_data.iloc[:,[0,1,2]])
fitter = read_data.general_fitter("test", data, [0,1], 2, bicubic)
fitter.set_var_name(['var1','var2'],'var3')
func_file = open("test_main1.py",'w')
func_file.write(fitter.generate_result())
func_file.close()

from test_main1 import test
predict = np.zeros(shape = (data.shape[0],))
for i in range(data.shape[0]):
    predict[i] = test(data[i,0],data[i,1])
error = predict-data[:,2]
print(max(abs(error)))