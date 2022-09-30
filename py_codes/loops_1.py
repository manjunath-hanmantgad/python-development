# -*- coding: utf-8 -*-
"""
@title:- loops
@author: Manjunath
"""


import numpy as np
randnum = np.random.randn()

if randnum > 0:
    print(randnum)
    
def dotproduct(a,b):
    
    """
    both vectors are numpy arrays
    both vectors have same length
    return dot product
    """
    if not (isinstance(a,np.ndarray) and isinstance(b,np.ndarray)):
        raise Exception("Must be a numpy array")
    
    if not len(a) == len(b):
        raise Exception('Must be same length')
    
    return (a*b)

a = np.array([1,2,3])
# a = [1,2,3] # just a list  # this raises an exception
b = np.array([10,10,10])

print(dotproduct(a, b))




