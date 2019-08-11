#!/usr/bin/env python
#-*- coding:utf-8 -*-
def vapor_oxygen_composition(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
	x2 = x*x
	x3 = x*x2
	x4 = x*x3
	y2 = y*y
	y3 = y*y2
	y4 = y*y3
	xy = x*y
	x2y = x2*y
	xy2 = x*y2
	x3y = x3*y
	x2y2 = x2*y2
	xy3 = x*y3
	z = 0.001903+\
	    x*-1.624830+\
	    y*1.314065+\
	    x2*5.190200+\
	    xy*-6.236612+\
	    y2*3.111479+\
	    x3*-8.037417+\
	    x2y*10.640503+\
	    xy2*-4.370953+\
	    y3*0.463780+\
	    x4*4.109210+\
	    x3y*-6.167151+\
	    x2y2*3.989928+\
	    xy3*-2.368203+\
	    y4*0.981991
	return z*1.000000+0.000000
