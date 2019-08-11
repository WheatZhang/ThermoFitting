#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
from scipy.optimize import minimize
import re

VAR_SYMBOL = ["x","y","z","w","u","v"]
class fittingBase(object):
    def __init__(self, power_coeff):
        self.power_coeff = power_coeff
        self.dimension = len(power_coeff)
        if self.dimension > 6:
            raise Exception("The dimension is too high.")
        for i in self.power_coeff:
            if i > 10:
                raise Exception("The order is too high.")

    def  __eq__(self, baseB):
        if not isinstance(baseB, fittingBase):
            return False
        if self.dimension != baseB.dimension:
            return False
        for index,item in enumerate(self.power_coeff):
            if baseB.power_coeff[index] != item:
                return False
        return True

    def evaluate(self, sample):
        if len(sample) != self.dimension:
            raise Exception("The dimension of the base is incorrect.")
        result = 1
        for i in range(self.dimension):
            for j in range(self.power_coeff[i]):
                result *= sample[i]
        return result

    def generate_str(self):
        str = ""
        first_flag = True
        for i in range(self.dimension):
            if self.power_coeff[i] == 0:
                continue
            if first_flag:
                first_flag = False
            else:
                str += "*"
            if self.power_coeff[i] == 1:
                str += VAR_SYMBOL[i]
            else:
                str += VAR_SYMBOL[i]+"%d"%self.power_coeff[i]
        if first_flag:
            return "1"
        return str

class fittingBaseGroup(object):
    def __init__(self, name, dimension):
        self.name = name
        self.bases = []
        self.dimension = dimension
        self.max_order = [0 for i in range(dimension)]

    def numberOfBases(self):
        return len(self.bases)

    def add_base(self, base):
        if base.dimension != self.dimension:
            raise Exception("The dimension of the base is incorrect.")
        for i in range(self.dimension):
            if base.power_coeff[i] > self.max_order[i]:
                self.max_order[i] = base.power_coeff[i]
        self.bases.append(base)

    def evaluate(self, sample, coeff):
        result = 0
        for index, item in enumerate(self.bases):
            result += item.evaluate(sample) * coeff[index]
        return result

    def generate_power_series(self):
        str = ""
        for i in range(self.dimension):
            str += fittingBaseGroup.generate_single_power_series(VAR_SYMBOL[i], self.max_order[i])
        return str

    def generate_expression(self, coeff):
        str = ""
        str += "\toutput = \\\n"
        n_items = len(self.bases)
        for index, item in enumerate(self.bases):
            if index != n_items-1:
                str += "\t    "+item.generate_str()+"*%.8e+\\\n"%coeff[index]
            else:
                str += "\t    "+item.generate_str()+"*%.8e\n"%coeff[index]
        return str

    def __contains__(self, e):
        for i in self.bases:
            if i == e:
                return True
        return False

    @staticmethod
    def generate_single_power_series(var_symbol, order):
        if order <= 1:
            return ""
        str = ""
        if order == 2:
            str += "\t"+var_symbol+"2 = "+var_symbol+" * "+var_symbol+"\n"
            return str
        str += "\t"+var_symbol + "2 = " + var_symbol + "*" + var_symbol+"\n"
        for i in range(3,order+1):
            str +="\tSYMBOL%d = SYMBOL%d * SYMBOL\n" %(i,i-1)
        str = str.replace("SYMBOL",var_symbol)
        return str

    @staticmethod
    def bicubic_fitting_base():
        bicubic = fittingBaseGroup('Bicubic', 2)
        for i in range(4):
            for j in range(4):
                bicubic.add_base(fittingBase([i,j]))
        return bicubic

    @staticmethod
    def binary_fitting_base_A(order):
        bicubic = fittingBaseGroup('BinaryAOrder%d'%order, 2)
        for i in range(order+1):
            for j in range(order+1):
                bicubic.add_base(fittingBase([i, j]))
        return bicubic

    @staticmethod
    def trinary_fitting_base_A(order):
        trinary = fittingBaseGroup('TrinaryAOrder%d'%order, 3)
        for i in range(order+1):
            for j in range(order+1):
                for k in range(order+1):
                    trinary.add_base(fittingBase([i, j, k]))
        return trinary

    @staticmethod
    def binary_fitting_base_B(order):
        bicubic = fittingBaseGroup('BinaryAOrder%d' % order, 2)
        for i in range(order + 1):
            for j in range(order + 1):
                if i + j > order:
                    break
                bicubic.add_base(fittingBase([i, j]))
        return bicubic

    @staticmethod
    def trinary_fitting_base_B(order):
        trinary = fittingBaseGroup('TrinaryAOrder%d' % order, 3)
        for i in range(order + 1):
            for j in range(order + 1):
                if i + j > order:
                    break
                for k in range(order + 1):
                    if i + j + k > order:
                        break
                    trinary.add_base(fittingBase([i, j, k]))
        return trinary

    @staticmethod
    def fitting_base_library(dimension, way, order):
        if way == "Individual":
            if dimension == 2:
                return fittingBaseGroup.binary_fitting_base_A(order)
            elif dimension == 3:
                return fittingBaseGroup.trinary_fitting_base_A(order)
            else:
                raise Exception("Unknown dimension for way %s."%way)
        elif way == 'Compound':
            if dimension == 2:
                return fittingBaseGroup.binary_fitting_base_B(order)
            elif dimension == 3:
                return fittingBaseGroup.trinary_fitting_base_B(order)
            else:
                raise Exception("Unknown dimension for way %s."%way)
        else:
            raise Exception("Unknown way.")

