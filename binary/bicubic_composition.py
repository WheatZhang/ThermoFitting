#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pandas
import numpy as np
import matplotlib.pyplot as plt

thermo_data = pandas.read_csv("data/thin_data.txt", sep=',', header = None)
for i in range(21):
    for j in range(21):
        thermo_data.iloc[i*21+j,1] = j
thermo_mean = thermo_data.mean()
thermo_max = thermo_data.max()
thermo_min = thermo_data.min()
thermo_data = thermo_data.sub(thermo_min,axis = 1)
thermo_data = thermo_data.div(thermo_max-thermo_min,axis = 1)

data_X = np.array(thermo_data.iloc[:,0])
data_Y = np.array(thermo_data.iloc[:,1])
data_Z = np.array(thermo_data.iloc[:,2])

def bicubic_interpolation2(xi, yi, zi,funcname):
    func_file = open(funcname+".py", 'w')
    func_file.write("#!/usr/bin/env python\n#-*- coding:utf-8 -*-\n")
    func_file.write("def "+funcname+"(x,y):\n")
    # check sorting
    if np.any(np.diff(xi) < 0) and np.any(np.diff(yi) < 0):
        raise ValueError('data are not sorted')

    if zi.shape != (xi.size, yi.size):
        raise ValueError('zi is not set properly use np.meshgrid(xi, yi)')
    xnew = np.zeros(shape=(xi.size-1,))
    ynew = np.zeros(shape=(yi.size - 1,))
    for n, x in enumerate(xnew):
        xnew[n] = (xi[n+1]+xi[n])/2
    for n, y in enumerate(ynew):
        ynew[n] = (yi[n + 1] + yi[n]) / 2
    for n, x in enumerate(xnew):
        if n != xnew.size-1:
            if n != 0:
                func_file.write("\telif x <= " + str(xi[n + 1]) + ":\n")
            else:
                func_file.write("\tif x <= "+str(xi[n+1])+":\n")
        else:
            func_file.write("\telse:\n")
        for m, y in enumerate(ynew):
            if m != ynew.size - 1:
                if m != 0:
                    func_file.write("\t\telif y <= " + str(yi[m + 1]) + ":\n")
                else:
                    func_file.write("\t\tif y <= " + str(yi[m + 1]) + ":\n")
            else:
                func_file.write("\t\telse:\n")

            i = np.searchsorted(xi, x) - 1
            j = np.searchsorted(yi, y) - 1

            x1  = xi[i]
            x2  = xi[i+1]

            y1  = yi[j]
            y2  = yi[j+1]

            px = (x-x1)/(x2-x1)
            py = (y-y1)/(y2-y1)
            func_file.write("\t\t\tpx=(x-%f)/%f\n"% (x1,x2-x1))
            func_file.write("\t\t\tpy=(y-%f)/%f\n" % (y1, y2 - y1))
            f00 = zi[i-1, j-1]      #row0 col0 >> x0,y0
            f01 = zi[i-1, j]        #row0 col1 >> x1,y0
            f02 = zi[i-1, j+1]      #row0 col2 >> x2,y0

            f10 = zi[i, j-1]        #row1 col0 >> x0,y1
            f11 = p00 = zi[i, j]    #row1 col1 >> x1,y1
            f12 = p01 = zi[i, j+1]  #row1 col2 >> x2,y1

            f20 = zi[i+1,j-1]       #row2 col0 >> x0,y2
            f21 = p10 = zi[i+1,j]   #row2 col1 >> x1,y2
            f22 = p11 = zi[i+1,j+1] #row2 col2 >> x2,y2

            if 0 < i < xi.size-2 and 0 < j < yi.size-2:

                f03 = zi[i-1, j+2]      #row0 col3 >> x3,y0

                f13 = zi[i,j+2]         #row1 col3 >> x3,y1

                f23 = zi[i+1,j+2]       #row2 col3 >> x3,y2

                f30 = zi[i+2,j-1]       #row3 col0 >> x0,y3
                f31 = zi[i+2,j]         #row3 col1 >> x1,y3
                f32 = zi[i+2,j+1]       #row3 col2 >> x2,y3
                f33 = zi[i+2,j+2]       #row3 col3 >> x3,y3

            elif i<=0:  #小于0表示在第一个点之前。等于零表示在第一个和第二个点之间

                f03 = f02               #row0 col3 >> x3,y0

                f13 = f12               #row1 col3 >> x3,y1

                f23 = f22               #row2 col3 >> x3,y2

                f30 = zi[i+2,j-1]       #row3 col0 >> x0,y3
                f31 = zi[i+2,j]         #row3 col1 >> x1,y3
                f32 = zi[i+2,j+1]       #row3 col2 >> x2,y3
                f33 = f32               #row3 col3 >> x3,y3

            elif j<=0:

                f03 = zi[i-1, j+2]      #row0 col3 >> x3,y0

                f13 = zi[i,j+2]         #row1 col3 >> x3,y1

                f23 = zi[i+1,j+2]       #row2 col3 >> x3,y2

                f30 = f20               #row3 col0 >> x0,y3
                f31 = f21               #row3 col1 >> x1,y3
                f32 = f22               #row3 col2 >> x2,y3
                f33 = f23               #row3 col3 >> x3,y3


            elif i == xi.size-2 or j == yi.size-2:

                f03 = f02               #row0 col3 >> x3,y0

                f13 = f12               #row1 col3 >> x3,y1

                f23 = f22               #row2 col3 >> x3,y2

                f30 = f20               #row3 col0 >> x0,y3
                f31 = f21               #row3 col1 >> x1,y3
                f32 = f22               #row3 col2 >> x2,y3
                f33 = f23               #row3 col3 >> x3,y3

            Z = np.array([f00, f01, f02, f03,
                         f10, f11, f12, f13,
                         f20, f21, f22, f23,
                         f30, f31, f32, f33]).reshape(4,4).transpose()

            X = np.tile(np.array([-1, 0, 1, 2]), (4,1))
            X[0,:] = X[0,:]**3
            X[1,:] = X[1,:]**2
            X[-1,:] = 1

            Y = np.tile(np.array([-1, 0, 1, 2]), (4, 1)).transpose()
            Y[:, 0] = Y[:, 0] ** 3
            Y[:, 1] = Y[:, 1] ** 2
            Y[:, -1] = 1

            K= np.linalg.inv(Y)@Z@np.linalg.inv(X)
            px_vector = np.array([px**3, px**2, px, 1])
            py_vector = np.array([py**3, py**2, py, 1])
            func_file.write("\t\t\tpx2 = px*px\n")
            func_file.write("\t\t\tpx3 = px*px2\n")
            func_file.write("\t\t\tpy2 = py*py\n")
            func_file.write("\t\t\tpy3 = py*py2\n")
            func_file.write("\t\t\treturn ")
            flag = 0
            str_px = ["*px3","*px2","*px",""]
            str_py = ["*py3","*py2","*py",""]
            for px_v in range(4):
                for py_v in range(4):
                    if flag == 0:
                        flag = 1
                    else:
                        func_file.write("\\\n\t\t\t                +")
                    func_file.write("%f"%K[py_v,px_v]+str_py[py_v]+str_px[px_v])
            func_file.write("\n")
    func_file.close()


fit_x = []
fit_y = []
x_point = [0,5,10,15,20]
y_point = [0,5,10,15,20]
for i in range(5):
    fit_x.append(data_X[x_point[i]*21])
for i in range(5):
    fit_y.append(data_Y[y_point[i]])
fit_z = np.zeros(shape=(len(fit_x),len(fit_y)))
for i in range(5):
    for j in range(5):
        fit_z[i,j] = data_Z[x_point[i]*21+y_point[j]]
fit_x = np.array(fit_x)
fit_y = np.array(fit_y)

bicubic_interpolation2(fit_x,fit_y,fit_z,"bicubic_comp2")
import bicubic_comp2
predict_Z = np.zeros((data_X.size,))
for i in range(predict_Z.size):
    my_x = data_X[i]
    my_y = data_Y[i]
    predict_Z[i] = bicubic_comp2.bicubic_comp2(my_x, my_y)
print(np.max(np.abs(predict_Z-data_Z)))

plt.figure()
items = 21
for i in range(5):
    plt.subplot(230+i+1)
    y_range = []
    for j in range(items):
        y_range.append(i*5*21+j)
    plt.plot(range(items), predict_Z[y_range],c='r')
    plt.plot(range(items), data_Z[y_range],c='b')
plt.show()
