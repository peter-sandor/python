import numpy as np
import matplotlib.pyplot as plt

premium0 = 40000*12;
Nr_years = 30;
prem_index = 1.05;
factor_gain = 1.06;
rate_szja = 0.15;

premium1 = np.zeros((Nr_years, 1));
premium2 = np.zeros((Nr_years, 1));
total_paid = np.zeros((Nr_years, 1));
total_paid_wfees = np.zeros((Nr_years, 1));
total_with_gain = np.zeros((Nr_years, 1));
total_bonus = np.zeros((Nr_years, 1));
factor_bonus4 = np.zeros((Nr_years, 11));
years = np.linspace(1,Nr_years,Nr_years);

factor_risk = 1;
factor_fee0 = 0.99**2;
factor_fee1 = np.concatenate((0.2*np.ones((1, 1)), 0.5*np.ones((1, 1)), 0.8*np.ones((1, 1)), np.ones((Nr_years-3, 1))), axis=0);
factor_fee2 = np.concatenate((1*np.ones((3, 1)), 0.85*np.ones((np.minimum(Nr_years,17), 1)), 0.94*np.ones((np.maximum(Nr_years-20,0), 1))), axis=0);
factor_fee3 = np.concatenate((1*np.ones((3, 1)), 0.97*np.ones((np.minimum(Nr_years,17), 1)), 0.988*np.ones((np.maximum(Nr_years-20,0), 1))), axis=0);

factor_bonus1 = 0.01;
if premium0*12 < 180000:
    factor_bonus2 = 0;
elif premium0 >= 180000 and premium0 < 240000:
    factor_bonus2 = 0.01;
elif premium0 >= 240000 and premium0 < 270000:
    factor_bonus2 = 0.015;
elif premium0 >= 270000 and premium0 < 360000:
    factor_bonus2 = 0.03;
elif premium0 >= 360000 and premium0 < 480000:
    factor_bonus2 = 0.035;
else:
    factor_bonus2 = 0.04;

factor_bonus3 = np.concatenate((0*np.ones((3, 1)), 0.09*np.ones((np.minimum(Nr_years,17), 1)), 0*np.ones((np.maximum(Nr_years-20,0), 1))), axis=0);

factor_bonus4[:,0] = np.concatenate((np.array([4, 39, 9, 1, 1.96, 2.92, 3.88, 4.84, 5.8, 6.76]), np.zeros(np.maximum(Nr_years,10)-10)), axis=0);
factor_bonus4[:,1] = np.concatenate((np.array([4, 33, 9, 1, 1.96, 2.92, 3.88, 4.84, 5.8, 6.76, 7.72]), np.zeros(np.maximum(Nr_years,11)-11)), axis=0);
factor_bonus4[:,2] = np.concatenate((np.array([4, 27, 9, 1, 1.96, 2.92, 3.88, 4.84, 5.8, 6.76, 7.72, 8.68]), np.zeros(np.maximum(Nr_years,12)-12)), axis=0);
factor_bonus4[:,3] = np.concatenate((np.array([4, 21, 9, 1, 1.95, 2.90, 3.85, 4.80, 5.75, 6.70, 7.65, 8.60, 9.55]), np.zeros(np.maximum(Nr_years,13)-13)), axis=0);
factor_bonus4[:,4] = np.concatenate((np.array([4, 15, 9, 1, 1.92, 2.84, 3.76, 4.68, 5.60, 6.52, 7.44, 8.36, 9.28, 10.20]), np.zeros(np.maximum(Nr_years,14)-14)), axis=0);
factor_bonus4[:,5] = np.concatenate((np.array([4, 9, 9, 1, 1.90, 2.80, 3.70, 4.60, 5.50, 6.40, 7.30, 8.20, 9.10, 10.00, 10.90]), np.zeros(np.maximum(Nr_years,15)-15)), axis=0);
factor_bonus4[:,6] = np.concatenate((np.array([4, 4, 8, 1, 1.85, 2.70, 3.55, 4.40, 5.25, 6.10, 6.95, 7.80, 8.65, 9.50, 10.35, 11.20]), np.zeros(np.maximum(Nr_years,16)-16)), axis=0);
factor_bonus4[:,7] = np.concatenate((np.array([3, 3, 4, 1, 1.80, 2.60, 3.40, 4.20, 5.00, 5.80, 6.60, 7.40, 8.20, 9.00, 9.80, 10.60, 11.40]), np.zeros(np.maximum(Nr_years,17)-17)), axis=0);
factor_bonus4[:,8] = np.concatenate((np.array([0, 1, 3, 1, 1.75, 2.50, 3.25, 4.00, 4.75, 5.50, 6.25, 7.00, 7.75, 8.50, 9.25, 10.00, 10.75, 11.50]), np.zeros(np.maximum(Nr_years,18)-18)), axis=0);
factor_bonus4[:,9] = np.concatenate((np.array([0, 0, 2, 1, 1.67, 2.34, 3.01, 3.68, 4.35, 5.02, 5.69, 6.36, 7.03, 7.70, 8.37, 9.04, 9.71, 10.38, 11.05]), np.zeros(np.maximum(Nr_years,19)-19)), axis=0);
factor_bonus4[:,10] = np.concatenate((np.array([0, 0, 0, 1, 1.65, 2.30, 2.95, 3.60, 4.25, 4.90, 5.55, 6.20, 6.85, 7.50, 8.15, 8.80, 9.45, 10.10, 10.75, 11.40]), np.zeros(np.maximum(Nr_years,20)-20)), axis=0);
factor_bonus4 = 0.01*factor_bonus4;

factor_bonus5 = np.concatenate((0*np.ones((3, 1)), 1.005*np.ones((np.minimum(Nr_years,17), 1)), 0*np.ones((np.maximum(Nr_years-20,0), 1))), axis=0);

ind_fbonus4 = np.minimum(Nr_years-10,10);

for ind1 in range(Nr_years):
    if (ind1 <= 2):
        premium1[ind1] = premium0*prem_index**(ind1+1);
    else:
        premium1[ind1] = premium0*prem_index**3;
    
    premium2[ind1] = premium1[ind1] * factor_risk * factor_fee0 * factor_fee1[ind1] * factor_fee2[ind1] * factor_fee3[ind1];
    total_paid[ind1] = np.sum(premium1);
    total_paid_wfees[ind1] = np.sum(premium2);
    if ind1==0:
        total_with_gain[ind1] = premium2[ind1];
        total_bonus[ind1] = total_paid[ind1] * (factor_bonus1 + factor_bonus2 + factor_bonus3[ind1] + factor_bonus4[ind1,ind_fbonus4]) + total_with_gain[ind1] * factor_bonus5[ind1];
    else:
        total_with_gain[ind1] = factor_gain * total_with_gain[ind1-1] + premium2[ind1];
        total_bonus[ind1] = total_bonus[ind1-1] + premium1[ind1] * (factor_bonus1 + factor_bonus2 + factor_bonus3[ind1] + factor_bonus4[ind1,ind_fbonus4]) + total_with_gain[ind1] * factor_bonus5[ind1];

total_with_gain_bonus = total_with_gain + total_bonus;
# %matplotlib qt

plt.plot(years, total_paid,'+')
plt.plot(years, total_with_gain,'o')
plt.plot(years, total_with_gain + total_bonus,'.')