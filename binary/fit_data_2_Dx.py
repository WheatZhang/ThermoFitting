#!/usr/bin/env python
#-*- coding:utf-8 -*-
def fit_data_2_Dx(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
	x2 = x*x
	y2 = y*y
	y3 = y*y2
	x2dx = 2*x
	x3dx = 3*x2
	xydx = y
	x2ydx = 2*x*y
	xy2dx = y2
	x3ydx = 3*x2*y
	x2y2dx = 2*x*y2
	xy3dx = y3
	x3y2dx = 3*x2*y2
	x2y3dx = 2*x*y3
	x3y3dx = 3*x2*y3
	zdx = -1.260755+\
	    xydx*-11.770346+\
	    xy2dx*10.240381+\
	    xy3dx*0.730143+\
	    x2dx*8.226725+\
	    x2ydx*0.385787+\
	    x2y2dx*-14.084938+\
	    x2y3dx*5.313749+\
	    x3dx*-10.014560+\
	    x3ydx*20.672576+\
	    x3y2dx*-13.599160+\
	    x3y3dx*3.319305
	return zdx*0.002000
