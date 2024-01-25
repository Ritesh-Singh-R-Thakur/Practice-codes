# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:01:45 2024

@author: rites
"""

#seaborn

import seaborn as sns
import pandas as pd
import numpy as np

df=pd.read_csv('https://raw.githubusercontent.com/aishwaryamate/Datasets/main/cars.csv')
df

df.dtypes

#count plot

sns.countplot(x=df['body-style'])



#pandas





























