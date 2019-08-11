#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_nitrogen_enthalpy_Dx(pressure,temperature):
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
	zdx = -0.001991+\
	    xydx*0.194579+\
	    xy2dx*-0.214213+\
	    xy3dx*-0.179700+\
	    x2dx*0.010680+\
	    x2ydx*-0.389695+\
	    x2y2dx*0.792000+\
	    x2y3dx*-0.169544+\
	    x3dx*-0.005175+\
	    x3ydx*0.215382+\
	    x3y2dx*-0.521881+\
	    x3y3dx*0.218421
	return zdx*3.728911
