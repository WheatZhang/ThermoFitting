def LiqO2(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-9.30689433e+01+\
	    z*9.30971511e+01+\
	    y*9.39424608e+01+\
	    x*-7.49588947e+01
	x_O2 = output*4.08187548e-05+9.69345517e-05
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-1.23473295e-02
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*5.14444019e-01
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*3.72403300e+00
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-8.66294615e-01+\
	    z*1.86634786e+00+\
	    y*8.66365078e-01+\
	    x*-6.91594519e-01
	y_N2 = output*5.45249466e-04+9.97618462e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-1.52172754e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*6.33742197e-02
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*9.97252695e-01
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-9.30416346e+01+\
	    z*9.30700076e+01+\
	    y*9.39154945e+01+\
	    x*-7.49376886e+01
	y_O2 = output*1.69448096e-05+4.01955240e-05
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-5.12421209e-03
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*2.13496314e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*1.54548153e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*3.67060957e+00+\
	    z*-3.67069819e+00+\
	    y*-2.67070603e+00+\
	    x*2.17392215e+00
	vap_etlp = output*1.08956792e+00+-6.09180734e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*9.55847051e+00
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-3.90388335e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-3.91940698e+03
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*8.67621202e+00+\
	    z*-8.67634483e+00+\
	    y*-7.67638494e+00+\
	    x*6.51596584e+00
	liq_etlp = output*9.47628574e-01+-1.09051398e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*2.49176486e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-9.75913510e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.42812683e+02)/2.47804900e-01
	y = (T--1.78032390e+02)/7.45390000e-03
	z = (x_N2-9.95543246e-01)/1.02042860e-03
	output = \
	    1*-8.05735185e+03
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

