# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:12:20 2024

@author: rites
"""

import pandas as pd
from scipy.stats import norm
import numpy as np

df=pd.read_csv('Lungcapdata.csv')
df
df.shape
list(df)

df['LungCap'].mean()

#confidence interval-->90% confident population mean will lie below interval
df_ci=norm.interval(0.90,loc=df['LungCap'].mean(),scale=df['LungCap'].std())
print('90% confidence interval is',np.round(df_ci,4))


#confidence interval-->95% confident population mean will lie below interval
df_ci=norm.interval(0.95,loc=df['LungCap'].mean(),scale=df['LungCap'].std())
print('90% confidence interval is',np.round(df_ci,4))



#confidence interval-->99% confident population mean will lie below interval
df_ci=norm.interval(0.99,loc=df['LungCap'].mean(),scale=df['LungCap'].std())
print('90% confidence interval is',np.round(df_ci,4))










