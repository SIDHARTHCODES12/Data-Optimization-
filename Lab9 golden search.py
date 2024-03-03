# -*- coding: utf-8 -*-
"""
Created on Thursday Feb 13 14:46:26 2024
Santhosh Kumar S
2367422
"""
import math 
def f(x):
    y = math.pow(x,4)- 14*math.pow(x,3)+ 60*x*x-70*x
    return y

a0=0
b0=2
epsilon = 0.1
roe = 0.382
N= round(math.log(epsilon/2)/math.log(1-roe),0)
i=0
while (b0-a0 > epsilon):
    print("\nIteration: ",i)
    a1 = a0 +roe *(b0 - a0)
    b1 = a0 + (1- roe) * (b0 - a0) 
    fa1 = f(a1)
    fb1 = f(b1)
    print("a0 = ",a0,"b0= ",b0,"a1= ",a1,"b1= ",b1)
    print("f(a1)= ",fa1,"f(b1)= ",fb1)
    print("f(a1)<f(b1)? ",fa1<fb1)
    if (fa1) <fb1:
        b0 = b1
    else:
        a0 =a1
    i = i+1
print("Final Minimumm lies between ",a1,"and ",b1)