# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import loadtxt

# lines = loadtxt("E:\data\ilc_di01_1_Data.csv", comments="#", delimiter=",", unpack=False);

f = open("E:\data\ilc_di01_1_Data.csv", 'r');
x = f.readlines();
f.close();

str_year = '2018';
#str_country = 'Hungary';
#str_country = 'Slovakia';
str_country = 'European Union - 28 countries (2013-2020)';
index1 = np.zeros((4, 1));
index1 = index1.astype(int);
iter1 = np.linspace(0,len(x)-1,len(x));
iter1 = iter1.astype(int);
str_val = None;
value = np.zeros((0, 0));
ind2 = 0;

for ind1 in iter1:
    index1[0] = x[ind1].find(str_year);
    index1[1] = x[ind1].find(str_country);
    index1[2] = x[ind1].find(' decile');
    index1[3] = x[ind1].find('Top cut-off point');
    Nlength = len(x[ind1]);
    if (index1[0]>=0) and (index1[1]>=0) and (index1[2]>=0)  and (index1[3]>=0):
        a = x[ind1].find('Euro',int(index1[2]),Nlength);
        b = x[ind1].find('"',a+7);
        str_val = x[ind1][a+7:b];
        if str_val == ':':
            1;
        else:
            value = np.append(value,float(str_val.replace(',','')));
        ind2 = ind2 + 1;

plt.plot(np.linspace(1,9,9), value,'+')