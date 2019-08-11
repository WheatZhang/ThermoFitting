def LiqO2(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.12775529e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.94172442e+00+\
	    z*2.63019306e+00+\
	    z2*-1.75620598e-02+\
	    y*2.17720726e+00+\
	    y*z*-1.87579777e-02+\
	    y2*-1.05405206e-02+\
	    x*-1.63434921e-01+\
	    x*z*1.35691417e-03+\
	    x*y*1.36569121e-03+\
	    x2*-2.01036253e-05
	x_O2 = output*1.73344983e-02+2.39551307e-01
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.12775529e-02
	output = \
	    1*-1.14326325e-02+\
	    z*9.49191335e-05+\
	    y*9.55331067e-05+\
	    x*-2.81258570e-06
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.12775529e-02
	output = \
	    1*4.69768517e-01+\
	    z*-4.04734430e-03+\
	    y*-4.54858369e-03+\
	    x*2.94670492e-04
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.12775529e-02
	output = \
	    1*4.04281651e+00+\
	    z*-5.39885733e-02+\
	    y*-2.88325078e-02+\
	    x*2.08568530e-03
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.08782948e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-5.95761546e-01+\
	    z*1.61430549e+00+\
	    z2*3.03699902e-02+\
	    y*5.78610478e-01+\
	    y*z*5.18720326e-02+\
	    y2*1.71502628e-02+\
	    x*-4.50993678e-02+\
	    x*z*-3.92664474e-03+\
	    x*y*-2.69839821e-03+\
	    x2*1.13595483e-04
	y_N2 = output*7.84478949e-03+8.69606581e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.08782948e-02
	output = \
	    1*-1.42771611e-03+\
	    z*-1.24306264e-04+\
	    y*-8.54235163e-05+\
	    x*7.19221168e-06
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.08782948e-02
	output = \
	    1*5.64989590e-02+\
	    z*5.06509293e-03+\
	    y*3.34930676e-03+\
	    x*-2.63487606e-04
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.08782948e-02
	output = \
	    1*1.16414264e+00+\
	    z*4.38021188e-02+\
	    y*3.74070738e-02+\
	    x*-2.83166636e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.14658132e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.89337288e+00+\
	    z*2.58127400e+00+\
	    z2*-1.79109626e-02+\
	    y*2.15604557e+00+\
	    y*z*-8.04624714e-03+\
	    y2*-1.17894712e-03+\
	    x*-1.60559981e-01+\
	    x*z*7.96239900e-04+\
	    x*y*1.65581029e-04+\
	    x2*1.98748171e-05
	y_O2 = output*8.49520691e-03+1.14295878e-01
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.14658132e-02
	output = \
	    1*-5.50429093e-03+\
	    z*2.72965656e-05+\
	    y*5.67642166e-06+\
	    x*1.36269043e-06
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.14658132e-02
	output = \
	    1*2.27984202e-01+\
	    z*-8.50824891e-04+\
	    y*-2.49328051e-04+\
	    x*1.75088409e-05
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.14658132e-02
	output = \
	    1*1.91250776e+00+\
	    z*-2.65410451e-02+\
	    y*-5.96159496e-03+\
	    x*5.89947051e-04
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34428785e-01)/1.10884550e-02
	output = \
	    1*2.63786870e+00+\
	    z*-2.72595478e+00+\
	    y*-1.68165952e+00+\
	    x*1.28928141e-01
	vap_etlp = output*1.91736890e+01+-5.99521206e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34428785e-01)/1.10884550e-02
	output = \
	    1*9.97570300e+00
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34428785e-01)/1.10884550e-02
	output = \
	    1*-4.01343846e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34428785e-01)/1.10884550e-02
	output = \
	    1*-4.71360611e+03
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.12775529e-02
	output = \
	    1*3.10198036e+00+\
	    z*-3.02588461e+00+\
	    y*-2.20750376e+00+\
	    x*1.77399090e-01
	liq_etlp = output*3.18079906e+01+-1.11020908e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.12775529e-02
	output = \
	    1*2.27707708e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.12775529e-02
	output = \
	    1*-8.73998211e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.61398049e+02)/2.47804900e-01
	y = (T--1.75105086e+02)/8.03391333e-02
	z = (x_N2-7.34239687e-01)/1.12775529e-02
	output = \
	    1*-8.53441432e+03
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp
