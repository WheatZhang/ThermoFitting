#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 结论：不能使用numpy中的函数


from pyomo.environ import *
import numpy as np
model = ConcreteModel()

model.x = Var(initialize = 0)
model.y = Var(initialize=  0)

def myfunc(x,y):
    a = np.array([1,2])
    b = np.array([x,y])
    return np.dot(a,b)

def mycons(m):
    return np.abs(m.x) <= 5

model.x_con = Constraint(rule = mycons)

model.obj = Objective(rule = myfunc(model.x,model.y))



solver = SolverFactory("ipopt")
result = solver.solve(model)
print(result)