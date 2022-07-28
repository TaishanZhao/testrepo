# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:49:37 2020

@author: zhaot
"""

import numpy as np
def gaussElim(A,b):
    n=len(b)
    for k in range(n-1):
        for i in range(k+1,n):          
            if A[i,k] != 0.0:
                lamda = A[i,k]/A[k,k]
                A[i,k] = 0.0
                A[i,k+1:n] = A[i,k+1:n]-lamda*A[k,k+1:n]
                b[i] = b[i]-lamda*b[k]
    b[n-1] = b[n-1]/A[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(A[k,k+1:n],b[k+1:n])) / A[k,k]
    return b        
