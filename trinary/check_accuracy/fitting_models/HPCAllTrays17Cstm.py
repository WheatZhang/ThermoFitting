def LiqO2(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77479018e+02)/2.63824000e-02
	z = (x_N2-9.58998354e-01)/4.76770079e-03
	output = \
	    1*-2.74698967e+00+\
	    z*4.32871841e+00+\
	    y*3.23471250e+00+\
	    x*-1.08289026e+00
	x_O2 = output*4.16907423e-03+1.85040299e-02
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77479018e+02)/2.63824000e-02
	z = (x_N2-9.58998354e-01)/4.76770079e-03
	output = \
	    1*-1.21457121e-02
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77479018e+02)/2.63824000e-02
	z = (x_N2-9.58998354e-01)/4.76770079e-03
	output = \
	    1*5.11164887e-01
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77479018e+02)/2.63824000e-02
	z = (x_N2-9.58998354e-01)/4.76770079e-03
	output = \
	    1*3.78520993e+00
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.58998354e-01)/4.82092963e-03
	output = \
	    1*-9.25816268e-01+\
	    z*1.84557432e+00+\
	    y*9.26132920e-01+\
	    x*-2.07709875e-01
	y_N2 = output*2.64062977e-03+9.80089625e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.58998354e-01)/4.82092963e-03
	output = \
	    1*-1.47558275e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.58998354e-01)/4.82092963e-03
	output = \
	    1*6.17981219e-02
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.58998354e-01)/4.82092963e-03
	output = \
	    1*1.01090015e+00
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.59112877e-01)/4.70640717e-03
	output = \
	    1*-4.19807372e+00+\
	    z*4.20481829e+00+\
	    y*4.78515099e+00+\
	    x*-1.06703794e+00
	y_O2 = output*1.79277344e-03+7.83372385e-03
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.59112877e-01)/4.70640717e-03
	output = \
	    1*-5.14640761e-03
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.59112877e-01)/4.70640717e-03
	output = \
	    1*2.16778145e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.59112877e-01)/4.70640717e-03
	output = \
	    1*1.60170727e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77479018e+02)/2.63824000e-02
	z = (x_N2-9.58947681e-01)/4.47703679e-03
	output = \
	    1*2.94210327e+00+\
	    z*-3.38558552e+00+\
	    y*-1.94477936e+00+\
	    x*6.64189735e-01
	vap_etlp = output*5.30005172e+00+-6.06884970e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77479018e+02)/2.63824000e-02
	z = (x_N2-9.58947681e-01)/4.47703679e-03
	output = \
	    1*9.47046224e+00
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77479018e+02)/2.63824000e-02
	z = (x_N2-9.58947681e-01)/4.47703679e-03
	output = \
	    1*-3.90693463e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77479018e+02)/2.63824000e-02
	z = (x_N2-9.58947681e-01)/4.47703679e-03
	output = \
	    1*-4.00795866e+03
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.58947681e-01)/4.87160286e-03
	output = \
	    1*6.01398979e+00+\
	    z*-5.38804252e+00+\
	    y*-5.19221427e+00+\
	    x*1.23311802e+00
	liq_etlp = output*7.35676059e+00+-1.08957576e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.58947681e-01)/4.87160286e-03
	output = \
	    1*2.44056386e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.58947681e-01)/4.87160286e-03
	output = \
	    1*-9.65236352e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.53901951e+02)/3.71707300e-01
	y = (T--1.77492209e+02)/3.95736000e-02
	z = (x_N2-9.58947681e-01)/4.87160286e-03
	output = \
	    1*-8.13665234e+03
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

