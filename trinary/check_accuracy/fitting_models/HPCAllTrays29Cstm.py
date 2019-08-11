def LiqO2(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*-2.82009023e+01+\
	    z*3.18974132e+01+\
	    y*2.89038031e+01+\
	    x*-1.99935755e+01
	x_O2 = output*1.53101425e-04+6.10935606e-04
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*-1.23526407e-02
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*5.16976266e-01
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*3.75564301e+00
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*-7.82471076e-01+\
	    z*1.88293727e+00+\
	    y*7.82535750e-01+\
	    x*-5.41795329e-01
	y_N2 = output*6.89231935e-04+9.95406314e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*-1.50692195e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*6.30094897e-02
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*9.98046675e-01
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.18240900e-03
	output = \
	    1*-2.84684363e+01+\
	    z*2.92681168e+01+\
	    y*2.91684133e+01+\
	    x*-2.01759940e+01
	y_O2 = output*6.31195857e-05+2.54941228e-04
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.18240900e-03
	output = \
	    1*-5.13912511e-03
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.18240900e-03
	output = \
	    1*2.15086586e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.18240900e-03
	output = \
	    1*1.56239626e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*3.54806117e+00+\
	    z*-3.89747415e+00+\
	    y*-2.54818846e+00+\
	    x*1.79786361e+00
	vap_etlp = output*1.31365432e+00+-6.08714966e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*9.53076913e+00
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*-3.91065068e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*-3.93744000e+03
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*9.40277481e+00+\
	    z*-1.05663632e+01+\
	    y*-8.40303877e+00+\
	    x*6.18246340e+00
	liq_etlp = output*9.96554547e-01+-1.08965666e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*2.48629548e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*-9.78303990e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.46529756e+02)/2.47804900e-01
	y = (T--1.77912681e+02)/8.55980000e-03
	z = (x_N2-9.91318725e-01)/1.30032045e-03
	output = \
	    1*-8.09797096e+03
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp
