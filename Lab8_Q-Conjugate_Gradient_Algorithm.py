# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:19:32 2024
@author: 2367407
@description: Lab8 - Q-Conjugate Gradient Algorithm
"""

import numpy as np

def roundf(a, k):
    b = []
    for i in range(len(a)):
        b.append(round(a[i], k))
    return b

def isZero(g):
    result = True
    for i in range(len(g)):
        if g[i] != 0:
            result = False
            break
    return result

def ScalarMul(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

def QXMul(Q, x):
    qx = []
    for i in range(len(x)):
        qx.append(ScalarMul(Q[i], x))
    return qx

def ConjugateMUL(di, Q, dj):
    vector = []
    for j in range(len(Q)):
        vj = 0
        for i in range(len(Q)):
            vj += di[i] * Q[i][j]
        vector.append(vj)
    diQdj = ScalarMul(vector, dj)
    return diQdj

def MatMUL(a, b):
    m = len(a)
    n = len(b[0])
    
    if len(a[0]) != len(b):
        print("Incompatible matrices")
        return(a, b)
    
    t = len(a[0])
    c = []
    for i in range(m):
        row = []
        for j in range(n):
            temp = 0
            for k in range(t):
                temp += a[i][k] * b[k][j]
            row.append(temp)
        c.append(row)  
    return c

def FX(Q, b, x):
    fx = ConjugateMUL(x, Q, x)
    fx -= ScalarMul(x, b)
    return fx


# Input
Q = [[3, 0, 1],
     [0, 4, 2],
     [1, 2, 3]]
b = [3, 0, 1]
X = [[0, 0, 0]]

d = []
g = []
alpha = []
beta = []

for i in range(len(Q)):
    print("\nIteration i = ", i,
          "Initial Solution X = ", roundf(X[i], 4))
    print("Function Value...", round(FX(Q, b, X[i]), 4))
    x = X[i]
    gi = np.asarray(QXMul(Q, x)) - np.asarray(b).tolist()
    g.append(gi)
    
    print("i =", i, "\tg value...", roundf(g[i], 4))
    di = ((-1) * np.asarray(gi)).tolist()
    d.append(di)
    print("Direction i...", roundf(d[i], 4))
    
    if isZero(g[i]):
        print("Optimality Attained...")
        break
    
    alphaNr = ScalarMul(g[i], d[i])
    alphaDr = ConjugateMUL(d[i], Q, d[i])
    print("Alpha (Nr/Dr) = -", round(alphaNr, 4), "/", round(alphaDr, 4))
    alpha.append(-alphaNr/alphaDr)
    print("Alpha...", alpha[i])
    
    # Compute xi+1 = xi + alphai * di
    xip1 = (np.asarray(x) + alpha[i] * np.asarray(d[i])).tolist()
    X.append(xip1)
    print("New Solution X = ", roundf(X[i+1], 4))
    print("Function Value...", round(FX(Q, b, X[i+1])))
    
    gi1 = (np.asarray(QXMul(Q, X[i+1])) - np.asarray(b)).tolist()
    g.append(gi1)
    print("i =", i+1, "\tg value...", roundf(g[i+1], 4))
    
    if isZero(g[i+1]):
        print("Optimality Attained...")
        break
    
    betaNr = ConjugateMUL(g[i+1], Q, d[i])
    betaDr = ConjugateMUL(d[i], Q, d[i])
    print("Beta (Nr/Dr) = -", round(betaNr, 4), "/", round(betaDr, 4))
    beta.append(-betaNr/betaDr)
    print("Beta...", round(beta[i], 4))
    
    di = ((-1) * np.asarray(g[i+1]) + beta[i] * np.asarray(d[i])).tolist()
    d.append(di)
    print("Direction i+1...", roundf(d[i+1], 4))