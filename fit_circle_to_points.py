# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:23:14 2020

@author: SPeter
"""

import numpy as np
import scipy as sp

def fit_circle_to_points(x_in, y_in):
    N_fit = len(x_in)
    B0 = (y_in[1] - y_in[0])/(x_in[1] - x_in[0]);
    A0 = y_in[0] - B0 * x_in[0];
    B1 = (y_in[N_fit] - y_in[N_fit-1])/(x_in[N_fit] - x_in[N_fit-1]);
    A1 = y_in[N_fit] - B1 * x_in[N_fit];
    x0_guess = (A1-A0)/(B0-B1);
    y0_guess = A0 + B0 * x0_guess;
    R_guess = np.sqrt((x_in[0]-x0_guess)**2 + (y_in[0]-y0_guess)**2)
    par_out, pcov = sp.optimize.curve_fit(eq_circle,[x_in,y_in],np.zeros(np.shape(x_in)),p0=(20, x0_guess,y0_guess))
    
#    y_mid = (y_in(N_fit) - y_in[0])/(x_in(N_fit) - x_in[0])*(x_in[np.round(N_fit/2)] - x_in[0]) + x_in[0];
#    if y0_guess >= np.max(y_in):
#        par_out, pcov = sp.optimize.curve_fit(eq_circle_minus,x_in,y_in,p0=(20, np.min(x_in), np.max(y_in)))
#        y_fitted = eq_circle_minus(x_in,par_out[0],par_out[1],par_out[2])
#    elif y0_guess <= np.min(y_in):
#        par_out, pcov = sp.optimize.curve_fit(eq_circle_plus,x_in,y_in,p0=(20, np.min(x_in), np.max(y_in)))
#        y_fitted = eq_circle_plus(x_in,par_out[0],par_out[1],par_out[2])
#    else:
        
    return par_out

def eq_circle(x,R,x0,y0):
    return (x[:,1]-x0)**2 + (x[:,2]-y0)**2 - R**2

def eq_circle_minus(x,R,x0,y0):
    return -np.sqrt(R**2 - (x-x0)**2) + y0