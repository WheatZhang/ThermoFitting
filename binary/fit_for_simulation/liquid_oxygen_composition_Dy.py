#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_oxygen_composition_Dy(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
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
	zdy = 5.102425+\
	    yxdy*18.091677+\
	    yx2dy*-15.156516+\
	    yx3dy*0.570620+\
	    y2dy*-8.582956+\
	    y2xdy*-14.713666+\
	    y2x2dy*23.946051+\
	    y2x3dy*-6.053944+\
	    y3dy*5.623218+\
	    y3xdy*0.254038+\
	    y3x2dy*-8.012103+\
	    y3x3dy*3.258808
	return zdy*0.029341
