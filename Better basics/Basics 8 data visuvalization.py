# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:39:32 2024

@author: rites
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import warnings#to remove unnecessary warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/cars.csv')
df


df=pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/cars.csv')
df

df.dtypes

#count plot seaborn

sns.countplot(x=df['body-style'])

sns.countplot(x=df['make'])#x-axis names are not visible properly

sns.countplot(y=df['make'])#get the names on y-axis

sns.countplot(x=df['make'])
plt.xticks(rotation=90)
plt.show()

#pandas

#pandads barplot

df['body-style'].value_counts()

df['body-style'].value_counts().plot(kind='bar')

#to see all the frequencies on top of bars

barplot_df=df['body-style'].value_counts().plot(kind='bar')

for i in barplot_df.containers: #for loop
    barplot_df.bar_label(i)

#matplotlib piechart==>frequency,labels(use pandas for pie chart)

a=[20,30,25,36]
b=['a','b','c','d']

plt.pie(a, labels=b,autopct='%0.2f')
plt.show()

plt.pie(a, labels=b,autopct='%0f%%')
plt.show()


#To get labels make a list
df['body-style'].value_counts()

names=['sedan','hatchback','wagon','hardtop','convertible']

plt.pie(df['body-style'].value_counts(),labels=names,autopct='%0.0f%%')

#pandas piechart==>pandas pie chart is better
df['body-style'].value_counts().plot(kind='pie',autopct='%0.0f%%')

#seaborn code change theme and color of all graphs running after this code 
sns.set_theme(style='darkgrid',palette='turbo_r')

#plotly library
import plotly.io as pio
import plotly.express as pe 
pio.renderers.default='browser'#to see graph in my browser

df.dtypes

pe.histogram(df['width'])

pe.histogram(df['height'])























































































