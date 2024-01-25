# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 10:51:34 2023

@author: rites
"""

import pandas as pd

df=pd.read_csv('nyc_weather.csv')
df

df.dtypes

#checking blanks in the data

df.isnull()

#how many null value a column contains
df.isnull().sum()

df['Events']

#if the variable is categorical-- use counts

df['Events'].value_counts()

#filter the data
df['Events']=='Rain'

df[df['Events']=='Rain']

df_rain=df[df['Events']=='Rain']

df_rain


df[(df['Events']=='Rain') & (df['Temperature']>45)]

#renaming the columns

df.columns

#create dictionary
d1={'Sea Level PressureIn':'SLP',
    'WindSpeedMPH':'WSM',
    'WindDirDegrees':'WDD'}

df.rename(columns=d1)#-->temprary change

df.rename(columns=d1,inplace=True)#-->permanent change

df.columns






















