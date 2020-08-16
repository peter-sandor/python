# -*- coding: utf-8 -*-
"""
Modified on Mon Aug 03 2020

@author: Judit, Peter
"""
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

#import numpy.matlib as npml

#from skimage.draw import ellipse
#from skimage.measure import find_contours, approximate_polygon, subdivide_polygon  
from skimage import measure
from skimage import feature
#from scipy.optimize import curve_fit

def eq_circle(x,R,x0,y0):
    N = np.shape(x)[0]
    out = (x[0:np.int(N/2)]-x0)**2 + (x[np.int(N/2):N]-y0)**2 - R**2
    return np.concatenate((out,np.zeros(np.shape(out))))

def eq_circle_plus(x,R,x0,y0):
    return np.sqrt(R**2 - (x-x0)**2) + y0

def eq_circle_minus(x,R,x0,y0):
    return -np.sqrt(R**2 - (x-x0)**2) + y0
#from skimage.feature import corner_harris, corner_subpix, corner_peaks
    
def fit_circle_to_points2(x_in, y_in):
    N_fit = len(x_in)
    B0 = (y_in[1] - y_in[0])/(x_in[1] - x_in[0]);
    A0 = y_in[0] - B0 * x_in[0];
    B1 = (y_in[N_fit-1] - y_in[N_fit-2])/(x_in[N_fit-1] - x_in[N_fit-2]);
    A1 = y_in[N_fit-1] - B1 * x_in[N_fit-1];
    x0_guess = (A1-A0)/(B0-B1);
    y0_guess = A0 + B0 * x0_guess;
    R_guess = np.sqrt((x_in[0]-x0_guess)**2 + (y_in[0]-y0_guess)**2)
    data_fit = np.hstack((x_in,y_in))
    par_out = sp.optimize.curve_fit(eq_circle,data_fit,np.zeros(np.shape(data_fit)),p0=(R_guess,x0_guess,y0_guess))
    return par_out

# Construct some test data
#x, y = np.ogrid[-np.pi:np.pi:100j, -np.pi:np.pi:100j]
#r = np.sin(np.exp((np.sin(x)**3 + np.cos(y)**2)))
plt.close('all')
img=mpimg.imread('05_feld150_03_crop_sm2.jpg');

#img=mpimg.imread('02_feld120_04mod_csakteglalap_smooth.jpg')

# print np.shape(img);
edges2 = feature.canny(img, sigma=2) # image with detected edges
fig, ax2 = plt.subplots();
ax2.imshow(edges2,cmap = plt.cm.gray);

#x0=np.linspace(0,np.shape(img)[1]-1,np.shape(img)[1])
#plt.plot(x0,img[650,:])
#plt.xlim(0,200)
#plt.ylim(60,240)
#plt.show()

# Find contours at a constant value of 0.8
contours = measure.find_contours(img, 160, fully_connected='high');
contours2 = measure.find_contours(img, 160, fully_connected='high');

# Display the image and plot all contours found
fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=(7,14));
ax1.imshow(img, interpolation='nearest', cmap=plt.cm.gray);
for n in range(len(contours)-1):
    if np.shape(contours[n])[0]>100 and (np.max(contours[n][:,1])-np.min(contours[n][:, 1]))<45 and (np.max(contours[n][:, 0])-np.min(contours[n][:, 0]))<27:   
        ax1.plot(contours[n][:,1], contours[n][:,0], '-r',linewidth=3);
ax1.axis('image')
plt.title('ez')
ax1.set_xticks([])
ax1.set_yticks([])
plt.show()

N_list = 4;
vy=np.array([[22, 30],[0,3],[7,20],[7,20]])
vx=np.array([[8, 37],[8,37],[0,5],[40,45]])
z=np.zeros((4,2))
zv=np.zeros((2,2))
xbase=np.linspace(0,160,160)
ybase=np.linspace(0,120,120)
yf=np.zeros((160,4))
xf=np.zeros((120,2))
#plt.show()
mets=np.zeros((4,2))
erint=np.zeros((8,4))
suly=6
lengsz=np.zeros((1))

pixelnm=200/54.0

