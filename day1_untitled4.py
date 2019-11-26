# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:55:12 2019

@author: Maaike
"""

d = {}
for i in range(0,100): 
    if (i**2) < 100: 
        d.update({i:i**2})
print(d.values)