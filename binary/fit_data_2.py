#!/usr/bin/env python
#-*- coding:utf-8 -*-
def fit_data_2(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
	x2 = x*x
	x3 = x*x2
	y2 = y*y
	y3 = y*y2
	xy = x*y
	x2y = x2*y
	xy2 = x*y2
	x3y = x3*y
	x2y2 = x2*y2
	xy3 = x*y3
	x3y2 = x3*y2
	x2y3 = x2*y3
	x3y3 = x3*y3
	z = 0.005291+\
	    y*1.054866+\
	    y2*5.248787+\
	    y3*-3.455737+\
	    x*-1.260755+\
	    xy*-11.770346+\
	    xy2*10.240381+\
	    xy3*0.730143+\
	    x2*8.226725+\
	    x2y*0.385787+\
	    x2y2*-14.084938+\
	    x2y3*5.313749+\
	    x3*-10.014560+\
	    x3y*20.672576+\
	    x3y2*-13.599160+\
	    x3y3*3.319305
	return z*1.000000+0.000000
