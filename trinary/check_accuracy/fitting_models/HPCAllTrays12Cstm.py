def LiqO2(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-2.22860121e+00+\
	    z*3.12547049e+00+\
	    z2*-8.56501268e-03+\
	    y*2.49502129e+00+\
	    y*z*-5.28359691e-03+\
	    y2*-4.43449882e-03+\
	    x*-3.47764403e-01+\
	    x*z*5.94619816e-04+\
	    x*y*7.91665855e-04+\
	    x2*6.00001840e-05
	x_O2 = output*1.28356378e-02+6.64248610e-02
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*-1.20088519e-02+\
	    z*2.05331576e-05+\
	    y*2.73374672e-05+\
	    x*4.14380146e-06
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*5.03450474e-01+\
	    z*-1.06613494e-03+\
	    y*-1.78960439e-03+\
	    x*1.59743947e-04
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*3.85553358e+00+\
	    z*-2.11313427e-02+\
	    y*-6.51776600e-03+\
	    x*7.33514098e-04
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*-6.04565637e-01+\
	    z*1.69058266e+00+\
	    y*6.04951056e-01+\
	    x*-8.52202562e-02
	y_N2 = output*6.46004671e-03+9.53383215e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*-1.48107620e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*6.14357188e-02
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*1.04959971e+00
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.00892736e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-2.11744589e+00+\
	    z*2.87014020e+00+\
	    z2*-8.01983871e-03+\
	    y*2.37329598e+00+\
	    y*z*3.71735718e-03+\
	    y2*3.23397694e-03+\
	    x*-3.30327122e-01+\
	    x*z*-7.89069589e-05+\
	    x*y*-8.65777378e-04+\
	    x2*1.34837656e-04
	y_O2 = output*5.87494806e-03+2.89060618e-02
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.00892736e-02
	output = \
	    1*-5.22092163e-03+\
	    z*-1.24714873e-06+\
	    y*-1.36838774e-05+\
	    x*4.26230114e-06
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.00892736e-02
	output = \
	    1*2.19190123e-01+\
	    z*3.43323372e-04+\
	    y*5.97359800e-04+\
	    x*-7.99604651e-05
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.00892736e-02
	output = \
	    1*1.67127241e+00+\
	    z*-9.33984701e-03+\
	    y*2.16460384e-03+\
	    x*-4.59472410e-05
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01963452e-01)/9.92377184e-03
	output = \
	    1*2.62468727e+00+\
	    z*-2.87454249e+00+\
	    y*-1.74385105e+00+\
	    x*2.48518318e-01
	vap_etlp = output*1.43583418e+01+-6.05079443e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01963452e-01)/9.92377184e-03
	output = \
	    1*9.59978715e+00
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01963452e-01)/9.92377184e-03
	output = \
	    1*-3.93621419e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01963452e-01)/9.92377184e-03
	output = \
	    1*-4.15907020e+03
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*3.44141978e+00+\
	    z*-3.58573771e+00+\
	    y*-2.51911011e+00+\
	    x*3.74025914e-01
	liq_etlp = output*2.38963035e+01+-1.09435204e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*2.40453625e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*-9.46330685e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.56999512e+02)/3.71707300e-01
	y = (T--1.76911493e+02)/6.36114000e-02
	z = (x_N2-9.01482074e-01)/1.04051505e-02
	output = \
	    1*-8.23494835e+03
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