class GeneralFitter(object):
    def __init__(self, name, data=None, indep_var_index=None, dep_var_index=None, base_group=None):
        self.name = name
        if data is None:
            return
        if not isinstance(data, np.ndarray):
            raise Exception("The data for fitting process must be an ndarray.")
        self.base_group = base_group
        self.data = data
        self.dimension = len(indep_var_index)
        if self.dimension != self.base_group.dimension:
            raise Exception("The dimension of the base is incorrect.")
        self.indep_var_index =indep_var_index
        self.dep_var_index = dep_var_index

    def set_var_name(self, indep_var_name, dep_var_name):
        if self.dimension != len(indep_var_name):
            raise Exception("The dimension of the indep_var_name is incorrect.")
        self.indep_var_name = indep_var_name
        self.dep_var_name = dep_var_name

    def cost_function_OLD_VERSION(self, params, data):
        error = 0
        for n_data in range(data.shape[0]):
            error+=np.linalg.norm(data[n_data,self.dep_var_index] - \
                                  self.base_group.evaluate(data[n_data, self.indep_var_index],params))
        return error

    def fit_OLD_VERSION(self, fitterB=None):
        self.min_value = np.zeros(shape=(self.dimension+1,))
        self.max_value = np.zeros(shape=(self.dimension+1,))
        for i in range(self.dimension):
            self.min_value[i] = np.min(self.data[:, self.indep_var_index[i]])
            self.max_value[i] = np.max(self.data[:, self.indep_var_index[i]])
        self.min_value[self.dimension] = np.min(self.data[:, self.dep_var_index])
        self.max_value[self.dimension] = np.max(self.data[:, self.dep_var_index])
        data = np.zeros(shape=self.data.shape)
        for i in range(self.data.shape[0]):
            for index,item in enumerate(self.indep_var_index):
                data[i,item] = (self.data[i,item]-self.min_value[index])/(self.max_value[index]-self.min_value[index])
            data[i, self.dep_var_index] = (self.data[i, self.dep_var_index] - self.min_value[-1]) / (self.max_value[-1] - self.min_value[-1])
        if fitterB == None:
            x0 = np.zeros(shape=(self.base_group.numberOfBases(),))
        else:
            x0 = np.zeros(shape=(self.base_group.numberOfBases(),))
            for index, item in enumerate(fitterB.base_group.bases):
                for index2, item2 in enumerate(self.base_group.bases):
                    if item == item2:
                        self.coeff[item2] = fitterB.coeff[item]
                        break
        output = minimize(self.cost_function, x0, args=(data))
        self.coeff = output.x

    def cost_function(self, params, X, y):
        error = y - X.dot(params)
        return error.dot(error)

    def fit(self, fitterB=None):
        self.min_value = np.zeros(shape=(self.dimension+1,))
        self.max_value = np.zeros(shape=(self.dimension+1,))
        for i in range(self.dimension):
            self.min_value[i] = np.min(self.data[:, self.indep_var_index[i]])
            self.max_value[i] = np.max(self.data[:, self.indep_var_index[i]])
        self.min_value[self.dimension] = np.min(self.data[:, self.dep_var_index])
        self.max_value[self.dimension] = np.max(self.data[:, self.dep_var_index])
        data = np.zeros(shape=self.data.shape)
        for i in range(self.data.shape[0]):
            for index,item in enumerate(self.indep_var_index):
                if self.max_value[index] == self.min_value[index]:
                    raise Exception(self.indep_var_name[index]+" has only one value in all samples.")
                data[i,item] = (self.data[i,item]-self.min_value[index])/(self.max_value[index]-self.min_value[index])
            if self.max_value[-1] == self.min_value[-1]:
                raise Exception(self.dep_var_name+" has only one value in all samples.")
            data[i, self.dep_var_index] = (self.data[i, self.dep_var_index] - self.min_value[-1]) / (self.max_value[-1] - self.min_value[-1])
        temp = []
        for n_data in range(data.shape[0]):
            temp.append(self.base_group.bases[0].evaluate(data[n_data, self.indep_var_index]))
        data_for_fit = np.transpose([temp])
        for index, item in enumerate(self.base_group.bases):
            if index == 0:
                continue
            temp = []
            for n_data in range(data.shape[0]):
                temp.append(item.evaluate(data[n_data, self.indep_var_index]))
            data_for_fit = np.hstack((data_for_fit,np.transpose([temp])))
        if fitterB == None:
            x0 = np.zeros(shape=(self.base_group.numberOfBases(),))
        else:
            x0 = np.zeros(shape=(self.base_group.numberOfBases(),))
            for index, item in enumerate(fitterB.base_group.bases):
                for index2, item2 in enumerate(self.base_group.bases):
                    if item == item2:
                        x0[index2] = fitterB.coeff[index]
                        break
        output = minimize(self.cost_function, x0, args=(data_for_fit, data[:, self.dep_var_index]))
        self.coeff = output.x

    def evaluate(self, sample):
        if not hasattr(self, "coeff"):
            raise Exception("Must do regression first.")
        data = []
        for index,item in enumerate(sample):
            data.append((item - self.min_value[index]) / (self.max_value[index] - self.min_value[index]))
        raw_output = self.base_group.evaluate(data, self.coeff)
        return raw_output * (self.max_value[-1] - self.min_value[-1]) + self.min_value[-1]

    def generate_result(self):
        if not hasattr(self, "coeff"):
            raise Exception("Must do regression first.")
        str = ""
        str += "def " + self.name + "("
        first_flag = True
        for i in range(self.dimension):
            if first_flag:
                str += self.indep_var_name[i]
                first_flag = False
            else:
                str += ',' + self.indep_var_name[i]
        str += "):\n"
        for i in range(self.dimension):
            str += "\t" + VAR_SYMBOL[i] + " = (" + self.indep_var_name[i] + "-%.8e)/%.8e\n" % (
            self.min_value[i], self.max_value[i] - self.min_value[i])
        str += self.base_group.generate_power_series()
        str += self.base_group.generate_expression(self.coeff)
        str += "\t" + self.dep_var_name + " = output*%.8e+%.8e\n" % (
        self.max_value[-1] - self.min_value[-1], self.min_value[-1])
        str += "\treturn " + self.dep_var_name+"\n\n"
        return str

    def get_derivative_fitter(self, partial_var_index):
        if partial_var_index>= self.dimension:
            raise Exception("The partial derivative variable index beyond the scope.")
        derivative_fitter = GeneralFitter(name = self.name+"_p"+self.indep_var_name[partial_var_index])
        derivative_fitter.indep_var_name = self.indep_var_name
        derivative_fitter.dep_var_name = self.dep_var_name
        derivative_fitter.dimension = self.dimension
        derivative_fitter.base_group = fittingBaseGroup("DerivativeFitterBase",self.dimension)
        derivative_fitter.coeff = []
        derivative_fitter.max_value = self.max_value.copy()
        derivative_fitter.min_value = self.min_value.copy()
        derivative_fitter.max_value[self.dimension] = 1
        derivative_fitter.min_value[self.dimension] = 0
        for i in range(len(self.base_group.bases)):
            if self.base_group.bases[i].power_coeff[partial_var_index] > 0:
                power_coeff = []
                for index, item in enumerate(self.base_group.bases[i].power_coeff):
                    if index == partial_var_index:
                        power_coeff.append(item-1)
                    else:
                        power_coeff.append(item)
                derivative_fitter.base_group.add_base(fittingBase(power_coeff))
                derivative_fitter.coeff.append(self.base_group.bases[i].power_coeff[partial_var_index]*self.coeff[i])
        for i in range(len(derivative_fitter.coeff)):
            derivative_fitter.coeff[i] *= (self.max_value[self.dimension]-self.min_value[self.dimension])/\
                                       (self.max_value[partial_var_index]-self.min_value[partial_var_index])
        return derivative_fitter

    def fit_and_write(self, fitterB=None):
        self.fit(fitterB)
        return self.generate_result()

