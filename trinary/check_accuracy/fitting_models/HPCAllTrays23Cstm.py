def LiqO2(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82420040e-01)/2.42754430e-03
	output = \
	    1*-8.92786809e+00+\
	    z*9.25967266e+00+\
	    y*9.45204621e+00+\
	    x*-4.61928755e+00
	x_O2 = output*9.86599697e-04+3.47431560e-03
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82420040e-01)/2.42754430e-03
	output = \
	    1*-1.22606859e-02
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82420040e-01)/2.42754430e-03
	output = \
	    1*5.15132157e-01
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82420040e-01)/2.42754430e-03
	output = \
	    1*3.76330526e+00
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.46537712e-03
	output = \
	    1*-8.46636832e-01+\
	    z*1.84684346e+00+\
	    y*8.46759524e-01+\
	    x*-4.14623950e-01
	y_N2 = output*1.33468449e-03+9.90949011e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.46537712e-03
	output = \
	    1*-1.48878433e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.46537712e-03
	output = \
	    1*6.24295998e-02
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.46537712e-03
	output = \
	    1*9.99828098e-01
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.43325332e-03
	output = \
	    1*-8.61607551e+00+\
	    z*8.91633329e+00+\
	    y*9.08372711e+00+\
	    x*-4.43863240e+00
	y_O2 = output*4.29662521e-04+1.43747315e-03
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.43325332e-03
	output = \
	    1*-5.13068609e-03
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.43325332e-03
	output = \
	    1*2.15597340e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.43325332e-03
	output = \
	    1*1.57444118e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.43325332e-03
	output = \
	    1*3.76942458e+00+\
	    z*-3.76978292e+00+\
	    y*-2.76958476e+00+\
	    x*1.38045705e+00
	vap_etlp = output*2.55329684e+00+-6.08031871e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.43325332e-03
	output = \
	    1*9.48250322e+00
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.43325332e-03
	output = \
	    1*-3.90631999e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82399475e-01)/2.43325332e-03
	output = \
	    1*-3.95576355e+03
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82420040e-01)/2.44481265e-03
	output = \
	    1*8.41296250e+00+\
	    z*-8.41375688e+00+\
	    y*-7.48637982e+00+\
	    x*3.89231368e+00
	liq_etlp = output*2.35503069e+00+-1.08897073e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82420040e-01)/2.44481265e-03
	output = \
	    1*2.46605749e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82420040e-01)/2.44481265e-03
	output = \
	    1*-9.73913254e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.50184878e+02)/3.71707400e-01
	y = (T--1.77763832e+02)/1.81029000e-02
	z = (x_N2-9.82420040e-01)/2.44481265e-03
	output = \
	    1*-8.10477468e+03
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

