# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:06:12 2020

@author: peter
"""

import numpy as np
import matplotlib.pyplot as plt

data1=np.loadtxt('data1.txt')
data2=np.loadtxt('data2.txt')
data3=np.loadtxt('data3.txt')


# =============================================================================
# plt.plot(data2[:,0],data2[:,2]-1.0,'x')
# plt.plot(data2[:,0],data2[:,1]-1.0,'o')
# =============================================================================
plt.plot(data2[:,0],data3[:,1]-1.0,'o')
plt.show()