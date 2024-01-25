# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:51:48 2024

@author: rites
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize']=(10,4)
plt.rcParams['figure.dpi']=100

df=pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/cars.csv')
df

df.dtypes

#univariate graphs{one column graph}
""" 1.histogram
    2.barplot
    3.piechart
    4.boxplot"""
    
#bivariate graphs{requires two columns} 
""" 1.scatterplot """   

df.describe()

pd.set_option('display.max_colwidth',7)

#matplotlib boxplot

plt.boxplot(df['engine-size'])

plt.boxplot(df['engine-size'],vert=False)

plt.boxplot(df['engine-size'],vert=False,notch=True)

plt.boxplot(df['engine-size'],vert=False,notch=True,showmeans=True)

plt.boxplot(df['engine-size'],vert=False,notch=True,showmeans=True,patch_artist=True)

#see all the boxplots at one time

df.boxplot()

plt.boxplot(df['width'])

#seaborn boxplot

df.dtypes

sns.boxplot(df['highway-mpg'],orient='h')

sns.set_theme(style='darkgrid',palette='turbo_r')

sns.boxplot(df['highway-mpg'],orient='h')

sns.boxplot(df['price'],orient='h')

df[df['price']>30000]

sns.boxplot(x=df['price'],y=df['make'])

#plotly boxplot
import plotly.express as pe
import plotly.io as pio
pio.renderers.default='browser'
pe.box(data_frame=df,x='price',y='make')









































































































































