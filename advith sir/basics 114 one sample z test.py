# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:48:50 2024

@author: rites
"""

import pandas as pd
import numpy as np
df=pd.read_csv('Lungcapdata.csv')
df

df.head()

df['LungCap']

xbar=df['LungCap'].mean()
xbar
mu=8
sd=df['LungCap'].std()
n=len(df['LungCap'])
rootn=np.sqrt(n)

num=(xbar-mu)
den=(sd/rootn)
zcal=num/den
print('z calcilated value:',zcal.round(3))

#package calculation #one sample package code

from statsmodels.stats import weightstats as onesample

Zcal,pval=onesample.ztest(df['LungCap'],value=8,alternative='smaller')
Zcal,pval

#p value 
alpha=0.05
if pval<alpha:
    print('h0 is rejected and h1 is accepted')
else:
    print('ho is accepted and h1 is rejected')



























