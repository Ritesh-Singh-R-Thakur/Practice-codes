# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:11:57 2024

@author: rites
"""

#pandas filtering and groupby

import pandas as pd

#from githup
df=pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/Salaries.csv')

df.head()

df['gender']=='Female'

df[df['gender']=='Female']

df['gender']=='Female'
df['salary']>150000

df[(df['gender']=='Female') & (df['salary']>150000)]#&=and

df[(df['gender']=='Female') | (df['salary']>150000)]# | =or

df.head()

df[df['rank']=='Prof']['salary']

df[df['rank']=='Prof']['salary'].mean()

df[(df['rank']=='Prof') & (df['gender']=='Male')]['salary'].mean()

df[(df['rank']=='Prof') & (df['gender']=='Female')]['salary'].mean()

#groupby fuction

df.groupby('rank')['salary'].mean()

df.groupby('gender')['salary'].mean()

df.groupby('rank')['salary'].agg({'mean','median','min','max','std'})

###########home work##########
df1=pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/nba.csv')
df1

df1.head()
df1.dtypes

#1
df1['Team']=='Boston Celtics'
df1['Weight']<100

df1[(df1['Team']=='Boston Celtics')&(df1['Weight']<100)]

#2

df1['Team'].unique()

df1[df1['Team']=='Los Angeles Lakers']['Salary'].mean()

#3
df1['Position'].value_counts()
df1['Position'].unique()
df1.groupby('Position')['Salary'].mean().round(3)

#4
df1['College'].unique()
df1[df1['College']=='San Diego State']
#Kawhi Leonard

#5
df1['Team'].unique()
df1[df1['Team']=='Toronto Raptors']['Salary'].max()
df1['Name']
df1['Salary'].max()


df1[(df1['Team']=='Toronto Raptors')&(df1['Salary']==13600000.0)]
#DeMarre Carroll











































