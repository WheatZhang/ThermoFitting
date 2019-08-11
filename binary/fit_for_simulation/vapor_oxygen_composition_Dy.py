#!/usr/bin/env python
#-*- coding:utf-8 -*-
def vapor_oxygen_composition_Dy(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
	y2 = y*y
	y3 = y*y2
	x2 = x*x
	x3 = x*x2
	y2dy = 2*y
	y3dy = 3*y2
	y4dy = 4*y3
	yxdy = x
	y2xdy = 2*y*x
	yx2dy = x2
	y3xdy = 3*y2*x
	y2x2dy = 2*y*x2
	yx3dy = x3
	zdy = 1.314065+\
	    y2dy*3.111479+\
	    yxdy*-6.236612+\
	    y3dy*0.463780+\
	    y2xdy*-4.370953+\
	    yx2dy*10.640503+\
	    y4dy*0.981991+\
	    y3xdy*-2.368203+\
	    y2x2dy*3.989928+\
	    yx3dy*-6.167151
	return zdy*0.029341
