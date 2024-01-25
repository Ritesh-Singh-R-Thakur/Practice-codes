# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:02:17 2024

@author: rites
"""

import numpy as np
age=np.array([[22],[25],[28],[32],[36],[40]])
weight=np.array([60,70,78,74,85,80])

import matplotlib.pyplot as plt
plt.scatter(age, weight)
plt.show()

y=weight
x=age

from sklearn.linear_model import LinearRegression
LR=LinearRegression()
LR.fit(x,y)

LR.intercept_
LR.coef_

y_pred=LR.predict(x)

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.scatter(x,y_pred,color='red')
plt.plot(x,y_pred,color='black')
plt.show()

##################################################

import pandas as pd

df=pd.read_csv('Viralcount_Drug.csv')
df
y1=df['Viralcount']
x1=df[['drug']]


#viralcount=y,x=drug

import matplotlib.pyplot as plt
plt.scatter(df['drug'], df['Viralcount'])
 
from sklearn.linear_model import LinearRegression
LR1=LinearRegression()
LR1.fit(x1,y1)

LR1.intercept_
LR1.coef_

y1_pred=LR1.predict(x1)

import matplotlib.pyplot as plt
plt.scatter(x1,y1)
plt.scatter(x1,y1_pred,color='red')
plt.plot(x1,y1_pred,color='black')
plt.show()

from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y1,y1_pred)
mse

print('Root mean square error:',np.sqrt(mse).round(2))

t1=np.array([[20]])
LR1.predict(t1)









