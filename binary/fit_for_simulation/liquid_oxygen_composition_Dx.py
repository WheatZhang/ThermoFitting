#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_oxygen_composition_Dx(pressure,temperature):
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
	zdx = -6.353776+\
	    xydx*18.091677+\
	    xy2dx*-14.713666+\
	    xy3dx*0.254038+\
	    x2dx*1.645231+\
	    x2ydx*-15.156516+\
	    x2y2dx*23.946051+\
	    x2y3dx*-8.012103+\
	    x3dx*1.373898+\
	    x3ydx*0.570620+\
	    x3y2dx*-6.053944+\
	    x3y3dx*3.258808
	return zdx*0.002000
