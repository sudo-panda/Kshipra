import urllib.request
import urllib.error
import math
import numpy as np
import cv2 as cv
import pandas
import csv
import time

def inp(X,Y,rows,cols):
    dist_B_W_L = 111.320 #distance in km between latitudes and longitudes in the equator
    rng = 1 #distance in km of the area of which we need to find elevation
    N=X+((rng/2)/dist_B_W_L)
    if N>90:
        N=N%90-90
    S=X-((rng/2)/dist_B_W_L)
    if S>90:
        S=(S%-90)+90
    E=Y+((rng/2)/(dist_B_W_L*(math.cos(math.radians(X)))))
    if E>180:
        E=E%180-180
    W=Y-((rng/2)/(dist_B_W_L*(math.cos(math.radians(X)))))
    if W<180:
        W=(W%-180)+180
    heights = "sealevel"
    box=str(S)+","+str(W)+","+str(N)+","+str(E)
    BingMapsKey="AsRCr-5CGNNFnojPR7utwIayhfTOsDz5aeAQbq51t1mOG0PhNLgr20bMQYLvAt7G"
    url="http://dev.virtualearth.net/REST/v1/Elevation/Bounds?bounds="+ str(box)+"&rows="+str(rows)+"&cols="+str(cols)+"&heights="+str(heights)+"&key="+str(BingMapsKey)
    
    #print(url)

    try:
        data = str(urllib.request.urlopen(url).read(1000))
    except urllib.error.URLError as e:
        print("Error: \n",e)
        exit()

    
    return data

def imgcollection(data,rows,cols):
    u=cv.imread('40N_080E.tif',0)
    print(u[1:10,:])

def getElevation(data,rows,cols):
    data=data[data.find('"elevations":'):]
    data=data[data.find('[')+1:data.find(']')]
    
    data=np.fromstring(data,dtype=int,sep=',')
    
    
    N=81-np.shape(data)[0]
    data1=np.zeros(N)
    
    #print(np.shape(data1))
    data=(np.concatenate((data,data1), axis=0))
    data = np.reshape(data,(rows,cols))
    #print(data)

    return data

def recur(data,r,c):
    maxI=r
    maxJ=c
    for i in range(-1,2):
        for j in range(-1,2):
            try:
                if(data[maxI,maxJ]<=data[r+i,c+j]):
                    maxI=r+i
                    maxJ=c+j
            except:
                continue
    if(maxI==r and maxJ==c):
        return [maxI,maxJ]
    return recur(data,maxI,maxJ)

def slope(data,rows,cols):
    [Mi,Mj]=[int((rows +1)/2),int((cols+1)/2)]
    Ti,Tj=recur(data,int((rows +1)/2),int((cols+1)/2))
    dist=(math.sqrt(math.pow(Ti-Mi,2)+math.pow(Tj-Mj,2))/9)
    alt=abs(data[Ti][Tj]-data[Mi][Mj])
    try:
        return float(alt)/float(dist)
    except:
        return 0

dataset=list(csv.reader( open('landslidedata.csv','r'),delimiter=','))
lc=0
for row in dataset:
    try:
        if lc==0:
            lc+=1
            print(row)
            continue
        if(row[31]!=""):
            lc+=1
            continue

        X=float(row[29])
        Y=float(row[30])
    
        rows = 9
        cols = 9
        data=inp(X,Y,rows,cols)
        E=getElevation(data,rows,cols)
        X2=(slope(E,rows,cols))
        X3=str(X2)
        row[31]=X3
        with open('landslidedata.csv','w',newline='') as fl1:
            f=csv.writer(fl1)
            f.writerows(list(dataset))
            fl1.flush()
        print("Done",lc)
        time.sleep(0.2)
    except:
        print("Error or Skipped in ",lc)
    lc+=1
    
    

    #A=cv.imread("Hansen_GFC-2017-v1.5_treecover2000_30N_070E.tif",0)
    #print(A)