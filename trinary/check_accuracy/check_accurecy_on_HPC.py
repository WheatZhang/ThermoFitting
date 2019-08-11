#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pandas as pd

csv_data = pd.read_csv("HPC_data.txt", sep='\t')

fitting_items = ["x_O2","y_N2","y_O2","vap_etlp","liq_etlp"]
var_name_in_model = ["LiqO2","VapN2","VapO2","VapEtlp","LiqEtlp"]
record = []

for r in range(csv_data.shape[0]):
    place = csv_data.loc[r,'place']
    T = csv_data.loc[r,'T']
    P = csv_data.loc[r, 'P']
    x_N2 = csv_data.loc[r, 'x_N2']
    x_O2 = csv_data.loc[r, 'x_O2']
    x_Ar = csv_data.loc[r, 'x_Ar']
    y_N2 = csv_data.loc[r, 'y_N2']
    y_O2 = csv_data.loc[r, 'y_O2']
    y_Ar = csv_data.loc[r, 'y_Ar']
    vap_etlp = csv_data.loc[r, 'HV']
    liq_etlp = csv_data.loc[r, 'HL']
    if place == "Cond":
        pass
    else:
        for j in range(len(var_name_in_model)):
            func = __import__("fitting_models.HPCAllTrays%sCstm"%place+var_name_in_model[j])
            if var_name_in_model[j] == "LiqO2":
                x_O2_fit = eval("func.HPCAllTrays%sCstm"%place+var_name_in_model[j]+"."+var_name_in_model[j]+"(P,T,x_N2)")
            elif var_name_in_model[j] == "VapN2":
                y_N2_fit =eval("func.HPCAllTrays%sCstm"%place+var_name_in_model[j]+"."+var_name_in_model[j]+"(P,T,x_N2)")
            elif var_name_in_model[j] == "VapO2":
                y_O2_fit =eval("func.HPCAllTrays%sCstm"%place+var_name_in_model[j]+"."+var_name_in_model[j]+"(P,T,x_N2)")
            elif var_name_in_model[j] == "VapEtlp":
                vap_etlp_fit =eval("func.HPCAllTrays%sCstm"%place+var_name_in_model[j]+"."+var_name_in_model[j]+"(P,T,x_N2)")
            elif var_name_in_model[j] == "LiqEtlp":
                liq_etlp_fit =eval("func.HPCAllTrays%sCstm"%place+var_name_in_model[j]+"."+var_name_in_model[j]+"(P,T,x_N2)")
        x_Ar_fit = 1-x_N2-x_O2_fit
        y_Ar_fit = 1-y_N2_fit-y_O2_fit
        record.append([place,x_O2-x_O2_fit,x_Ar-x_Ar_fit,y_N2-y_N2_fit,y_O2-y_O2_fit,y_Ar-y_Ar_fit,vap_etlp-vap_etlp_fit,liq_etlp-liq_etlp_fit])

fp = open("AccuracyOnHPCReport.txt",'w')
fp.write("place\tx_O2\tx_Ar\ty_N2\ty_O2\ty_Ar\tvap_etlp\tliq_etlp\n")
for i in range(len(record)):
    fp.write(record[i][0]+"\t")
    for j in range(1,len(record[0])-1):
        fp.write("%e"%record[i][j]+"\t")
    fp.write("%e" % record[i][-1] + "\n")
fp.close()