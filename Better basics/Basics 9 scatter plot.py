# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:31:44 2024

@author: rites
"""

#scatter plots==>use seaborn for scatterplot
"""cartesian system(x,y)=>are these x & y are related or not"""
""" 3 types of scatter plot
1.positive correlation==>if line in scatter plot is increasing from 0 to infinity
2.negative correlation==>if line in scatter plot is in decreasing from 0 to infinity
3.no correlation==>if data is scttered everywhere"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize']=(8,4)
plt.rcParams['figure.dpi']=100

df=pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/cars.csv')
df

df.dtypes
df.head()

#how engine size and width are related

sns.scatterplot(x=df['engine-size'],y=df['width'])

sns.pairplot(df)#only intger columns

sns.set_style('darkgrid')#to cahange backgroud in the graph
sns.scatterplot(x=df['engine-size'],y=df['price'],hue=df['body-style'])

#how engine size and body style and fuel type affect price of the cars
sns.scatterplot(x=df['engine-size'],y=df['price'],hue=df['body-style'],style=df['fuel-type'])

#3d scatterplot
import plotly.express as pe
import plotly.io as pio
pio.renderers.default='browser'

pe.scatter_3d(data_frame=df,x='width',y='engine-size',z='price',color='body-style')
pe.scatter(data_frame=df,x='width',y='price',color='fuel-type')

























