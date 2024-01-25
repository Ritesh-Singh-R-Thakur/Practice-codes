# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 10:48:27 2024

@author: rites
"""

#Ftable value

import scipy.stats as ftab
ft=ftab.f(dfn=2,dfd=33)
ft.ppf(0.95).round(4) #5%
#######################################

#ANOVA Codes

import pandas as pd
df=pd.read_csv('Dietplan.csv')
df

from statsmodels.formula.api import ols
anova1=ols('calories~C(Dietplans)',data=df).fit()

import statsmodels.api as sm
table=sm.stats.anova_lm(anova1,type=1) #type 1 ANOVA dataframe
table

pval=0.039441
alpha=0.05
if pval<alpha:
    print('h0 is rejected and h1 is accepted')
else:
    print('ho is accepted and h1 is rejected')
    
########################################################################

df1=pd.read_csv('promots.csv')
df1

from statsmodels.formula.api import ols
anova2=ols('sales~C(promotions)',data=df1).fit()

import statsmodels.api as sm
table1=sm.stats.anova_lm(anova2,type=1) #type 1 ANOVA dataframe
table1

pval=0.000695
alpha=0.05
if pval<alpha:
    print('h0 is rejected and h1 is accepted')
else:
    print('ho is accepted and h1 is rejected')
    
#their is no significance differnce between than
    
#######################################################

df2=pd.read_csv('market_3.csv')
df2

df2['Region'].value_counts()
#1
Canada=df2[df2['Region']=='Canada']
Canada

Canada['Returns'].sum() #71936

#2
Western_Europe=df2[df2['Region']=='Western Europe']
Western_Europe

Western_Europe['Returns'].sum() #169755

#3
Africa=df2[df2['Region']=='Africa']
Africa

Africa['Returns'].sum() #74087

#4
South_America=df2[df2['Region']=='South America']
South_America

South_America['Returns'].sum() #102851

#5
Pacific=df2[df2['Region']=='Pacific']
Pacific

Pacific['Returns'].sum() #77129

#6
United_States=df2[df2['Region']=='United States']
United_States

United_States['Returns'].sum() #187502

#7
Central_America_Caribbean=df2[df2['Region']=='Central America/Caribbean']
Central_America_Caribbean

Central_America_Caribbean['Returns'].sum() #106893

#8
Eastern_Europe =df2[df2['Region']=='Eastern Europe']
Eastern_Europe 

Eastern_Europe['Returns'].sum() #86701

#9
Middle_East=df2[df2['Region']=='Middle East']
Middle_East

Middle_East['Returns'].sum() #149518

#10
Asia=df2[df2['Region']=='Asia']
Africa

Asia['Returns'].sum() #10895

#OR Easy use groupby function

total_region=df2.groupby('Region').sum()
total_region

total_region['Returns']












