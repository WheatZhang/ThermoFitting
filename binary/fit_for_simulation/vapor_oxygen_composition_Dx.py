#!/usr/bin/env python
#-*- coding:utf-8 -*-
def vapor_oxygen_composition_Dx(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
	x2 = x*x
	x3 = x*x2
	y2 = y*y
	y3 = y*y2
	x2dx = 2*x
	x3dx = 3*x2
	x4dx = 4*x3
	xydx = y
	x2ydx = 2*x*y
	xy2dx = y2
	x3ydx = 3*x2*y
	x2y2dx = 2*x*y2
	xy3dx = y3
	zdx = -1.624830+\
	    x2dx*5.190200+\
	    xydx*-6.236612+\
	    x3dx*-8.037417+\
	    x2ydx*10.640503+\
	    xy2dx*-4.370953+\
	    x4dx*4.109210+\
	    x3ydx*-6.167151+\
	    x2y2dx*3.989928+\
	    xy3dx*-2.368203
	return zdx*0.002000
