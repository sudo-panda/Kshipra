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
    try:
        data = str(urllib.request.urlopen(url).read(1000))
    except urllib.error.URLError as e:
        print("Error: \n",e)
        exit()

    
    return data

def getElevation(data,rows,cols):
    data=data[data.find('"elevations":'):]
    data=data[data.find('[')+1:data.find(']')]
    data=np.fromstring(data,dtype=int,sep=',')
    data = np.reshape(data,(rows,cols))
    return data

def recur(data,r,c,X,Y,sum,k):
    maxI=r
    maxJ=c

    dist_B_W_L = 111.320 #distance in km between latitudes and longitudes in the equator
    rng = 1 #distance in km of the area of which we need to find elevation
    Lat_Diff=((rng/2)/dist_B_W_L)
    Long_Diff=((rng/2)/(dist_B_W_L*(math.cos(math.radians(X)))))

    for i in range(-1,2):
        for j in range(-1,2):
            try:
                if(data[maxI,maxJ]<=data[r+i,c+j]):
                    maxI=r+i
                    maxJ=c+j
            except Exception as e:
                print(e)
                continue
    pv=pixelValue(X+((maxI-5)/4)*Lat_Diff,Y+((maxJ-5)/4)*Long_Diff)
    if(pv>=0):
        k=k+1
        sum=sum+pv
    if(maxI==r and maxJ==c):
        return [maxI,maxJ,sum/k]
    return recur(data,maxI,maxJ,X,Y,sum,k)

def pixelValue(X,Y):
    XI=(math.floor(X/10)*10)
    YI=(math.floor(Y/10)*10)
    if(XI<0):
        XS=str(abs(XI))+"S"
    else:
        XS=str(XI)+"N"
    if(YI<0):
        YS=str(abs(YI))+"W"
    else:
        YS=str(YI)+"E"
    try:
        Mat = cv.imread("LC_Data/SLC_"+XS+"_"+YS+".tif",0)
        return Mat[int(400*(X-XI))][int(400*(Y-YI))]
    except Exception as e:
        print("Error in finding pixel Value: \n",e)
        return -1

def slope(data,rows,cols,X,Y):
    [Mi,Mj]=[int((rows +1)/2),int((cols+1)/2)]
    [Ti,Tj,avg]=recur(data,int((rows +1)/2),int((cols+1)/2),X,Y,pixelValue(X,Y),1)
    dist=(math.sqrt(math.pow(Ti-Mi,2)+math.pow(Tj-Mj,2))/9)
    alt=abs(data[Ti][Tj]-data[Mi][Mj])
    return [float(alt)/float(dist),avg]



def main():
    dataset=list(csv.reader( open("landslidedata.csv",'r'),delimiter=','))
    lc=0
    for row in dataset:
        try:
            if(row[21]!="IN"):
                lc+=1
                continue
            try:
                if lc==0:
                    lc+=1
                    continue
                try:
                    if(row[31]!="" and row[32]!=""):
                        lc+=1
                        continue
                    try:
                        X=float(row[29])#Make 30
                        Y=float(row[30])#Make 29

                        rows = 9
                        cols = 9
                        data=inp(X,Y,rows,cols)
                        E=getElevation(data,rows,cols)
                        s,avg=(slope(E,rows,cols,X,Y))
                        if(row[31]==""):
                            row[31]=str(s)
                        if(row[32]==""):
                            row[32]=str(avg)
                        try:
                            with open('landslidedata.csv','w',newline='') as fl1:
                                f=csv.writer(fl1)
                                f.writerows(list(dataset))
                                fl1.flush()
                            print("Done calculating ",lc)
                            time.sleep(0.2)
                        except Exception as e:
                            print("Error 5 in main in parsing index no ",lc," :\n",e)
                            lc+=1
                            continue
                    except Exception as e:
                        print("Error 4 in main in parsing index no ",lc," :\n",e)
                        lc+=1
                        continue
                except Exception as e:
                    print("Error 3 in main in parsing index no ",lc," :\n",e)
                    lc+=1
                    continue
            except Exception as e:
                print("Error 2 in main in parsing index no ",lc," :\n",e)
                lc+=1
                continue
        except Exception as e:
            print("Error 1 in main in parsing index no ",lc," :\n",e)
        lc+=1

if __name__=="__main__":
    main()