class AdaptivePolynomialFitting(object):
    def __init__(self, thermo_name):
        self.thermo_name = thermo_name
        # self.filename = filename

    def set_data(self, df, names):
        self.csv_data = df
        self.name_in_df = names
        self.indep_var_names = names[:-1]
        self.dep_var_name = names[-1]
        self.dimension = len(self.indep_var_names)

    def set_range(self, nominal_value, deviation):
        self.nominal_value = nominal_value
        self.deviation = deviation

    def set_fitting_param(self, way, max_order, desired_error):
        self.max_order = max_order
        self.way = way
        self.target_error = desired_error

    def generate_derivative_func(self, indexOrName):
        if not hasattr(self, "last_fitter"):
            raise Exception("The fitting should be done first.")
        if isinstance(indexOrName, str):
            index = self.indep_var_names.index(indexOrName)
        else:
            index = indexOrName
        der_fitter = self.last_fitter.get_derivative_fitter(index)
        # func_file = open(re.match(r'(.+?)\.',self.filename).group(1)+"_p"+self.indep_var_names[index]+".py", 'w')
        # func_file.write(der_fitter.generate_result())
        # func_file.close()
        return der_fitter.generate_result()

    def generate_funcion(self):
        def indicator_func(df):
            result = (df[self.indep_var_names[0]]>(self.nominal_value[0]-self.deviation[0])) & (df[self.indep_var_names[0]]<(self.nominal_value[0]+self.deviation[0]))
            if self.dimension == 1:
                return result
            for i in range(1,len(self.indep_var_names)):
                result = result & (df[self.indep_var_names[i]]>(self.nominal_value[i]-self.deviation[i])) & (df[self.indep_var_names[i]]<(self.nominal_value[i]+self.deviation[i]))
            return result

        selected_data = self.csv_data[indicator_func(self.csv_data)]
        selected_data = selected_data.sample(frac=1.0)  # 全部打乱
        cut_idx = int(round(0.5 * selected_data.shape[0]))
        df_test, df_train = selected_data.iloc[:cut_idx], selected_data.iloc[cut_idx:]
        if selected_data.shape[0] < self.max_order*self.dimension:
            raise Exception("Too few samples.")
        # print(selected_data.shape[0])
        # print(df_test.shape[0])
        train_data = np.array(df_train.loc[:,self.name_in_df])
        test_data = np.array(df_test.loc[:,self.name_in_df])
        indep_var_index = []
        for i in range(len(self.indep_var_names)):
            indep_var_index.append(i)
        dep_var_index = self.dimension

        last_base = fittingBaseGroup.fitting_base_library(self.dimension, self.way, 1)
        last_fitter = GeneralFitter(self.thermo_name, train_data, indep_var_index, dep_var_index, last_base)
        last_fitter.set_var_name(self.indep_var_names,self.dep_var_name)
        last_fitter.fit()
        last_predict = np.zeros(shape = (test_data.shape[0],1))
        for i in range(test_data.shape[0]):
            last_predict[i,0] = last_fitter.evaluate(test_data[i,:-1])
        last_error = last_predict-test_data[:,[-1]]
        max_last_error = max(abs(last_error))
        flag = False
        order = 1
        if max_last_error>self.target_error:
            if self.max_order > 1:
                for i in range(1,self.max_order+1):
                    new_base = fittingBaseGroup.fitting_base_library(self.dimension, self.way, i)
                    new_fitter = GeneralFitter(self.thermo_name, train_data, indep_var_index, dep_var_index, new_base)
                    new_fitter.set_var_name(self.indep_var_names, self.dep_var_name)
                    new_fitter.fit(last_fitter)
                    new_predict = np.zeros(shape=(test_data.shape[0], 1))
                    for j in range(test_data.shape[0]):
                        new_predict[j, 0] = new_fitter.evaluate(test_data[j, :-1])
                    new_error = new_predict - test_data[:, [-1]]
                    max_new_error = max(abs(new_error))
                    if max_new_error > max_last_error:
                        raise Exception("Mission impossible, the data should be more localized.")
                    else:
                        last_fitter = new_fitter
                        max_last_error = max_new_error
                        if max_last_error < self.target_error:
                            flag = True
                            order = i
                            break
            else:
                raise Exception("Mission impossible, the order should be bigger.")
        else:
            flag = True
        if flag == False:
            raise Exception("Mission impossible, the order should be bigger.")

        print("The max error on test dataset is %e."%max_last_error)
        # func_file = open(self.filename,'w')
        # func_file.write(last_fitter.generate_result())
        # func_file.close()
        self.current_max_error = max_last_error
        self.order = order
        self.last_fitter = last_fitter
        return last_fitter.generate_result()