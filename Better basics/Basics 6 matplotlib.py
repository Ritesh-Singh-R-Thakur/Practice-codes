# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:05:52 2024

@author: rites
"""

#matplotlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#matplotlib line plot

x=np.linspace(1,20,25)
x

y=np.random.random_sample(25)
y

plt.plot(x,y)#graph is not clear

plt.rcParams['figure.figsize']=(6,3)
plt.rcParams['figure.dpi']=100

plt.plot(x,y)

plt.plot(x,y,color='red',linestyle='--')


df=pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/cars.csv')
df

#histogram

#histogram uses 
""" 1.to check frequency of the data
    2.to find skewness
    3.to find outliers"""
df.head()

df.dtypes

plt.hist(df['width'])

df['width'].skew()                    # -1 to 1 highly skewed
#0.904003498786254                    # -0.5 to 0.5  modereate skewness
#moderate skweness                    # close to zero noraml distribution

df.hist()
plt.tight_layout()

mean=df['width'].mean()
median=df['width'].median()

plt.hist(df['width'],edgecolor='black')
plt.axvline(mean,color='red')
plt.axvline(median,color='green')
plt.title('freaquency graph for width column')













































