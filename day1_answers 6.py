# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 14:57:34 2019

@author: Maaike
"""


## ASSIGNMENT 6 ##
# load dictionary
d = {
  'The Netherlands': {
    'capital': 'Amsterdam',
    'population': 17283008,
    'continent': 'Europe',
  },
  'France': {
    'capital': 'Paris',
    'population': 67186638,
    'continent': 'Europe',
  },
  'USA': {
    'capital': 'Washington, D.C.',
    'population': 327167434,
    'continent': 'North America',
  }
}

#country with high population
maximum = 0
for i in d:
    if d[i]['population'] > maximum:
        maximum = d[i]['population']
       
for i in d: 
    if d[i]['population'] == maximum:
        print(i, maximum)

#number of countries per continent
continent_ask = input('continent = ')
number_count = 0
for i in d: 
    if d[i]['continent'] == continent_ask:
        number_count += 1
print(number_count)
        
##allow for addition of new countries
d.update({
        input('country = '):
            {'capital': input('capital = '), 
             'population': input('population = '), 
            'continent': input('continent = ')}
        })



