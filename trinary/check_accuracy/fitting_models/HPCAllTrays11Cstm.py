def LiqO2(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.83309743e-01)/1.13402752e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.93407626e+00+\
	    z*2.72104494e+00+\
	    z2*-1.90454549e-03+\
	    y*2.31695494e+00+\
	    y*z*3.73529135e-03+\
	    y2*-1.59398857e-03+\
	    x*-2.75288526e-01+\
	    x*z*-7.20731247e-04+\
	    x*y*-9.72298748e-05+\
	    x2*1.36368709e-04
	x_O2 = output*1.60903831e-02+8.37276882e-02
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.83309743e-01)/1.13402752e-02
	output = \
	    1*-1.19166286e-02+\
	    z*-3.11988542e-05+\
	    y*-4.20886523e-06+\
	    x*1.18061968e-05
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.83309743e-01)/1.13402752e-02
	output = \
	    1*4.98793079e-01+\
	    z*8.04131942e-04+\
	    y*-6.86306370e-04+\
	    x*-2.09316063e-05
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.83309743e-01)/1.13402752e-02
	output = \
	    1*3.86081067e+00+\
	    z*-5.40460722e-03+\
	    y*5.29989509e-03+\
	    x*-1.02262438e-03
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82992808e-01)/1.16572095e-02
	output = \
	    1*-5.93483142e-01+\
	    z*1.66907422e+00+\
	    y*6.18613327e-01+\
	    x*-7.48306524e-02
	y_N2 = output*7.44297580e-03+9.44651506e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82992808e-01)/1.16572095e-02
	output = \
	    1*-1.49839063e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82992808e-01)/1.16572095e-02
	output = \
	    1*6.16030657e-02
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82992808e-01)/1.16572095e-02
	output = \
	    1*1.06568206e+00
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.83248703e-01)/1.08521399e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.90030528e+00+\
	    z*2.54621111e+00+\
	    z2*-8.19483606e-03+\
	    y*2.27811846e+00+\
	    y*z*3.09962611e-03+\
	    y2*3.24883020e-03+\
	    x*-2.70240924e-01+\
	    x*z*4.20939209e-05+\
	    x*y*-7.24248810e-04+\
	    x2*9.61817514e-05
	y_O2 = output*7.22197444e-03+3.66996241e-02
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.83248703e-01)/1.08521399e-02
	output = \
	    1*-5.25056421e-03+\
	    z*8.17851092e-07+\
	    y*-1.40715730e-05+\
	    x*3.73746843e-06
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.83248703e-01)/1.08521399e-02
	output = \
	    1*2.20124659e-01+\
	    z*2.99503364e-04+\
	    y*6.27840610e-04+\
	    x*-6.99810066e-05
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.83248703e-01)/1.08521399e-02
	output = \
	    1*1.69447425e+00+\
	    z*-1.09071385e-02+\
	    y*2.06276557e-03+\
	    x*2.80130209e-05
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82992808e-01)/1.16572095e-02
	output = \
	    1*2.64393832e+00+\
	    z*-2.85386116e+00+\
	    y*-1.71441283e+00+\
	    x*2.08005513e-01
	vap_etlp = output*1.72093674e+01+-6.04549132e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82992808e-01)/1.16572095e-02
	output = \
	    1*9.63027441e+00
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82992808e-01)/1.16572095e-02
	output = \
	    1*-3.94745113e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82992808e-01)/1.16572095e-02
	output = \
	    1*-4.21311339e+03
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82675867e-01)/1.19741504e-02
	output = \
	    1*3.34295612e+00+\
	    z*-3.43472329e+00+\
	    y*-2.43622502e+00+\
	    x*3.08687076e-01
	liq_etlp = output*2.88295262e+01+-1.09612220e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82675867e-01)/1.19741504e-02
	output = \
	    1*2.39416933e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82675867e-01)/1.19741504e-02
	output = \
	    1*-9.39704597e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.57619024e+02)/3.71707300e-01
	y = (T--1.76727421e+02)/7.47418000e-02
	z = (x_N2-8.82675867e-01)/1.19741504e-02
	output = \
	    1*-8.26960091e+03
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

