# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:16:44 2023

@author: rites
"""

#lists--->we can put many values and differnt data types in one object

L1 = []

L1 = [10,20,30,72.3,'cat',True]
L1


len(L1)

#access the value
L1[0]
L1[3]
L1[4]
L1[4]=75 #modify the value
L1

L1[-1]
L1[-2]

L1.pop() #by default it removes last value
L1

L1.pop(3) #if we pass number inside brackets,it will remove
L1

L1.append(80) # add the value at the last position
L1

sum(L1)
avg=sum(L1)/len(L1)
avg

L2=[3,5,7,9,[2,4,6,8],11,13]
L2[0]

L2[4][0]


L3=[45,23,65,14,15,77,19,24]
L3.sort()#assending order
L3
L3.sort(reverse=True)
L3

#tuples-->we cannot modify,we cannot remove or add


T1 = ()
T1= (10,20,30,40,50)
T1

T1[0]=12 # you cannot modify


T2=list(T1) #change tuples to list
T2

#dictionary-->keys and values

d1 = {'Hyd':1,'Banglore':2,'pune':3}
d1.keys()
d1.values()
d2={'ID':[1,2,3,4],'Salary':[10000,20000,25000,30000],'Exp':[2,4,6,8]}
d2.keys()
d2.values()

d2['ID']
#=====================================================================




























