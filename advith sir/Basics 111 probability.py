# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:22:49 2023

@author: rites
"""

from scipy.stats import binom

bi=binom(n=5,p=0.6)#n,p

#p(x=3),r=3

z1=bi.pmf(3) #r=event
z1
z1.round(3)

#p(x=4)

z2=bi.pmf(4) #r=event
z2
z2.round(3)

#p(x<=2)

z3=bi.pmf(0)+bi.pmf(1)+bi.pmf(2)
z3
z3.round(3)

# or

z3=bi.cdf(2) # p(x<=2)
z3

#at least 3 x>=3

z4=1-bi.cdf(2)
z4

#p=0.70 q=0.30 n=250 r=160
#p(x>=160)
bi1=binom(n=250,p=0.7)
z5=1-bi1.cdf(159)
z5

#####################################
#p=0.8,q=0.2,n=10,p[x=7=r]

bi2=binom(n=10,p=0.8)

z6=bi2.pmf(7) #r=event
z6
z6.round(3)
















































