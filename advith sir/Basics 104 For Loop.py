# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:01:03 2023

@author: rites
"""

#For loop

range(1,10)

for i in range(1,10):
    print(i)
  
for i in range(1,11):
    print(i)    
    
#even NUmber    
for i in range(0,11,2): #start,end,jump
    print(i)    
    
    
#odd number    
for i in range(1,11,2):
    print(i)    

age=[22,25,23,21,32,26,27,25,30,19]
#print age above 25
for i in age:
    if i>25:
        print(i)
k1=[]
k2=[]
for i in age:
    if i>25:
        k1.append(i)
    else:
        k2.append(i)

print(k1)
print(k2)
####################################################

salary=[10000,25000,15000,18000,34000,45000,60000]
salaryincre=[]
for i in salary:
    if i>9000:
        salaryincre.append(i+i*.1)

print(salaryincre)        
#############################################
for i in salary:
    j=i*10/100
    salaryincre.append(i+j)
print(salaryincre)    
###########################################





































    