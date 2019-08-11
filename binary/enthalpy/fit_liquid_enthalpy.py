#!/usr/bin/env python
#-*- coding:utf-8 -*-
from scipy.optimize import minimize
import numpy as np
import pandas
import csv

def create_cubic_polyfit(x,y,z,funcname):
    func_file = open(funcname+".py", 'w')
    func_file.write("#!/usr/bin/env python\n#-*- coding:utf-8 -*-\n")
    func_file.write("def "+funcname+"(crude_x,crude_y):\n")
    def fit(x,y, params):
        z = np.zeros(shape=x.shape)
        for i in range(z.size):
            xv=np.array([1,x[i],x[i]*x[i],x[i]*x[i]*x[i]])
            yv = np.array([1, y[i], y[i] * y[i], y[i] * y[i] * y[i]])
            for j in range(4):
                for k in range(4):
                    z[i]+=xv[j]*yv[k]*params[j*4+k]
        return z
    def cost_function(params, x, y, z):
        return np.linalg.norm(z - fit(x,y, params))
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)
    z_min = np.min(z)
    z_max = np.max(z)
    x = (x - x_min) / (x_max - x_min)
    y = (y - y_min) / (y_max - y_min)
    z = (z - z_min) / (z_max - z_min)
    func_file.write("\tx = (crude_x-%f)/%f\n"%(x_min,x_max-x_min))
    func_file.write("\ty = (crude_y-%f)/%f\n" % (y_min, y_max - y_min))
    func_file.write("\tx2 = x*x\n")
    func_file.write("\tx3 = x*x2\n")
    func_file.write("\ty2 = y*y\n")
    func_file.write("\ty3 = y*y2\n")
    func_file.write("\txy = x*y\n")
    func_file.write("\tx2y = x2*y\n")
    func_file.write("\txy2 = x*y2\n")
    func_file.write("\tx3y = x3*y\n")
    func_file.write("\tx2y2 = x2*y2\n")
    func_file.write("\txy3 = x*y3\n")
    func_file.write("\tx3y2 = x3*y2\n")
    func_file.write("\tx2y3 = x2*y3\n")
    func_file.write("\tx3y3 = x3*y3\n")
    x0 = np.zeros(shape=(16,))
    output = minimize(cost_function, x0, args=(x, y, z))
    func_file.write("\tz = %f+\\\n" % output.x[0])
    func_file.write("\t    y*%f+\\\n" % output.x[1])
    func_file.write("\t    y2*%f+\\\n" % output.x[2])
    func_file.write("\t    y3*%f+\\\n" % output.x[3])
    func_file.write("\t    x*%f+\\\n" % output.x[4])
    func_file.write("\t    xy*%f+\\\n" % output.x[5])
    func_file.write("\t    xy2*%f+\\\n" % output.x[6])
    func_file.write("\t    xy3*%f+\\\n" % output.x[7])
    func_file.write("\t    x2*%f+\\\n" % output.x[8])
    func_file.write("\t    x2y*%f+\\\n" % output.x[9])
    func_file.write("\t    x2y2*%f+\\\n" % output.x[10])
    func_file.write("\t    x2y3*%f+\\\n" % output.x[11])
    func_file.write("\t    x3*%f+\\\n" % output.x[12])
    func_file.write("\t    x3y*%f+\\\n" % output.x[13])
    func_file.write("\t    x3y2*%f+\\\n" % output.x[14])
    func_file.write("\t    x3y3*%f\n" % output.x[15])
    func_file.write("\treturn z*%f+%f\n" % (z_max - z_min, z_min))
    func_file.close()
    print(output.x)

