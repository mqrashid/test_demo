# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:55:47 2022

@author: Qasim Rashid
"""

#calculating the present value of a cash flow 
#importing numpy for numerics 
#importing timeit to compare the speed of four methods 

import numpy as np
import timeit


# Question 1 (Part 1) Explicit Python loop summing up each summand

#defining fucntion for the summing up each summand 
def summation(my_list, Mat_X):
    PV=0
    for i, Cash_Flow in enumerate(my_list):
        PV += Cash_Flow * Mat_X ** (i + 1)
    return PV

#Horner Scheme (Recursive)
def Horner(my_list, Mat_X):
    PV=0
    for i in np.arange(len(my_list)-1,-1,-1):
        PV=my_list[i]+(Mat_X*PV)
        PV*=Mat_X
        return PV

#polyVal Function 

def polyfunc(my_list,Mat_X):
    my_list=np.append(my_list[::-1],0)
    return np.polyval(my_list,Mat_X)

#Dot Product 

def dotprod(my_list,Mat_X):
    i=np.arange(1,len(my_list)+1)
    return np.dot(my_list,Mat_X ** i)

if __name__=="__main__":
    my_list=120.*np.arange(500,1200)
    r=0.01
    Mat_X=1/(1+r)
    
functional_def={"Explicit summation Loop":summation,
                "Horner's Scheme Loop":Horner,
                "polyval Function":polyfunc,
                "Dot Product of vectors":dotprod}


for k,v in functional_def.items():
   t = timeit.Timer('{}(my_list, Mat_X)'.format(v.__name__), 'from __main__ import {},my_list,Mat_X'.format(v.__name__))
   print("{}:\n\tvalue:{}, time:{} sec".format(k, v(my_list, Mat_X), t.timeit(number=1000)))
    
