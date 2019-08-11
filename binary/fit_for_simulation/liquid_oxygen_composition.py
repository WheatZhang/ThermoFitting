#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_oxygen_composition(pressure,temperature):
	x = (pressure-100.000000)/500.000000
	y = (temperature--195.914523)/34.081421
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
	z = 0.004688+\
	    y*5.102425+\
	    y2*-8.582956+\
	    y3*5.623218+\
	    x*-6.353776+\
	    xy*18.091677+\
	    xy2*-14.713666+\
	    xy3*0.254038+\
	    x2*1.645231+\
	    x2y*-15.156516+\
	    x2y2*23.946051+\
	    x2y3*-8.012103+\
	    x3*1.373898+\
	    x3y*0.570620+\
	    x3y2*-6.053944+\
	    x3y3*3.258808
	return z*1.000000+0.000000
