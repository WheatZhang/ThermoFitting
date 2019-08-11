def LiqO2(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*-4.68231731e+01+\
	    z*5.00664281e+01+\
	    y*4.76815780e+01+\
	    x*-3.50306422e+01
	x_O2 = output*8.74647329e-05+3.34108741e-04
	return x_O2

def LiqO2_pP(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*-1.23643470e-02
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_pT(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*5.16708356e-01
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def LiqO2_px_N2(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*3.74875354e+00
	x_O2 = output*1.00000000e+00+0.00000000e+00
	return x_O2

def VapN2(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*-8.19618785e-01+\
	    z*1.87584617e+00+\
	    y*8.19678415e-01+\
	    x*-6.02634406e-01
	y_N2 = output*6.20913994e-04+9.96273720e-01
	return y_N2

def VapN2_pP(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*-1.50999490e-03
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_pT(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*6.30575129e-02
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapN2_px_N2(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*9.97093706e-01
	y_N2 = output*1.00000000e+00+0.00000000e+00
	return y_N2

def VapO2(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*-4.67954237e+01+\
	    z*5.00361162e+01+\
	    y*4.76535652e+01+\
	    x*-3.50091178e+01
	y_O2 = output*3.64089095e-05+1.38859583e-04
	return y_O2

def VapO2_pP(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*-5.14373928e-03
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_pT(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*2.14963616e-01
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapO2_px_N2(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*1.55954736e+00
	y_O2 = output*1.00000000e+00+0.00000000e+00
	return y_O2

def VapEtlp(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*3.66574985e+00+\
	    z*-3.88648414e+00+\
	    y*-2.66584808e+00+\
	    x*1.99790799e+00
	vap_etlp = output*1.17643183e+00+-6.08884382e+03
	return vap_etlp

def VapEtlp_pP(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*9.48489136e+00
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_pT(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*-3.88565336e+02
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def VapEtlp_px_N2(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*-3.91409149e+03
	vap_etlp = output*1.00000000e+00+0.00000000e+00
	return vap_etlp

def LiqEtlp(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*9.28158268e+00+\
	    z*-9.91160860e+00+\
	    y*-8.28183726e+00+\
	    x*6.47200156e+00
	liq_etlp = output*9.52932508e-01+-1.08994398e+04
	return liq_etlp

def LiqEtlp_pP(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*2.48880497e+01
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_pT(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*-9.77801560e+02
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp

def LiqEtlp_px_N2(P,T,x_N2):
	x = (P-5.45290732e+02)/2.47804900e-01
	y = (T--1.77954572e+02)/8.07120000e-03
	z = (x_N2-9.92991276e-01)/1.16813408e-03
	output = \
	    1*-8.08562494e+03
	liq_etlp = output*1.00000000e+00+0.00000000e+00
	return liq_etlp
