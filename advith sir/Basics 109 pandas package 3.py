# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:16:29 2023

@author: rites
"""

import pandas as pd
import numpy as np

d1={'ID':[1,2,3,4,5],
    'Age':[24,25,26,np.nan,30],
    'Height':[170,np.nan,172,180,166],
    'weight':[70,78,82,76,90]}

d1
df=pd.DataFrame(d1)
df



df.isnull().sum()

#how to remove the blanks
df.dropna(axis=0)
df

df_wb=df.dropna(axis=0)#blank rows removal
df_wb


df_col=df.dropna(axis=1)#blank column removal
df_col

#replace blanks with mean or median

df

df['Age'].mean()

df['Age']=df['Age'].fillna(value=df['Age'].mean())

df['Height']=df['Height'].fillna(value=df['Height'].mean())

df
#####################

d2={'ID':[6,7,8,9,10],
    'Age':[24,25,26,45,30],
    'Height':[170,181,172,180,166],
    'weight':[70,78,82,76,90]}

df2=pd.DataFrame(d2)
df2

#add 2 data set (veriable should be same)

df3=pd.concat([df,df2])
df3

df3=pd.concat([df,df2],ignore_index=True)
df3


d3={'Id':[1,2,3,4,5,6,7,8,9,10],
    'BP':[110,120,115,125,145,130,132,142,117,121]}
df4=pd.DataFrame(d3)
df4

#add new column #concatinating vertically 
df5=pd.concat([df3,df4],axis=1)
df5

#find and remove duplicates column

df6=df5.T.drop_duplicates().T
df6

d3={'ID':[1,2,2,4,5],
    'Age':[24,25,25,32,30],
    'Height':[170,172,172,180,166],
    'weight':[70,78,78,76,90]}


df7=pd.DataFrame(d3)
df7

df7.drop_duplicates()

df7.drop_duplicates(inplace=True,ignore_index=True)
df7

#sorting and ordering a dataframe

df7.sort_values(by='Age',inplace=True)
df7













