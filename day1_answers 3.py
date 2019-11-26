# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:57:06 2019

@author: Maaike
"""


### ASSIGNMENT 3 ##

for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0): 
        print("FizzBuzz")
    elif i % 3 == 0: 
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: 
        print(i)
        
## ASSIGNMENT 4 ##
x = list(range(0,101))
y = x

list(zip(x,y))
