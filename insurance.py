# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

premium0 = 40000;
prem_index = 1.05;
factor_gain = 1.05;
premium1 = np.zeros((12*30, 1));
premium2 = np.zeros((12*30, 1));
total_paid = np.zeros((12*30, 1));
total_with_gain = np.zeros((12*30, 1));
months = np.linspace(1,12*30,12*30);
factor_risk = 1;
factor_fee1 = np.concatenate((0.2*np.ones((12, 1)), 0.5*np.ones((12, 1)), 0.8*np.ones((12, 1)), np.ones((12*27, 1))), axis=0);
factor_fee2 = np.concatenate((1*np.ones((12*3, 1)), 0.85*np.ones((12*17, 1)), 0.94*np.ones((12*10, 1))), axis=0);
factor_fee3 = np.concatenate((1*np.ones((12*3, 1)), 0.97*np.ones((12*17, 1)), 0.988*np.ones((12*10, 1))), axis=0);

for ind1 in range(12*30):
    if (ind1 <= 36):
        premium1[ind1] = premium0*prem_index**(ind1//12);
    else:
        premium1[ind1] = premium0*prem_index**3;
    
    premium2[ind1] = premium1[ind1] * factor_risk * factor_fee1[ind1] * factor_fee2[ind1] * factor_fee3[ind1];
    total_paid[ind1] = np.sum(premium1);
    if ind1==0:
        total_with_gain[ind1] = factor_gain * premium2[ind1];
    elif np.remainder(ind1,12)==0:
        total_with_gain[ind1] = factor_gain * (total_with_gain[ind1-1] + premium2[ind1]);
    else:
        total_with_gain[ind1] = total_with_gain[ind1-1] + premium2[ind1];

# %matplotlib qt
plt.plot(months, premium2)
plt.plot(months, total_paid,'+')
plt.plot(months, total_with_gain,'o')