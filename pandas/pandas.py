# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 14:00:32 2025

@author: ihsan
"""
import pandas as pd

data_list= [10,20,30,40]

s1= pd.Series(data_list)

print("Series from list(default index): ")
print(s1)

print ("Type:", type(s1))

# Output:
# 0 10
# 1 20
# 2 30
# 3 40
# dtype: int64
# <class ’pandas.core.series.Series’>

custom_index= ['a','b','c','d']

s2= pd.Series(data_list, index=custom_index)

print("\nSeries with custom index:")
print(s2)
# Output:
# a 10
# b 20
# c 30
# d 40
# dtype: int64

# Create a Series from a Python dictionary.
# The dictionary KEYS become the Series INDEX.
data_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
s3 = pd.Series(data_dict)
print("\nSeries from dictionary:")
print(s3)
# Output:
# Alice 85
# Bob 92
# Charlie 78
# dtype: int64
 



