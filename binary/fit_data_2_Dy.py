#!/usr/bin/env python
#-*- coding:utf-8 -*-
def fit_data_2_Dy(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
	y2 = y*y
	x2 = x*x
	x3 = x*x2
	y2dy = 2*y
	y3dy = 3*y2
	yxdy = x
	y2xdy = 2*y*x
	yx2dy = x2
	y3xdy = 3*y2*x
	y2x2dy = 2*y*x2
	yx3dy = x3
	y3x2dy = 3*y2*x2
	y2x3dy = 2*y*x3
	y3x3dy = 3*y2*x3
	zdy = 1.054866+\
	    yxdy*-11.770346+\
	    yx2dy*0.385787+\
	    yx3dy*20.672576+\
	    y2dy*5.248787+\
	    y2xdy*10.240381+\
	    y2x2dy*-14.084938+\
	    y2x3dy*-13.599160+\
	    y3dy*-3.455737+\
	    y3xdy*0.730143+\
	    y3x2dy*5.313749+\
	    y3x3dy*3.319305
	return zdy*0.029341
