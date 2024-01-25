# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:23:46 2024

@author: rites
"""

#install the chi-square package

pip install researchpy

#########################################

import pandas as pd

df=pd.read_csv('credit_new.csv')
df

list(df)

df['Cards']
df['Ethnicity']

import researchpy as rp

table,results= rp.crosstab(df['Cards'],df['Ethnicity'],test='chi-square')
#rp.crosstab(df['Cards'],df['Ethnicity']) #table making code
table
results

#chi-square table value for given alpha and degrees of freedom

import scipy.stats as stats
tabval=stats.chi.ppf(q=0.95,df=8)
tabval.round(4)

######################################################
pval=0.0395
alpha=0.05
if pval<alpha:
    print('h0 is rejected and h1 is accepted')
else:
    print('ho is accepted and h1 is rejected')

################################################################



























