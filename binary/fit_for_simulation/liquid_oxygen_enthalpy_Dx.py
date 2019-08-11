#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_oxygen_enthalpy_Dx(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--200.000000)/37.000000
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
	zdx = 0.022997+\
	    xydx*-0.406914+\
	    xy2dx*-0.322334+\
	    xy3dx*1.049611+\
	    x2dx*-0.037320+\
	    x2ydx*0.981229+\
	    x2y2dx*-0.910912+\
	    x2y3dx*-0.565309+\
	    x3dx*0.020327+\
	    x3ydx*-0.587405+\
	    x3y2dx*0.879245+\
	    x3y3dx*-0.074628
	return zdx*4.493035
