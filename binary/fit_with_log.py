#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pandas
import numpy as np
from sklearn import  linear_model
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from scipy.optimize import minimize

thermo_data = pandas.read_csv("data/thermo_test.txt", sep=',', header = None).iloc[0:201]
thermo_mean = thermo_data.mean()
thermo_max = thermo_data.max()
thermo_min = thermo_data.min()
thermo_data = thermo_data.sub(thermo_min,axis = 1)
thermo_data = thermo_data.div(thermo_max-thermo_min,axis = 1)
thermo_data['t2'] = thermo_data.iloc[:,1].mul(thermo_data.iloc[:,1],axis = 0)
thermo_data['t3'] = thermo_data.loc[:,'t2'].mul(thermo_data.iloc[:,1],axis = 0)
thermo_data['t4'] = thermo_data.loc[:,'t3'].mul(thermo_data.iloc[:,1],axis = 0)
thermo_data['t5'] = thermo_data.loc[:,'t4'].mul(thermo_data.iloc[:,1],axis = 0)

linear =linear_model.LinearRegression(fit_intercept=False)
# linear = SVR(kernel='linear', C=1000,max_iter=100000)
data_X = pandas.concat([thermo_data.iloc[:,1],thermo_data.iloc[:,9:11]],axis=1,ignore_index=True)
# data_X = thermo_data.iloc[:,0:2]
data_Y = thermo_data.iloc[:,4]
linear.fit(data_X, data_Y)
predict_Y = linear.predict(data_X)

plt.figure()
items = data_Y.shape[0]
plt.plot(range(items), predict_Y,c='r')
plt.plot(range(items), data_Y,c='b')
print(linear.coef_)

X = np.array(data_X)
y = np.array(data_Y)
def fit(X, params):
    return X.dot(params[:-2])+np.log(X[:,0]+params[-2])*params[-1]
def cost_function(params, X, y):
    return np.max(np.abs(y - fit(X, params)))

cons = ({'type': 'eq', 'fun': lambda x: fit(np.array([X[-1,:]]), x)-1},)
x0=np.append(linear.coef_,[1,0])
output = minimize(cost_function, x0, args=(X, y),constraints=cons)
y_hat = fit(X, output.x)
plt.figure()
plt.plot(range(items), y_hat,c='r')
plt.plot(range(items), y,c='b')
print(np.max(np.abs(y-y_hat)))
print(output.x)
plt.show()
