# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:41:38 2019

@author: hossein.mortazavi
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
# %matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6


data = pd.read_csv('AirPassengers.csv')
print(data.head())
print ('\n Data Types:')
print (data.dtypes)

print('test')
