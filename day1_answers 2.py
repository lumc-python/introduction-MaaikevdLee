# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:56:50 2019

@author: Maaike
"""


## ASSIGNMENT 2###
### define the tandem repeat
tandem = 'ACGT' * 3 + 'TTATT' * 5    


### print suffixes
for i in range(0, len(tandem)):
    print(tandem[i:len(tandem)])
    

### print all substrings length 3
for i in range(0,len(tandem)):
    if (i % 3 ==0) and (len(tandem[i:i+3]) == 3):
        print(tandem[i:i+3])


### print all unique substrings length 3
substrings = []
for i in range(0,len(tandem)):
    if(i % 3 == 0) and (len(tandem[i:i+3]) == 3):
        string = (tandem[i:i+3])
        if string not in substrings:
            substrings.append(string)
            print(string)

