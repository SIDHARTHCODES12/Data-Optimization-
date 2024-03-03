# -*- coding: utf-8 -*-
"""
Created on Thursday Feb 13 15:23:07 2024
Santhosh Kumar S
2367422
"""
import math
def f(x):
    y= (1/2)*x*x-math.sin(x)
    return(y)
def fd(x):
    fdx= x-math.cos(x)
    return(fdx)
def fdd(x):
    fddx= 1+ math.sin(x)
    return(fddx)
x0=0.5
epsilon= 0.000005
i=0
x1=x0-fd(x0)/fdd(x0)
while(abs(x0-x1)>epsilon):
    x0=x1
    x1=x0-fd(x0)/fdd(x0)
    print("\nIteration: ",i)
    print("x0= ", round(x0,6),"     x1= ", round(x1,6))
    i=i+1
   
print("Final Minimum lies between ", x0, "and ", x1)
print("f(aN)= ",f(x0), "f(bN)= ", f(x1))  