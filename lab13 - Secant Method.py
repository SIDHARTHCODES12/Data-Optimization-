# -*- coding: utf-8 -*-
"""
Created on Thursday Feb 13 15:23:07 2024
Santhosh Kumar S
2367422
"""
def g(x):
    y= x*x*x - 12.2*x*x + 7.45*x + 42
    return(y)
def xkplus1(x0, x1):
    Nr= g(x1)*x0 - g(x0)*x1
    Dr= g(x1)- g(x0)
    x2= Nr/Dr
    return(x2)

x0=13
x1=12
epsilon= 0.000005
i=0

while(abs(x0-x1)>epsilon):
    x2= xkplus1(x0, x1)
    print("\nIteration: ",i)
    print("x0= ", round(x0,6),
          "     x1= ", round(x1,6),
          "     x2= ", round(x1,6))
    x0= x1; x1=x2
    i= i+x1
   
print("Final Minimum lies between ", x0, "and ", x1)
print("x0= ",x0, "and x1= ",x1)  