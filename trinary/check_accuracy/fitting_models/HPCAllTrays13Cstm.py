def LiqO2(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*-2.20410635e+00+\
	    z*3.12486698e+00+\
	    y*2.46501503e+00+\
	    x*-4.07648305e-01
	x_O2 = output*1.09657763e-02+5.22656438e-02
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*-1.20260757e-02
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*5.04736066e-01
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*3.82634675e+00
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*-6.04516943e-01+\
	    z*1.70610194e+00+\
	    y*6.04862794e-01+\
	    x*-1.01016182e-01
	y_N2 = output*5.45041262e-03+9.60882870e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*-1.48121889e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*6.15590112e-02
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*1.03835955e+00
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*-2.13767665e+00+\
	    z*3.02239974e+00+\
	    y*2.39896656e+00+\
	    x*-3.95931583e-01
	y_O2 = output*4.88691539e-03+2.25677739e-02
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*-5.20539721e-03
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*2.18909393e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.95543312e-03
	output = \
	    1*1.64930178e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17870261e-01)/8.62837221e-03
	output = \
	    1*2.64035825e+00+\
	    z*-2.93522117e+00+\
	    y*-1.73894361e+00+\
	    x*2.93698085e-01
	vap_etlp = output*1.20981176e+01+-6.05545301e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17870261e-01)/8.62837221e-03
	output = \
	    1*9.55911812e+00
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17870261e-01)/8.62837221e-03
	output = \
	    1*-3.92833652e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17870261e-01)/8.62837221e-03
	output = \
	    1*-4.11556781e+03
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.57767906e-03
	output = \
	    1*3.55883644e+00+\
	    z*-3.63508772e+00+\
	    y*-2.63171835e+00+\
	    x*4.63448044e-01
	liq_etlp = output*1.93707873e+01+-1.09286296e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.57767906e-03
	output = \
	    1*2.41516738e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.57767906e-03
	output = \
	    1*-9.51901612e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.56380000e+02)/3.71707300e-01
	y = (T--1.77068007e+02)/5.35543333e-02
	z = (x_N2-9.17543200e-01)/8.57767906e-03
	output = \
	    1*-8.20904004e+03
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

