# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:57:43 2024

@author: rites
"""

import pandas as pd
df=pd.read_csv('Cars_100.csv')
df

df['USCARS'].mean()
df['GERMANCARS'].mean()

#Two sample Z-test Pacakage code
from scipy.stats import ttest_ind as TSZtest 
zcal,pval=TSZtest(df['USCARS'],df['GERMANCARS'])

zcal
alpha=0.05
if pval<alpha:
    print('h0 is rejected and h1 is accepted')
else:
    print('ho is accepted and h1 is rejected')

#=====================

df1=pd.read_csv('Lungcapdata.csv')
df1

df1['Gender']
df1["Gender"].value_counts()

male=df1[df1['Gender']=='male']
male
female=df1[df1['Gender']=='female']
female

zcal,pval=TSZtest(male['LungCap'],female['LungCap'])

zcal
alpha=0.05
if pval<alpha:
    print('h0 is rejected and h1 is accepted')
else:
    print('ho is accepted and h1 is rejected')
    
####################################
#Two sample proportion data

import numpy as np 

n1=247 #sample size 1
n2=308
p1=0.37 # proportion state 1
p2=0.39

props=np.array([p1*100,p2*100])
sampsize=np.array([247,308])    

from statsmodels.stats.proportion import proportions_ztest

stats,pval=proportions_ztest(props, sampsize)

alpha=0.05
if pval<alpha:
    print('h0 is rejected and h1 is accepted')
else:
    print('ho is accepted and h1 is rejected')







