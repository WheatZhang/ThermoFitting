#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pandas as pd
import read_data
import numpy as np

csv_data = pd.read_csv("filteredTriThermo.csv", sep='\t')
name_in_df = ["P","T","x_N2","x_O2"]
nominal_value = [200,-182,0.4]
deviation = [50,4,0.1]
max_order = 4
thermo_name = "tri_thermo"
desired_error = 1e-3
filename = "optimal_order.py"
way = 'Compound'

fitter = read_data.AdaptivePolynomialFitting(thermo_name, filename)
fitter.set_data(csv_data, name_in_df)
fitter.set_range(nominal_value, deviation)
fitter.set_fitting_param(way, max_order, desired_error)
fitter.fit_and_write()