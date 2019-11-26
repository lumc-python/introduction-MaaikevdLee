# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:57:19 2019

@author: Maaike
"""


### ASSIGNMENT 5 ##

d = {}
for i in range(0,100): 
    if (i**2) < 100: 
        d[i]=i**2

for i in d:
    print(i, "is the square of", d[i])
    