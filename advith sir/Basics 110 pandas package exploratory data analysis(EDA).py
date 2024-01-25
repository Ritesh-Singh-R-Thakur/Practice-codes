# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 14:16:19 2023

@author: rites
"""

import pandas as pd

df=pd.read_csv('market_3.csv')
df

df.shape

df.dtypes
df.head()
df.tail()

#Histogram-->numerical
#'Barchar/Piechart-->categorical(Region,Product,Subsidiar)'
#Scatterplot-->numerical
#Boxplot--->numerical

#value_counts-->Number order
df['Region'].value_counts().shape
df['Product'].value_counts().shape
df['Subsidiary'].value_counts().shape

#group by-->Aplbatical order
df.groupby('Region').size()

#adding everything
df.groupby('Region').sum()

df.groupby('Product').sum()

df.groupby('Subsidiary').sum()

#indivisual sum values
t1=df.groupby('Region')['Returns'].sum()
t1
df.groupby('Region')['Inventory'].sum()


df.groupby('Region')['Sales'].sum()

#construction of bar graph
t1=df.groupby('Region')['Returns'].sum()
t1
t1.plot(kind='bar')


t2=df.groupby('Product')['Returns'].sum()
t2
t2.plot(kind='bar')



df_t3=df[(df['Region']=='Africa') | (df['Region']=='Asia') | (df['Region']=='Canada')]

t3=df_t3.groupby('Product')['Returns'].sum()
t3

t3.plot(kind='bar')

#Pie chart
t3.plot(kind='pie')

#Histogram And Skewness

df.dtypes

df['Stores'].hist()
df['Stores'].skew()
df['Stores'].kurt()

df['Sales'].hist()
df['Sales'].skew()

df['Inventory'].hist()
df['Inventory'].skew()

df['Returns'].hist()
df['Returns'].skew()


#Scater Plot
df.dtypes

df.plot.scatter(x='Sales',y='Returns')


df.plot.scatter(x='Sales',y='Inventory')


#matplotlib-->matplot libarary

import matplotlib.pyplot as plt
plt.scatter(x=df['Sales'],y=df['Returns'],color='green')
plt.xlabel('Sales')
plt.ylabel('Returns')
plt.show()

#Correlation-->

df[['Sales','Returns']].corr()
#answer is 0.966123-->(strong positive) because it is more than 0.5

#Boxplot-->to identify the outliers

df1=pd.read_csv('CallCentre.csv')
df1

df1['Calls Rec.'].hist()
df1['Calls Rec.'].skew()

df1['Calls Rec.'].min()
df1['Calls Rec.'].max()
df1['Calls Rec.'].mean()
df1['Calls Rec.'].std()

df1.boxplot(column=['Calls Rec.'],vert=False)

import numpy as np
Q1=np.percentile(df1['Calls Rec.'],25)
Q1

Q3=np.percentile(df1['Calls Rec.'],75)
Q3

IQR=Q3-Q1
IQR

LW=Q1-(1.5*IQR)
UW=Q3+(1.5*IQR)
LW
UW


df1[df1['Calls Rec.']<LW]
df1[df1['Calls Rec.']>UW]
















