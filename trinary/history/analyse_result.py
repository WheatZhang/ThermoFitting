#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np

import order1
import order2
import order3

train_data = np.loadtxt("train_data.txt", dtype=float, delimiter=",")
test_data = np.loadtxt("test_data.txt", dtype=float, delimiter=",")

predict1 = np.zeros(shape = (train_data.shape[0],1))
for i in range(train_data.shape[0]):
    predict1[i,0] = order1.tri_thermo(train_data[i,0],train_data[i,1],train_data[i,2])
error = predict1-train_data[:,3]

predict2 = np.zeros(shape = (train_data.shape[0],1))
for i in range(train_data.shape[0]):
    predict2[i,0] = order2.tri_thermo(train_data[i,0],train_data[i,1],train_data[i,2])
error = predict2-train_data[:,3]

predict3 = np.zeros(shape = (train_data.shape[0],1))
for i in range(train_data.shape[0]):
    predict3[i,0] = order3.tri_thermo(train_data[i,0],train_data[i,1],train_data[i,2])
error = predict3-train_data[:,3]

save_result = np.hstack((train_data,predict1,predict2,predict3))
np.savetxt("result1.txt", save_result, fmt="%f", delimiter=",")

predict1 = np.zeros(shape = (test_data.shape[0],1))
for i in range(test_data.shape[0]):
    predict1[i,0] = order1.tri_thermo(test_data[i,0],test_data[i,1],test_data[i,2])
error = predict1-test_data[:,3]

predict2 = np.zeros(shape = (test_data.shape[0],1))
for i in range(test_data.shape[0]):
    predict2[i,0] = order2.tri_thermo(test_data[i,0],test_data[i,1],test_data[i,2])
error = predict2-test_data[:,3]

predict3 = np.zeros(shape = (test_data.shape[0],1))
for i in range(test_data.shape[0]):
    predict3[i,0] = order3.tri_thermo(test_data[i,0],test_data[i,1],test_data[i,2])
error = predict3-test_data[:,3]

save_result = np.hstack((test_data,predict1,predict2,predict3))
np.savetxt("result2.txt", save_result, fmt="%f", delimiter=",")