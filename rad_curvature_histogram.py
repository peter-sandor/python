# -*- coding: utf-8 -*-
"""
Modified on Mon Aug 03 2020

@author: Judit, Peter
"""
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

from skimage.draw import ellipse
from skimage.measure import find_contours, approximate_polygon, subdivide_polygon  
from skimage import measure
from skimage import feature
from skimage.feature import corner_harris, corner_subpix, corner_peaks

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
    if np.shape(contour)[0]>100 and (np.max(contour[:, 1])-np.min(contour[:, 1]))<45 and (np.max(contour[:, 0])-np.min(contour[:, 0]))<27:
        fig=plt.figure(figsize=(9, 4))
        new_s = contour.copy()
        new_s[:,0]=new_s[:,0]-np.min(new_s[:,0])
        new_s[:,1]=new_s[:,1]-np.min(new_s[:,1])
        ax1.plot(contour[:, 1], contour[:, 0], '-r',linewidth=3)
        plt.plot(new_s[:, 1], new_s[:, 0],'-r',linewidth=3)
#plt.show()
        for k in range(2): #meroleges vonalak
            szaml=0;
            for i in range(np.shape(new_s)[0]):
                if vy[k,0]<new_s[i,0]<vy[k,1] and vx[k,0]<new_s[i,1]<vx[k,1] and szaml==0:
                    x=new_s[i,1];
                    y=new_s[i,0];
                    szaml=szaml+1;
                if  vy[k,0]<new_s[i,0]<vy[k,1] and vx[k,0]<new_s[i,1]<vx[k,1]:
                    x=np.append(x,new_s[i,1]);
                    y=np.append(y,new_s[i,0]);
            z[k] = np.polyfit(x, y, 1)
            yf[:,k]=z[k,1]+z[k,0]*xbase    
        for k in range(2,4): #fuggoleges vonalak
            szaml=0
            for i in range(np.shape(new_s)[0]):
                if vy[k,0]<new_s[i,0]<vy[k,1] and vx[k,0]<new_s[i,1]<vx[k,1] and szaml==0:
                    y=new_s[i,1];
                    x=new_s[i,0];
                    szaml=szaml+1;
                if  vy[k,0]<new_s[i,0]<vy[k,1] and vx[k,0]<new_s[i,1]<vx[k,1]:
                    y=np.append(y,new_s[i,1]);
                    x=np.append(x,new_s[i,0]);
            zv[k-2] = np.polyfit(x, y, 1) ##y-x-ben jobban fitteli a függőleges vonalakat ======================================
            z[k]=np.array([np.divide(1,zv[k-2,0]),-1*zv[k-2,1]*np.divide(1,zv[k-2,0])]) ##visszateres x-y KR-be======================================
            xf[:,k-2]=zv[k-2,1]+zv[k-2,0]*ybase
            yf[:,k]=z[k,1]+z[k,0]*xbase
        plt.ylim(0,30)
        plt.xlim(0,50)
        for i in range(2):
            plt.plot(xbase,yf[:,i],'-b',linewidth=2)
        for i in range(2,4):
            plt.plot(xbase,yf[:,i],'-b',linewidth=2)
        for i in range(2):
            plt.plot(xf[:,i],ybase,'-b',linewidth=2)
        szaml=0
        for i in range(2): ##egyenes metszetek szamolasa ======================================7
            for j in range(2,4):
                mets[szaml,0]=np.divide((z[j,1]-z[i,1]),(z[i,0]-z[j,0]))
                mets[szaml,1]=z[i,1]+z[i,0]*mets[szaml,0]
                szaml=szaml+1
        lengsz[0]=0.5*pixelnm*(np.sqrt((mets[1,0]-mets[0,0])**2+(mets[1,1]-mets[0,1])**2)+np.sqrt((mets[3,0]-mets[2,0])**2+(mets[3,1]-mets[2,1])**2))
        for k in range(2): ##erintesi pontok szamolasa ======================================7
            szaml=0
            for i in range(np.shape(new_s)[0]):
                if vy[k,0]<new_s[i,0]<vy[k,1] and szaml==0:
                    x=new_s[i,1]
                    y=new_s[i,0]
                    szaml=szaml+1
                if  vy[k,0]<new_s[i,0]<vy[k,1]:
                    x=np.append(x,new_s[i,1])
                    y=np.append(y,new_s[i,0])
                    szaml=szaml+1
                plt.plot(x,y,'xy',markersize=5)
                figmer1 = np.sqrt((mets[2*k,0]-x)**2+(mets[2*k,1]-y)**2)+suly*np.sqrt((y-(z[k,1]+z[k,0]*x))**2)
                figmer2 = np.sqrt((mets[2*k+1,0]-x)**2+(mets[2*k+1,1]-y)**2)+suly*np.sqrt((y-(z[k,1]+z[k,0]*x))**2)
            erint[k*2]=np.array([szamres,x[np.argmin(figmer1)],y[np.argmin(figmer1)],pixelnm*np.sqrt((mets[2*k,0]-x[np.argmin(figmer1)])**2+(mets[2*k,1]-y[np.argmin(figmer1)])**2)])              
            erint[2*k+1]=np.array([szamres,x[np.argmin(figmer2)],y[np.argmin(figmer2)],pixelnm*np.sqrt((mets[2*k+1,0]-x[np.argmin(figmer2)])**2+(mets[2*k+1,1]-y[np.argmin(figmer2)])**2)])                
            #print erint
        for k in range(2):
            l=k+2
            szaml=0
            for i in range(np.shape(new_s)[0]):
                if vx[l,0]<new_s[i,1]<vx[l,1] and szaml==0:
                    x=new_s[i,1]
                    y=new_s[i,0]
                    szaml=szaml+1
                if  vx[l,0]<new_s[i,1]<vx[l,1]:
                    x=np.append(x,new_s[i,1])
                    y=np.append(y,new_s[i,0])
                    szaml=szaml+1
                #plt.plot(x,y,'.')
                figmer1 = np.sqrt((mets[k,0]-x)**2+(mets[k,1]-y)**2)+suly*np.sqrt((x-(zv[k,1]+zv[k,0]*y))**2)
                figmer2 = np.sqrt((mets[k+2,0]-x)**2+(mets[k+2,1]-y)**2)+suly*np.sqrt((x-(zv[k,1]+zv[k,0]*y))**2)
            erint[4+k*2]=np.array([szamres,x[np.argmin(figmer1)],y[np.argmin(figmer1)],pixelnm*np.sqrt((mets[k,0]-x[np.argmin(figmer1)])**2+(mets[k,1]-y[np.argmin(figmer1)])**2)])              
            erint[2*k+5]=np.array([szamres,x[np.argmin(figmer2)],y[np.argmin(figmer2)],pixelnm*np.sqrt((mets[k+2,0]-x[np.argmin(figmer2)])**2+(mets[k+2,1]-y[np.argmin(figmer2)])**2)])                
            #print erint
        plt.plot(mets[:,0],mets[:,1],'xg', markersize=20, mew=2)
        plt.plot(erint[:,1],erint[:,2],'xk', label=str(n), markersize=20,mew=2)
        plt.legend(numpoints=1)
