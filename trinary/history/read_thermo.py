#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pandas as pd
import read_data
import numpy as np

csv_data = pd.read_csv("filteredTriThermo.csv", sep='\t')
nominal_P=200
nominal_T=-182
nominal_xN2=0.4
P_deviation = 50
T_deviation = 4
xN2_deviation = 0.05

def indicator_func(df):
    return (df["P"]>(nominal_P-P_deviation)) & (df["P"]<(nominal_P+P_deviation)) &\
           (df["T"]>(nominal_T-T_deviation)) & (df["T"]<(nominal_T+T_deviation)) &\
           (df["x_N2"]>(nominal_xN2-xN2_deviation)) & (df["x_N2"]<(nominal_xN2+xN2_deviation))
selected_data = csv_data[indicator_func(csv_data)]
print(selected_data.shape[0])
selected_data = selected_data.sample(frac=1.0)  # 全部打乱
cut_idx = int(round(0.5 * selected_data.shape[0]))
df_test, df_train = selected_data.iloc[:cut_idx], selected_data.iloc[cut_idx:]
print(df_test.shape[0])

trilinear = read_data.fittingBaseGroup.trinary_fitting_base_A(1)
trisquare = read_data.fittingBaseGroup.trinary_fitting_base_A(2)
tricubic = read_data.fittingBaseGroup.trinary_fitting_base_A(3)
train_data = np.array(df_train.iloc[:,[0,1,8,9]])
fitter1 = read_data.general_fitter("tri_thermo", train_data, [0,1,2], 3, trilinear)
fitter1.set_var_name(['T','P','x_N2'],'x_O2')
func_file = open("order1.py",'w')
func_file.write(fitter1.fit_and_write())
func_file.close()

fitter2 = read_data.general_fitter("tri_thermo", train_data, [0,1,2], 3, trisquare)
fitter2.set_var_name(['T','P','x_N2'],'x_O2')
func_file = open("order2.py",'w')
func_file.write(fitter2.fit_and_write(fitter1))
func_file.close()

fitter3 = read_data.general_fitter("tri_thermo", train_data, [0,1,2], 3, tricubic)
fitter3.set_var_name(['T','P','x_N2'],'x_O2')
func_file = open("order3.py",'w')
func_file.write(fitter3.fit_and_write(fitter2))
func_file.close()

np.savetxt("train_data.txt", train_data, fmt="%f", delimiter=",")
test_data = np.array(df_test.iloc[:,[0,1,8,9]])
np.savetxt("test_data.txt", test_data, fmt="%f", delimiter=",")

