## UNIFAC CALCULATIONS
## r= Unifac parameter pertaining to the volume of each group in the molecule.
## q= Unifac parameter pertaining to the area of molecule.
## R= Universal Gas Constant (8.31775 J/mol.K)
## Temperature (T) = 25 degree C (298.16 K)


import pylab as pb
import numpy as np
import pandas as pd
lak= pd.read_excel("Process Simulation Lab.xlsx","LLE")
for i in lak:
    print i

print "Parameters", " Water", "   Methanol"
for i in range(len(lak['Water'])):    
    print i+1,'.',lak['Parameters'][i],'\t', lak['Water'][i],'\t', lak['Methanol'][i]
    
lak1= pd.read_excel("Process Simulation Lab.xlsx","Sheet1")
for i in lak1:
    print i 
    
print "  ","X1","   X2"
for i in range(len(lak1['X1'])):
    print i+1, '.',lak1['X1'][i], '\t', lak1['X2'][i]
xWat = lak1['X1'];
xMet = lak1['X2'];
VWat = lak['Water'][2];
VMet = lak['Methanol'][2];
AWat = lak['Water'][1];
AMet = lak['Methanol'][1];


def volfrac(x1,x2,v1,v2):
    return x1*v1/(x1*v1+x2*v2)
print "VWater", " VMethanol"
volFracW=[]
volFracM=[]
for i in range(len(xWat)):
    temp=volfrac(xWat[i],xMet[i],VWat,VMet)    
    print round(temp,3),'\t',round(1-temp,3)
    volFracW.append(temp)
    volFracM.append(1-temp)
    
def areafrac (x1,x2,q1,q2):
    return x1*q1/(x1*q1+x2*q2)

print "AWater" , "AMethanol"

areaFracW=[]
areaFracM=[]
for i in range(len(xWat)):
    temp1=areafrac(xWat[i],xMet[i],AWat,AMet)
    print round(temp1,3), '\t' , round(1-temp1,3)
    areaFracW.append(temp1)
    areaFracM.append(1-temp1)
    
    
def longCalc (V1,V2, A1, A2, q1, q2, X1, X2):
    return (8.314*298.16*((X1* np.log(V1/X1)+X2*np.log (2/X2))+5*((X1*q1*np.log (A1/V1))+(X2*q2*np.log (A2/V2)))))
    
print "G"

G=[]
for i in range(len(xWat)):
    temp2= longCalc (volFracW[i],volFracM[i],areaFracW[i],areaFracM[i],lak['Water'][1],lak['Methanol'][1],xWat[i],xMet[i])
    print round(temp2,3)
    G.append(temp2)
    
    
pb.plot(xWat,G)
pb.xlabel("xWat")
pb.ylabel("G")
pb.title("Gibbs Free Energy")


    