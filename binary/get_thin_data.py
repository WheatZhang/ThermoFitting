#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pandas
import numpy as np
thermo_data = pandas.read_csv("data/thermo_test.txt", sep=',', header = None)
a = []
for j in range(20+1):
    for i in range(20+1):
        a.append(i*10+j*10*201)
thin_data = thermo_data.iloc[a].to_csv("data/thin_data.txt", sep=',', header = None,index=False)