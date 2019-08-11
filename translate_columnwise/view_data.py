#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train_data = pd.read_csv('HPC_result/1__Main Tower.txt',sep='\t')
fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(20, 12),
                         tight_layout=True)
for ax ,column in zip(axes.ravel(),train_data.iloc[:,2:].columns):
    ax.scatter(train_data[column],train_data['P'],s=2, c='black')
    ax.set_ylabel('P')
    ax.set_xlabel(column)
fig.savefig("pic/corr_with_P.png", dpi=600)