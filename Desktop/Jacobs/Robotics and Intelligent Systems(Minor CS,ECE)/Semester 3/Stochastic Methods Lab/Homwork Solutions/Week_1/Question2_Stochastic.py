# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:23:56 2022

@author: Qasim Rashid
"""

def c(fv, m, n, r):
    return (fv * (r / m)) / ((1 + r / m) ** (n * m + 1) - (1 + r / m))
def PV(c, m, n, r):
    return c * (1 - (1 + r / m) ** (-n * m)) / (1-1/(1+r / m))

if __name__ == '__main__':
    fv = PV(c=2000, m=12, n=30, r=0.02)
    a = c(fv=fv, m=12, n=40, r=0.02)
    print('A =', a)
    
