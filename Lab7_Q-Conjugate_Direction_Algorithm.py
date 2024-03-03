# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:35:06 2024
@author: 2367407
@description: Lab7 - Given a Quadratic function f(x) find the solution x that minimizes the function value.
"""

import numpy as np

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


# Input
Q = [[4, 2],
     [2, 2]]
b = [-1, 1]
X = [[0, 0]]
d = [[1, 0],
     [1, -2]]

g = []
alpha = []

for i in range(len(Q)):
    print("\nIteration i = ", i, "Initial Solution X = ", X[i])
    x = X[i]
    g.append(np.asarray(QXMul(Q, x)) - np.asarray(b))
    print("i =", i, "\tg value...", g[i])
    
    alphaNr = ScalarMul(g[i], d[i])
    alphaDr = ConjugateMUL(d[i], Q, d[i])
    print("Alpha (Nr/Dr) = -", alphaNr, "/", alphaDr)
    alpha.append(-alphaNr/alphaDr)
    print("Alpha...", alpha[i])
    
    # Compute x1 = x0 + alpha * d0
    xip1np = np.asarray(x) + alpha[i] * np.asarray(d[i])
    xip1 = xip1np.tolist()
    X.append(xip1)
    print("New Solution X = ", X[i+1])