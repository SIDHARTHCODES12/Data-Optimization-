# -*- coding: utf-8 -*-
"""
Created on Thursday Feb 13 15:45:34 2024
Santhosh Kumar S
2367422
"""
import math
def f(x):
    y= math.pow(x,4)-14*math.pow(x,3)+60*x*x-70*x
    return(y)

def fd(x):
    fdx= 4* math.pow(x,3)-42*x*x+120*x-70
    return(fdx)

a0=0; b0=2; finalrange= 0.001
i=0
while(b0-a0 > finalrange/2):
    x=(a0+b0)/2
    print("\nIteration: ",i)
    print("a0= ",round(a0,4)," b0= ",round(b0,4), " Mid x= ",round(x,4))
    print("fd(x)=", round(fd(x),4), "fd(x) > 0 ? ", fd(x)>0)
    if fd(x)>0:
        b0=x
    else:
        a0=x
    i= i+1
   
print("Final Minimum lies between ", a0, "and ", b0)
print("f(aN)= ",f(a0), "f(bN)= ", f(b0))
