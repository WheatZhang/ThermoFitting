#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import read_data

fitting_items = ["x_O2","y_N2","y_O2","vap_etlp","liq_etlp"] #,"vap_rho","liq_rho"
var_name_in_model = ["LiqO2","VapN2","VapO2","VapEtlp","LiqEtlp"] #,"vap_rho","liq_rho"
desired_error = [1e-5,1e-5,1e-5,1e-1,1e-1]
max_error = [1e-3,1e-3,1e-3,10,10]
max_order = 5
way = 'Compound'
record = []

for i in range(1,42+1):
    for j in range(len(fitting_items)):
        csv_data = pd.read_csv("dataset_design/%d__Main Tower.csv"%i, sep=',')
        name_in_df = ["P","T","x_N2",fitting_items[j]]
        nominal_value = [540,-176,0.8]
        deviation = [100,20,1]
        thermo_name = var_name_in_model[j]
        filename = "fitting_models/HPCAllTrays%dCstm"%i+var_name_in_model[j]+".py"
        fitter = read_data.AdaptivePolynomialFitting(thermo_name, filename)
        fitter.set_data(csv_data, name_in_df)
        fitter.set_range(nominal_value, deviation)
        fitter.set_fitting_param(way, max_order, desired_error[j])
        try:
            fitter.fit_and_write()
        except Exception:
            print(filename)
            fitter.target_error = max_error[j]
            fitter.fit_and_write()
        fitter.write_derivative_func("P")
        fitter.write_derivative_func("T")
        fitter.write_derivative_func("x_N2")
        record.append([filename,fitter.current_max_error,fitter.order])

for j in range(len(fitting_items)):
    csv_data = pd.read_csv("dataset_design/Condenser.csv", sep=',')
    name_in_df = ["P","T","x_N2",fitting_items[j]]
    nominal_value = [540,-176,0.8]
    deviation = [100,20,1]
    thermo_name = var_name_in_model[j]
    if fitting_items[j] == "x_O2":
        filename = "fitting_models/HPCCondSelfCstm" + var_name_in_model[j] + ".py"
    elif fitting_items[j] == "liq_etlp":
        filename = "fitting_models/HPCCondOutletCstm"+var_name_in_model[j]+".py"
    else:
        continue
    fitter = read_data.AdaptivePolynomialFitting(thermo_name, filename)
    fitter.set_data(csv_data, name_in_df)
    fitter.set_range(nominal_value, deviation)
    fitter.set_fitting_param(way, max_order, desired_error[j])
    try:
        fitter.fit_and_write()
    except Exception:
        fitter.target_error = max_error[j]
        fitter.fit_and_write()
    fitter.write_derivative_func("P")
    fitter.write_derivative_func("T")
    fitter.write_derivative_func("x_N2")
    record.append([filename, fitter.current_max_error, fitter.order])

for j in range(len(fitting_items)):
    csv_data = pd.read_csv("dataset_design/1__Main Tower.csv", sep=',')
    name_in_df = ["P","T","x_N2",fitting_items[j]]
    nominal_value = [540,-176,0.8]
    deviation = [100,20,1]
    thermo_name = var_name_in_model[j]
    filename = "fitting_models/HPCFeed1SelfCstm"+var_name_in_model[j]+".py"
    fitter = read_data.AdaptivePolynomialFitting(thermo_name, filename)
    fitter.set_data(csv_data, name_in_df)
    fitter.set_range(nominal_value, deviation)
    fitter.set_fitting_param(way, max_order, desired_error[j])
    try:
        fitter.fit_and_write()
    except Exception:
        fitter.target_error = max_error[j]
        fitter.fit_and_write()
    fitter.write_derivative_func("P")
    fitter.write_derivative_func("T")
    fitter.write_derivative_func("x_N2")
    record.append([filename, fitter.current_max_error, fitter.order])

for j in range(len(fitting_items)):
    csv_data = pd.read_csv("dataset_design/4__Main Tower.csv", sep=',')
    name_in_df = ["P","T","x_N2",fitting_items[j]]
    nominal_value = [540,-176,0.8]
    deviation = [100,20,1]
    thermo_name = var_name_in_model[j]
    filename = "fitting_models/HPCFeed2SelfCstm"+var_name_in_model[j]+".py"
    fitter = read_data.AdaptivePolynomialFitting(thermo_name, filename)
    fitter.set_data(csv_data, name_in_df)
    fitter.set_range(nominal_value, deviation)
    fitter.set_fitting_param(way, max_order, desired_error[j])
    try:
        fitter.fit_and_write()
    except Exception:
        fitter.target_error = max_error[j]
        fitter.fit_and_write()
    fitter.write_derivative_func("P")
    fitter.write_derivative_func("T")
    fitter.write_derivative_func("x_N2")
    record.append([filename, fitter.current_max_error, fitter.order])

for j in range(len(fitting_items)):
    csv_data = pd.read_csv("dataset_design/1__Main Tower.csv", sep=',')
    name_in_df = ["P","T","x_N2",fitting_items[j]]
    nominal_value = [540,-176,0.8]
    deviation = [100,20,1]
    thermo_name = var_name_in_model[j]
    filename = "fitting_models/HPCSumpHdlpCstm"+var_name_in_model[j]+".py"
    fitter = read_data.AdaptivePolynomialFitting(thermo_name, filename)
    fitter.set_data(csv_data, name_in_df)
    fitter.set_range(nominal_value, deviation)
    fitter.set_fitting_param(way, max_order, desired_error[j])
    try:
        fitter.fit_and_write()
    except Exception:
        fitter.target_error = max_error[j]
        fitter.fit_and_write()
    fitter.write_derivative_func("P")
    fitter.write_derivative_func("T")
    fitter.write_derivative_func("x_N2")
    record.append([filename, fitter.current_max_error, fitter.order])

fp = open("FittingReport.csv",'w')
fp.write("Filename\tMaxTestError\tOrder\n")
for i in range(len(record)):
   fp.write(record[i][0]+"\t")
   fp.write("%e"%record[i][1]+"\t")
   fp.write("%d"%record[i][2]+'\n')
fp.close()