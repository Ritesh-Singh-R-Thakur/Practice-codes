# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:19:19 2023

@author: rites
"""
#==========================================

#noramal distribution problem  solving

#===========================================


from scipy.stats import norm

#mean=90kmph sd=10kmph

nd=norm(90,10)

#p(x>100)

z1=1-nd.cdf(100)
z1

#15.86% of cars will be travelling more than 100kmph

nd1=norm(90,5)
z2=1-nd1.cdf(100)
z2

#2.2% of cars will be travelling more than 100kmph

#mean=600 sd=20

nd3=norm(600,20)

#p(600<x<660)
z3=nd3.cdf(660)-nd3.cdf(600)
z3
#p(580-620)
z4=nd3.cdf(620)-nd3.cdf(580)
z4

#====================================================

#Level Of Significance (Alpha=5%)#






























