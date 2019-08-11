#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_nitrogen_enthalpy_Dy(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--200.000000)/37.000000
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
	zdy = 0.932428+\
	    yxdy*0.194579+\
	    yx2dy*-0.389695+\
	    yx3dy*0.215382+\
	    y2dy*-0.079852+\
	    y2xdy*-0.214213+\
	    y2x2dy*0.792000+\
	    y2x3dy*-0.521881+\
	    y3dy*0.197291+\
	    y3xdy*-0.179700+\
	    y3x2dy*-0.169544+\
	    y3x3dy*0.218421
	return zdy*50.390691
