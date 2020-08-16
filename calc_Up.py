# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:03:29 2019

@author: peter
"""
import numpy as np
import math
import matplotlib.pyplot as plt
# SI constants
h=6.626e-34; # [J*s]
c=2.99792e8; # [m/s]
kB=1.38e-23; # [m^2*kg/(s^2*K)]
qE=1.602e-19; # [C]
mE=9.109e-31; # [kg]
mP=1.672e-27; # [kg]
eps0=8.85418e-12; # [F/m]
G=6.673e-11; # [m^3/kg/s]
NA=6e23; # [1]
alpha=1/(4*math.pi*eps0)*qE**2/(h/(2*math.pi)*c); # [1]
a0=h**2/4/math.pi**2/mE/qE**2*4*math.pi*eps0; # [m]
sigma=2*math.pi**5*kB**4/(15*c**2*h**3); # [W/(m^2*K^4)]
rSun=7e8; # [m]
mSun=1.989e30; # [kg]
LSun=3.85e26; # [W]
rEarth=6.378e6; # [m]

FE = 1; # Field Enhancement
FWHM = 1.2e-2;
lmbd = 1.03e-6;
#w=0.85*FWHM;
w = 75/35*4e-3;
f = 1.0; # [m]
#w0 = lmbd*f*1/(pi*w);
#w0 = 12.5*6.45e-6;
w0 = 55e-6;
zR = math.pi*w0**2/lmbd;
# w0x = 50e-6; # [m]
# w0y = 100e-6;
power=40e-3; # [W]
intensity=power/(math.pi*w0**2);
reprate=1e5; # [Hz]
pulse_duration=30e-15; # [s]
pulse_energy = power/reprate; # [J]
peak_intensity=pulse_energy/pulse_duration/(math.pi*w0**2) # [W/m^2]
field=math.sqrt(2*peak_intensity/eps0/c); # [V/m]
omega=2*math.pi*c/lmbd;
# Up2=9.337287*peak_intensity*1e-18*(lambda*1e6)^2
Up=qE**2/(4*mE)*(FE*field)**2/omega**2/qE # [eV]

# Keldysh parameter
# VI=10*qE; # typical 10 eV ionization energy in Joules
VI=5*qE; # 5 eV work function in Joules
peak_int2 = peak_intensity/1e4;
keldysh=omega*math.sqrt(mE*VI)/(qE*FE*field)
print("I = %.2e W/cm2" % peak_int2)
print("Up = %.2g eV" % Up)