def create_4th_polyfit(x,y,z,funcname):
    func_file = open(funcname+".py", 'w')
    func_file.write("#!/usr/bin/env python\n#-*- coding:utf-8 -*-\n")
    func_file.write("def "+funcname+"(crude_x,crude_y):\n")
    def fit(x,y, params):
        z = np.zeros(shape=x.shape)
        for i in range(z.shape[0]):
            z[i]=np.array([1,x[i],y[i],\
                           x[i]*x[i],x[i]*y[i],y[i]*y[i],\
                           x[i]*x[i]*x[i],x[i]*x[i]*y[i],x[i]*y[i]*y[i],y[i]*y[i]*y[i],\
                           x[i]*x[i]*x[i]*x[i],x[i]*x[i]*x[i]*y[i],x[i]*x[i]*y[i]*y[i],x[i]*y[i]*y[i]*y[i],y[i]*y[i]*y[i]*y[i]]).dot(params)
        return z
    def cost_function(params, x, y, z):
        return np.linalg.norm(z - fit(x,y, params))
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)
    z_min = np.min(z)
    z_max = np.max(z)
    x = (x - x_min) / (x_max - x_min)
    y = (y - y_min) / (y_max - y_min)
    z = (z - z_min) / (z_max - z_min)
    func_file.write("\tx = (crude_x-%f)/%f\n"%(x_min,x_max-x_min))
    func_file.write("\ty = (crude_y-%f)/%f\n" % (y_min, y_max - y_min))
    func_file.write("\tx2 = x*x\n")
    func_file.write("\tx3 = x*x2\n")
    func_file.write("\tx4 = x*x3\n")
    func_file.write("\ty2 = y*y\n")
    func_file.write("\ty3 = y*y2\n")
    func_file.write("\ty4 = y*y3\n")
    func_file.write("\txy = x*y\n")
    func_file.write("\tx2y = x2*y\n")
    func_file.write("\txy2 = x*y2\n")
    func_file.write("\tx3y = x3*y\n")
    func_file.write("\tx2y2 = x2*y2\n")
    func_file.write("\txy3 = x*y3\n")
    x0 = np.zeros(shape=(15,))
    output = minimize(cost_function, x0, args=(x, y, z))
    func_file.write("\tz = %f+\\\n" % output.x[0])
    func_file.write("\t    x*%f+\\\n" % output.x[1])
    func_file.write("\t    y*%f+\\\n" % output.x[2])
    func_file.write("\t    x2*%f+\\\n" % output.x[3])
    func_file.write("\t    xy*%f+\\\n" % output.x[4])
    func_file.write("\t    y2*%f+\\\n" % output.x[5])
    func_file.write("\t    x3*%f+\\\n" % output.x[6])
    func_file.write("\t    x2y*%f+\\\n" % output.x[7])
    func_file.write("\t    xy2*%f+\\\n" % output.x[8])
    func_file.write("\t    y3*%f+\\\n" % output.x[9])
    func_file.write("\t    x4*%f+\\\n" % output.x[10])
    func_file.write("\t    x3y*%f+\\\n" % output.x[11])
    func_file.write("\t    x2y2*%f+\\\n" % output.x[12])
    func_file.write("\t    xy3*%f+\\\n" % output.x[13])
    func_file.write("\t    y4*%f\n" % output.x[14])
    func_file.write("\treturn z*%f+%f\n" % (z_max - z_min, z_min))
    func_file.close()
    print(output.x)

thermo_liquid = pandas.read_csv("data/thin_enthalpy_liquid.csv", sep=',')
x = np.array(thermo_liquid.loc[:,'pressure'])
y = np.array(thermo_liquid.loc[:,'temperature'])
z1 = np.array(thermo_liquid.loc[:,'nitrogen'])
z2 = np.array(thermo_liquid.loc[:,'oxygen'])

create_cubic_polyfit(x,y,z1,"liquid_nitrogen")
create_cubic_polyfit(x,y,z2,"liquid_oxygen")
import liquid_nitrogen
z_hat = np.zeros(shape = z1.shape)
for i in range(z1.size):
    z_hat[i] = liquid_nitrogen.liquid_nitrogen(x[i],y[i])
print(np.max(np.abs(z1-z_hat)))
errFile1 = open('error/csvFile1.csv','w', newline='')
writer = csv.writer(errFile1)
for i in range(z_hat.size):
    writer.writerow([z1[i], z_hat[i]])
errFile1.close()

import liquid_oxygen
z_hat = np.zeros(shape = z2.shape)
for i in range(z2.size):
    z_hat[i] = liquid_oxygen.liquid_oxygen(x[i],y[i])
print(np.max(np.abs(z2-z_hat)))
errFile2 = open('error/csvFile2.csv','w', newline='')
writer = csv.writer(errFile2)
for i in range(z_hat.size):
    writer.writerow([z2[i], z_hat[i]] )
errFile2.close()