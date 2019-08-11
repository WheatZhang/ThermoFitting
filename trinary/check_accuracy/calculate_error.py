import pandas as pd
import numpy as np
import read_data

csv_data = pd.read_csv("dataset_design/7__Main Tower.csv", sep=',')
name_in_df = ["P","T","x_N2","x_O2"]
nominal_value = [540,-176,0.8]
deviation = [40,4,0.2]
max_order = 5
thermo_name = "tri_thermo"
desired_error = 5e-3
filename = "optimal_order.py"
way = 'Compound'

fitter = read_data.AdaptivePolynomialFitting(thermo_name, filename)
fitter.set_data(csv_data, name_in_df)
fitter.set_range(nominal_value, deviation)
fitter.set_fitting_param(way, max_order, desired_error)
fitter.fit_and_write()

from optimal_order import tri_thermo
for i in range(1,42):
    csv_data = pd.read_csv("dataset_design/%d__Main Tower.csv"%i, sep=',')
    max_error = 0
    for j in range(csv_data.shape[0]):
        predict = tri_thermo(csv_data.loc[j,"P"],csv_data.loc[j,"T"],csv_data.loc[j,"x_N2"])
        error = abs(predict - csv_data.loc[j,"x_O2"])
        if error>max_error:
            max_error = error
    print(max_error)