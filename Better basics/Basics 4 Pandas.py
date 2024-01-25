# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 22:23:02 2024

@author: rites
"""

import pandas as pd

#from pc
pd.read_csv(r"C:\Personal\Data science\101New101\All the notes from Advith sir class\sales.csv")#add 'r' before the loacation raw string

#from githup
df=pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/Salaries.csv')

df.head()

df.tail()

df.columns

df.shape

df.ndim

df['rank']

df[['rank','gender','salary']]

df.describe()

df.describe(include=object)

df.describe(include='all')

df.info()

df.dtypes

df.head()

df.loc[30:35]

df.loc[30:35,'service':'salary']

df.iloc[30:35,3:5]#"iloc"=>last number will be missing cannot put column names only indexes

df.dtypes

df.loc[[5,18]] #access single rows

df.loc[[5,18]],[['rank','phd']]

df['rank'].unique()

df['gender'].unique()

df['rank'].nunique()

df['rank'].value_counts()
#===========================Data visuvalization with pandas======================###
df=pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/cars.csv')
df

df.dtypes

#pandads barplot

df['body-style'].value_counts()

df['body-style'].value_counts().plot(kind='bar')

#to see all the frequencies on top of bars

barplot_df=df['body-style'].value_counts().plot(kind='bar')

for i in barplot_df.containers: #for loop
    barplot_df.bar_label(i)

#pandas piechart==>frequency,labels












































































































