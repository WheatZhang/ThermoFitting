#!/usr/bin/env python
#-*- coding:utf-8 -*-
from scipy.optimize import minimize
import numpy as np
import pandas
import matplotlib.pyplot as plt
from sklearn import  linear_model

thermo_data = pandas.read_csv("data/thin_data.txt", sep=',', header = None)
thermo_mean = thermo_data.mean()
thermo_max = thermo_data.max()
thermo_min = thermo_data.min()
thermo_data = thermo_data.sub(thermo_min,axis = 1)
thermo_data = thermo_data.div(thermo_max-thermo_min,axis = 1)
thermo_data['p2'] = thermo_data.iloc[:,0].mul(thermo_data.iloc[:,0],axis = 0)
thermo_data['pt'] = thermo_data.iloc[:,0].mul(thermo_data.iloc[:,1],axis = 0)
thermo_data['t2'] = thermo_data.iloc[:,1].mul(thermo_data.iloc[:,1],axis = 0)
thermo_data['p3'] = thermo_data.loc[:,'p2'].mul(thermo_data.iloc[:,0],axis = 0)
thermo_data['p2t'] = thermo_data.loc[:,'pt'].mul(thermo_data.iloc[:,0],axis = 0)
thermo_data['pt2'] = thermo_data.loc[:,'pt'].mul(thermo_data.iloc[:,1],axis = 0)
thermo_data['t3'] = thermo_data.loc[:,'t2'].mul(thermo_data.iloc[:,1],axis = 0)
thermo_data['p4'] = thermo_data.loc[:,'p3'].mul(thermo_data.iloc[:,0],axis = 0)
thermo_data['p3t'] = thermo_data.loc[:,'p2t'].mul(thermo_data.iloc[:,0],axis = 0)
thermo_data['p2t2'] = thermo_data.loc[:,'p2t'].mul(thermo_data.iloc[:,1],axis = 0)
thermo_data['pt3'] = thermo_data.loc[:,'t3'].mul(thermo_data.iloc[:,0],axis = 0)
thermo_data['t4'] = thermo_data.loc[:,'t3'].mul(thermo_data.iloc[:,1],axis = 0)

linear =linear_model.LinearRegression()
# linear = SVR(kernel='linear', C=1000,max_iter=100000)
data_X = pandas.concat([thermo_data.iloc[:,0:2],thermo_data.iloc[:,9:21]],axis=1,ignore_index=True)
# data_X = thermo_data.iloc[:,0:2]
data_Y = thermo_data.iloc[:,4]
linear.fit(data_X, data_Y)
predict_Y = linear.predict(data_X)
print(np.max(np.abs(data_Y-predict_Y)))

X = np.array(data_X)
y = np.array(data_Y)
def fit(X, params):
    return X.dot(params[0:-1])+params[-1]
def cost_function(params, X, y):
    return np.max(np.abs(y - fit(X, params)))

cons = []
i=10
cons.append({'type': 'eq', 'fun': lambda x: fit(X[i*21,:], x)})
cons.append({'type': 'eq', 'fun': lambda x: fit(X[i*21+20, :], x)-1})
x0=np.append(linear.coef_,linear.intercept_)
output = minimize(cost_function, x0, args=(X, y),constraints=cons)
print(output.x)
y_hat = fit(X, output.x)
print(np.max(np.abs(y-y_hat)))

plt.figure()
items = 21
for i in range(5):
    plt.subplot(230+i+1)
    y_range = []
    for j in range(items):
        y_range.append(i*5*21+j)
    #plt.plot(range(items), predict_Y[y_range],c='r')
    plt.plot(range(items), data_Y[y_range],c='b')
    plt.plot(range(items),y_hat[y_range],c='r')
plt.show()