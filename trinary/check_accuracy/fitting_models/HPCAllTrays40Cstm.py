def LiqO2(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*-1.13678624e+02+\
	    z*1.62580285e+02+\
	    y*1.14677263e+02+\
	    x*-1.46701275e+02
	x_O2 = output*9.03778618e-06+1.82586035e-05
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*-1.07007996e-02
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*4.44094859e-01
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*3.20472642e+00
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*2.51490149e-01+\
	    z*6.41192771e-01+\
	    y*-2.51588714e-01+\
	    x*3.21717965e-01
	y_N2 = output*2.45221392e-04+9.99053344e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*6.36727999e-04
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*-2.64353992e-02
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*3.42931981e-01
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*-1.12911260e+02+\
	    z*1.61486044e+02+\
	    y*1.13909605e+02+\
	    x*-1.45719825e+02
	y_O2 = output*3.74027896e-06+7.55275130e-06
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*-4.39888813e-03
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*1.82557931e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*1.31734645e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*5.57418484e-01+\
	    z*-3.84518614e-01+\
	    y*4.42957232e-01+\
	    x*-5.18119175e-01
	vap_etlp = output*4.85581253e-01+-6.09463589e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*-2.03054145e+00
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*9.21637364e+01
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*-4.07230501e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*4.20174161e-01+\
	    z*-3.36428067e-01+\
	    y*5.80766876e-01+\
	    x*-2.49529806e-01
	liq_etlp = output*3.76557493e-01+-1.09115831e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*-7.58357532e-01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*9.37064526e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.39777073e+02)/1.23902400e-01
	y = (T--1.78119929e+02)/2.33380000e-03
	z = (x_N2-9.98231246e-01)/4.58499622e-04
	output = \
	    1*-2.76302321e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

