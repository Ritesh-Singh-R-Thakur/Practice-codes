# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:58:45 2023

@author: rites
"""


#NUMPY-->numerical python

import numpy as np

#create a array-->array is like vector in same direction

x1=np.array([24,28,36,42])
x1

x2=np.array([[24,170],[28,168],[36,174],[42,171]])
x2
x2.shape

x3=np.array([[24,170,75],[28,168,70],[36,174,80],[42,171,85]])
x3
x3.shape

#access the rows and columns
x3[:,:]
 
x3[:,0:2]

x3[0:2,0:2]

x3[:,0:1]
#calculating mean

np.mean(x3[:,0:1])
np.median(x3[:,0:1])
np.std(x3[:,0:1])
np.var(x3[:,0:1])
np.min(x3[:,0:1])
np.max(x3[:,0:1])

#===================================

x4=np.random.randint(10,100,size=10)
x4


x5=np.random.randint(10,100,size=(3,5))
x5

x5.shape






