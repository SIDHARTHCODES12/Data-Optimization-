# -*- coding: utf-8 -*-
"""
Created on Thursday Feb 13 15:23:07 2024
Santhosh Kumar S
2367422
"""
import math
def FIBO(n):
    if n==1 or n==2:
        return(n)
    else:
        return(FIBO(n-2)+FIBO(n-1))
   
def f(x):
    y= math.pow(x,4)-14*math.pow(x,3)+60*x*x-70*x
    return(y)
a0=0; b0=2
finalrange= 0.3
initialrange= b0-a0
epsilon= 0.1

def FindN(initialrange, finalrange, epsilon):
    ratio= finalrange/ initialrange
    n=1
    while FIBO(n)<(1+ 2*epsilon)/ratio:
        n=n+1
    return(n)

N= FindN(initialrange, finalrange, epsilon)
print("Value of N= ", N)

for i in range(N):
    roei= 1-FIBO(N-i)/FIBO(N-i+1)
    a1= a0+ roei *(b0-a0)
    b1= a0+(1-roei)*(b0-a0)
    fa1=f(a1)
    fb1=f(b1)
    print("\nIteration: ",i)
    print("a0= ",round(a0,4)," b0= ",round(b0,4), " a1= ",round(a1,4), " b1= ",round(b1,4))
    print("f(a1)=", round(fa1,4), "f(b1)= ", round(fb1,4))
    print("f(a1)<f(b1)?", fa1<fb1)
   
    if (fa1)<(fb1):
        b0=b1
    else:
        a0=a1
print("Final Minimum lies between ", a1, "and ", b1)
print("f(aN)= ",fa1, "f(bN)= ", fb1)
