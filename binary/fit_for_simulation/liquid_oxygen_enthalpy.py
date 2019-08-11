#!/usr/bin/env python
#-*- coding:utf-8 -*-
def liquid_oxygen_enthalpy(pressure,temperature):
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
	z = -0.001162+\
	    y*0.850871+\
	    y2*0.449245+\
	    y3*-0.346104+\
	    x*0.022997+\
	    xy*-0.406914+\
	    xy2*-0.322334+\
	    xy3*1.049611+\
	    x2*-0.037320+\
	    x2y*0.981229+\
	    x2y2*-0.910912+\
	    x2y3*-0.565309+\
	    x3*0.020327+\
	    x3y*-0.587405+\
	    x3y2*0.879245+\
	    x3y3*-0.074628
	return z*2246.517325+-12132.703363
