#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_nitrogen_enthalpy(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--200.000000)/37.000000
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
	z = 0.000562+\
	    y*0.932428+\
	    y2*-0.079852+\
	    y3*0.197291+\
	    x*-0.001991+\
	    xy*0.194579+\
	    xy2*-0.214213+\
	    xy3*-0.179700+\
	    x2*0.010680+\
	    x2y*-0.389695+\
	    x2y2*0.792000+\
	    x2y3*-0.169544+\
	    x3*-0.005175+\
	    x3y*0.215382+\
	    x3y2*-0.521881+\
	    x3y3*0.218421
	return z*1864.455570+-13457.519087
