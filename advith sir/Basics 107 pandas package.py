# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 12:13:51 2023

@author: rites
"""

import pandas as pd

df=pd.read_csv("C:\\Personal\\Data science\\New101\\sir notes\\nyc_weather.csv")
df

df.shape
df.dtypes

df.head()
df.head(8)

df.tail()
df.tail(8)

list(df)
df.columns

#access the columns
df['Temperature']


df['Temperature'].min()
df['Temperature'].max()
df['Temperature'].mean()
df['Temperature'].median()
df['Temperature'].std()
df['Temperature'].var()

df['Temperature'].describe()

df[['Temperature','Humidity']].describe()

#access the columns with their positions

df.columns[[0,2,4]]
df[df.columns[[0,2,4]]]

#drop the columns 
df.drop(df.columns[[0,2,4]],axis=1)

df

#inplace-->remove columns permanently
df.drop(df.columns[[0,2,4]],axis=1,inplace=True)
df