#        plt.show()
#        print mets
#        print erint
#        print szamres
        if szamres==0:
            res=erint
            lengszres=lengsz
        else:
            res=np.append(res,erint,axis=0)
            lengszres=np.append(lengszres,lengsz,axis=0)
        szamres=szamres+1

# print res
# print lengszres
#np.savetxt('length_atlag_54',lengszres)

"""
szaml=0
for n, contour in enumerate(contours):
    if np.shape(contour)[0]>300:
        szaml=szaml+1
        new_s = contour.copy()
        new_s[:,0]=new_s[:,0]-np.min(new_s[:,0])
        new_s[:,1]=new_s[:,1]-np.min(new_s[:,1])
        szaml2=0        
        for m, contour2 in enumerate(contours2):            
            if np.shape(contour2)[0]>300:
                szaml2=szaml2+1
                if szaml2==szaml:                
                    new_s2 = contour2.copy()
                    new_s2[:,0]=new_s2[:,0]-np.min(new_s2[:,0])
                    new_s2[:,1]=new_s2[:,1]-np.min(new_s2[:,1])
                    plt.plot(new_s2[:, 1], new_s2[:, 0],'.r')
                    plt.plot(new_s[:, 1], new_s[:, 0],'.b')
                    plt.title(str(szaml)+'_'+str(szaml2))
                    appr_s = approximate_polygon(new_s, tolerance=0.8)
                    appr_s2 = approximate_polygon(new_s2, tolerance=0.8)
                    for i in range(30):
                        print appr_s[i], appr_s2[i]
                    plt.show()
#"""