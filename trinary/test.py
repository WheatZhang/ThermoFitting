#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
from scipy.optimize import minimize,leastsq
test_data = np.array([[1,2,3],[2,3,4],[3,4,5]])
# np.savetxt("result.txt", save_result, fmt="%f", delimiter=",")
def fit(X, params):
    return X.dot(params)
def cost_function(params, X, y):
    return np.max(np.abs(y - fit(X, params)))
def error(params, X, y):
    return y - fit(X, params)
x0=np.array([1,2])
# output = minimize(cost_function, x0, args=(save_result[:,:-1],save_result[:,-1]))
output = leastsq(error,x0,args=(test_data[:,:-1],test_data[:,-1]))
print(output)

# a=np.array([1,2,3])
# b=np.array([[1],[2],[3]])
# print(a.dot(b))
# print(a.dot(a))

a = np.array([])
b = np.array([[1,2,3]])
print(np.hstack((np.transpose(b),np.transpose(b))))