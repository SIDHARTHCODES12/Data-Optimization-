# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:16:48 2024

@author: nilea
"""
def lpp_std_form(c,a,bt):
    m1,n= len(c),len(a[0])
    for i in range(m1,n+m1):
        c.append(0)
    m=len(a)
    for i in range (m):
        for j in range (n,n+m):
            if i==(j-n):
                a[i].append(1)
            else:
                a[i].append(0)
        a[i].append(bt[i])
    return(c,a)

def stdform_table(c,a):
    m=len(a)
    n=len(c)-m
    print("m,n=",m,",",n)
    c1=[]
    for i in range(m+n):
        c1.append(-1*c[i])
    a.append(c1)
    basis=[]
    for i in range(n):
        basis.append(0)
    for i in range(m):
        basis.append(1)
    for i in range(m):
        a[i].append(n+i)
    a[m].append(0)
    return(a,basis)

def check_optimal(a):
    optimal= True
    m=len(a)-1
    n= len(a[0])-m-2
    print("m,n=",m,",",n)
    for j in range(n+m):
        if a[m][j]<0:
            optimal= False
            break
    return(optimal)

def outgoing_variable(a,enter):
    j = enter
    m = len(a)-1
    n = len(a[0])-m-2
    print("m,n=",m,",",n)
    ratio=[]
    for i in range(m):
        if a[i][j]>0:
            r=a[i][m+n]/a[i][j]
        else:
            r=999999
        ratio.append(r)
    minimum=min(ratio)
    i = ratio.index(minimum)
    print("ratio",ratio)
    print("minimum",minimum)
    return(i,minimum)

def entering_variable(a):
    m=len(a)-1
    n=len(a[0])-m-2
    print("m,n=",m,",",n)
    minimum=min(a[m])
    j=a[m].index(minimum)
    return j

def improved_bfs(a,enter,outgo):
    m=len(a)
    n=len(a[0])-1
    pivot=a[outgo][enter]
    for j in range (n):
        a[outgo][j]=a[outgo][j]/pivot
    for i in range (m):
        if i!=outgo:
            pivot1=a[i][enter]
            for j in range (n):
                a[i][j]=a[i][j]-a[outgo][j]*pivot1
    out=int(a[outgo][n])
    basis[out]=0
    basis[enter]=1
    a[outgo][n]=enter
    return (a,basis)

c=[2,3]
a=[[1,1,-1,4],
   [1,-2,-1,1],]
bt=[8,2]

cstd,astd=lpp_std_form(c,a,bt)
print("The cost vector in Std form",cstd)
print("Matrix A in STD form")
m=len(astd)
for i in range(m):
    print(astd[i])
alpp,basis=stdform_table(cstd,astd)
print("lpp in simplext table:")
for i in range(m+1):
    print(alpp[i])
print("basis:",basis)
print("initial BFS")
print("is this an optimal solution?",check_optimal(alpp))
iteration=0
while check_optimal(alpp)==False:
    iteration+=1
    print("\n\n simplex method iteration=",iteration)
    enter=entering_variable(alpp)
    outgo,mini=outgoing_variable(alpp,enter)
    if mini==999999:
        print("optimal solution reached")
        break
    print("enter",enter,"outgoing",outgo)
    print(f'the pivot element is alpp[{enter}][{outgo}]={alpp[enter][outgo]}')
    a1,basis=improved_bfs(alpp,enter,outgo)
    print("new basis..",basis)
    print("revised simplex matrix..")
    for i in range(m+1):
        print(a1[i])
    alpp=a1
    print("is this an optimal solution?",check_optimal(alpp))
print("\n\noptimal solution",alpp[m][-1])
for i in range(m):
    print("x",alpp[i][-1],"=",alpp[i][-2])