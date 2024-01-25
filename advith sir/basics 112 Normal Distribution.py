# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:29:30 2023

@author: rites
"""

from scipy.stats import norm
nd= norm(170,10) #mean=170 sd=10

#p(x<170)
x1=nd.cdf(170)
x1

#p(x>170)
x2=1-x1
x2

#p[140<x<180]=P[x<180]-p[x<140]

x3=nd.cdf(180)-nd.cdf(140)
x3

#----------------------------------------

#mean=500hr sd=100h

nd1=norm(500,100)

#p(500<=x<=650)
x4=nd1.cdf(650)-nd1.cdf(500)
x4
#there is 43% chance that people could have completed the traing program between 500 to 650 hours

#p(x<=580)
x5=nd1.cdf(580)
x5

#mean=29million sd=5million noram dis

nd2=norm(29,5) 

#p(x>=23) atleat 23 million means 23 million and more that 23 mllion

x6=1-nd2.cdf(23)
x6

#p(30<x<34)
x7=nd2.cdf(34)-nd2.cdf(30)
x7

#p(x>40)
x8=1-nd2.cdf(40)
x8

#############
#home work#
 
#mean=$50,000 sd=$10,000
nd3=norm(50000,10000)

#p(x<40000)
x9=nd3.cdf(40000)
x9
#15.8% people earn less than 40000$


#p(45000<x<65000)
x10=nd3.cdf(65000)-nd3.cdf(45000)
x10
#62.4% people earn between 45000 to 65000

#p(x>70000)
x11=1-nd3.cdf(70000)
x11
#2.2% people earn more than 70000$




































































