def LiqO2(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.37248686e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.95556831e+00+\
	    z*2.66072120e+00+\
	    z2*-2.57480101e-02+\
	    y*2.18263769e+00+\
	    y*z*-2.87926627e-02+\
	    y2*-1.53536154e-02+\
	    x*-1.31413296e-01+\
	    x*z*1.65751819e-03+\
	    x*y*1.62729821e-03+\
	    x2*-2.05748084e-05
	x_O2 = output*2.11729721e-02+2.86055898e-01
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.37248686e-02
	output = \
	    1*-1.12282331e-02+\
	    z*1.41621900e-04+\
	    y*1.39039839e-04+\
	    x*-3.51591128e-06
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.37248686e-02
	output = \
	    1*4.58950577e-01+\
	    z*-6.05433017e-03+\
	    y*-6.45691286e-03+\
	    x*3.42177475e-04
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.37248686e-02
	output = \
	    1*4.10462041e+00+\
	    z*-7.94414746e-02+\
	    y*-4.44176381e-02+\
	    x*2.55700711e-03
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85778253e-01)/1.35418860e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-5.23009368e-01+\
	    z*1.52460201e+00+\
	    z2*3.43742218e-02+\
	    y*5.16391151e-01+\
	    y*z*5.77091301e-02+\
	    y2*1.82206311e-02+\
	    x*-3.25315048e-02+\
	    x*z*-3.51025119e-03+\
	    x*y*-2.30429622e-03+\
	    x2*7.82611535e-05
	y_N2 = output*1.06973745e-02+8.41488125e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85778253e-01)/1.35418860e-02
	output = \
	    1*-1.40433797e-03+\
	    z*-1.51532462e-04+\
	    y*-9.94731320e-05+\
	    x*6.75684141e-06
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85778253e-01)/1.35418860e-02
	output = \
	    1*5.48603327e-02+\
	    z*6.13089916e-03+\
	    y*3.87144466e-03+\
	    x*-2.44803686e-04
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85778253e-01)/1.35418860e-02
	output = \
	    1*1.20435504e+00+\
	    z*5.43076385e-02+\
	    y*4.55871640e-02+\
	    x*-2.77291300e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.31774835e-02
	x2 = x * x
	y2 = y * y
	z2 = z * z
	output = \
	    1*-1.90199045e+00+\
	    z*2.43675692e+00+\
	    z2*-2.23451421e-02+\
	    y*2.14856060e+00+\
	    y*z*-1.27404969e-02+\
	    y2*-2.78876904e-03+\
	    x*-1.28180649e-01+\
	    x*z*9.35066387e-04+\
	    x*y*3.28541373e-04+\
	    x2*1.38113796e-05
	y_O2 = output*1.07928091e-02+1.40674310e-01
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.31774835e-02
	output = \
	    1*-5.58273798e-03+\
	    z*4.07255751e-05+\
	    y*1.43091833e-05+\
	    x*1.20307261e-06
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.31774835e-02
	output = \
	    1*2.30295020e-01+\
	    z*-1.36559936e-03+\
	    y*-5.97832448e-04+\
	    x*3.52149444e-05
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.31774835e-02
	output = \
	    1*1.99578714e+00+\
	    z*-3.66028690e-02+\
	    y*-1.04349021e-02+\
	    x*7.65851306e-04
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85778253e-01)/1.33594279e-02
	output = \
	    1*2.64860244e+00+\
	    z*-2.72052500e+00+\
	    y*-1.68435653e+00+\
	    x*1.04057129e-01
	vap_etlp = output*2.40224814e+01+-5.97821052e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85778253e-01)/1.33594279e-02
	output = \
	    1*1.00874174e+01
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85778253e-01)/1.33594279e-02
	output = \
	    1*-4.01841082e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85778253e-01)/1.33594279e-02
	output = \
	    1*-4.89195807e+03
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.33599488e-02
	output = \
	    1*3.08836916e+00+\
	    z*-2.93713530e+00+\
	    y*-2.18235414e+00+\
	    x*1.40445884e-01
	liq_etlp = output*3.91619426e+01+-1.11458600e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.33599488e-02
	output = \
	    1*2.21954282e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.33599488e-02
	output = \
	    1*-8.48773670e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.62637073e+02)/2.47804800e-01
	y = (T--1.74564594e+02)/1.00692600e-01
	z = (x_N2-6.85595270e-01)/1.33599488e-02
	output = \
	    1*-8.60960811e+03
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

