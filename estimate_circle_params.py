# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:23:14 2020

@author: SPeter
"""

def estimate_circle_params(x_in, y_in):
    N_fit = len(x_fit)
    orig_slope = (y_fit(N_fit) - y_fit[0])/(x_fit(N_fit) - x_fit[0]);
    perp_slope = -1/orig_slope;
    midpoint = orig_slope*((x_fit(N_fit) - x_fit[0])/2 + x_fit[0]);
    perp_isect = 
    return params_out