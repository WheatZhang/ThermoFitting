#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_oxygen_enthalpy_Dy(pressure,temperature):
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
	zdy = 0.850871+\
	    yxdy*-0.406914+\
	    yx2dy*0.981229+\
	    yx3dy*-0.587405+\
	    y2dy*0.449245+\
	    y2xdy*-0.322334+\
	    y2x2dy*-0.910912+\
	    y2x3dy*0.879245+\
	    y3dy*-0.346104+\
	    y3xdy*1.049611+\
	    y3x2dy*-0.565309+\
	    y3x3dy*-0.074628
	return zdy*60.716684
