# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 00:30:50 2024

@author: rites
"""

#numpy package==>to adavance calculations=>array calculation==>array has same kind of data

#array is 50x fater to calculate than list
#array is homogeous and list is heterogeneius data structure 

#array are stored data in a consicative memory location
#list store data in random place in memory

import numpy as np

a=np.array([1,2,3,4,5])

type(a)

a.ndim

b=np.array([1,10.2,True,'Python'])
b

np.array([[1,2,3],[4,5,6]])

#array creation methods:

x=np.arange(1,50)    
x

y=np.linspace(5,20,50)
y

y=np.linspace(5,20,50,retstep=True)
y

z=np.random.rand(5,2)
z

np.random.randn(5,5)

np.random.random_sample(250)