szamres=0
for n in range(0,1):
    contour = contours[n];
    N_contour = np.shape(contour)[0];
    if np.shape(contour)[0]>100 and (np.max(contour[:, 1])-np.min(contour[:, 1]))<45 and (np.max(contour[:, 0])-np.min(contour[:, 0]))<27:
        new_s = contour.copy()
        new_s[:,0]=new_s[:,0]-np.min(new_s[:,0])
        new_s[:,1]=new_s[:,1]-np.min(new_s[:,1])
        plt.Figure, ax1 = plt.subplots(); ax1.plot(contour[:,1], contour[:,0], '-r',linewidth=3);
#        plt.plot(new_s[:, 1], new_s[:, 0],'-r',linewidth=3)
        path_length = np.zeros((N_contour,1))
        path_length[0] = 0;
        for ind1 in range(1,np.shape(contour)[0]):
            path_length[ind1] = path_length[ind1-1] + np.sqrt((contour[ind1,0]-contour[ind1-1,0])**2 + (contour[ind1,1]-contour[ind1-1,1])**2);
        dyds = np.gradient(contour[:,0], path_length[:,0]);
        dxds = np.gradient(contour[:,1], path_length[:,0]);
        ddydss = np.gradient(dyds, path_length[:,0]);
        ddxdss = np.gradient(dxds, path_length[:,0]);
        vec_mag = np.sqrt(ddxdss**2 + ddydss**2);
        mask_all = vec_mag>0.12;
#        mask_dy = np.logical_and(np.abs(dyds)>0.1,np.abs(dyds)<0.90)
#        mask_dx = np.logical_and(np.abs(dxds)>0.1,np.abs(dxds)<0.90)
#        mask_all = np.logical_and(mask_dx,mask_dy)
        mask_01 = mask_all*1;
        plt.Figure, ax2 = plt.subplots(); ax2.plot(dxds, '-k',linewidth=3), ax2.plot(dyds, '-r',linewidth=3), ax2.plot(mask_01, 'ob',linewidth=3)
        plt.Figure, ax3 = plt.subplots(); ax3.plot(ddxdss, '-k',linewidth=3), ax3.plot(ddydss, '-r',linewidth=3), ax3.plot(vec_mag,'og',linewidth=3), ax3.plot(mask_01, 'ob',linewidth=3)
        ax1.plot(contour[mask_all,1], contour[mask_all,0], 'ok',linewidth=3)
        
        temp = np.array([]);
        corner_list = []
        ind2 = 0;
        ind3 = 0;
        while ind2 < N_contour:
            if mask_all[ind2]:
                temp = np.append(temp,ind2);
                ind3 = ind3 + 1;
                if ind2 == N_contour-1 and len(temp) >= N_list:
                    corner_list.append([int(ind1) for ind1 in temp]);
            else:
                if len(temp) >= N_list:
                    corner_list.append([int(ind1) for ind1 in temp]);
                ind3 = 0;
                temp = np.array([]);
            ind2 = ind2 + 1;
        
        radii = [];
        for ind1 in range(len(corner_list)):
            x_fit = contour[corner_list[ind1],1]
            y_fit = contour[corner_list[ind1],0]
            par_out = fit_circle_to_points2(x_fit,y_fit)
#            N_fit = len(x_fit)
#            test_val = (y_fit(N_fit) - y_fit[0])/(x_fit(N_fit) - x_fit[0])*(x_fit[np.round(N_fit/2)] - x_fit[0]) + x_fit[0];
#            if test_val > y_fit[np.round(N_fit/2)]:
#                x0_guess = ;
#                y0_guess = ;
#                par_out, pcov = sp.optimize.curve_fit(eq_circle_minus,x_fit,y_fit,p0=(20, np.min(x_fit), np.max(y_fit)))
#            else:
#                par_out, pcov = sp.optimize.curve_fit(eq_circle_plus,x_fit,y_fit,p0=(20, np.min(x_fit), np.max(y_fit)))
            radii.append(par_out[0])
            y_fitted = eq_circle(x_fit,par_out[0],par_out[1],par_out[2])
            plt.Figure, ax4 = plt.subplots(); ax4.plot(x_fit,y_fit,'ok'), ax4.plot(x_fit,y_fitted,'-r')
            
        
