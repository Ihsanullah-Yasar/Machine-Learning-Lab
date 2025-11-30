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

#------------------------------------------------------------

#KeySeriesAttributesandMethods

#Purpose: To understand the fundamental building block of a Da
#--taFrame. Most operations you learn on a Series apply directly to DataFrame columns.

#Key Takeaway: A Series is a labeled list. Use .iloc for posi
#--tion-based access and [label] for label-based access.

#You can also create a Series from a dictionary.
#The keys become the index, and the values become the data. This is very intuitive.

#Attributes and Methods:

#s3.values: Gets the raw data as a NumPy array [85 92 78].

print("Values of the series:", s3.values) # Underlying NumPy array: [85 92 78]

#s3.index: Gets the index labels Index(['Alice', 'Bob', 'Charlie']).
print("Index of the series:", s3.index) 
# Index object: Index([’Alice’, ’Bob’, ’Charlie’], dtype=’object’)s3.dtype: Shows the data type of the elements (int64).
print("Data type:", s3.dtype) # dtype: int64

#s3['Bob'] or s3.iloc[1]: Accesses elements.
# Access elements by label (index name) or by integer position (like anarray)
print("Value for ’Bob’:", s3['Bob']) # Output: 92 (using label)
print("Value at position 1:", s3.iloc[1]) # Output: 92 (using integer position-.iloc is crucial!)
#CRITICAL DISTINCTION: s3['Bob'] uses the label 'Bob'. s3.iloc[1] uses the integer position 1 (the second element). .iloc is essential for avoiding confusion.

#s3.mean(), s3.max(): These are vectorized operations—they work on the entire series at once,
#much like NumPy, and are very fast.
# Basic descriptive statistics (vectorized, like NumPy)
print("Mean score:", s3.mean()) # Output: 85.0
print("Maximum score:", s3.max()) # Output: 92
print("Standard deviation:", s3.std()) # Output: ~7.0

#-------------------------------------------

#The DataFrame:The Heart of Pandas
#A DataFrameisa2-dimensional labeled data structure.You can think of it as a dictionary of
# Series objects that all share the same index.
 
#CreatingDataFrames

# Most common: From a dictionary of lists/arrays
# Each key becomes a column name, each value becomes the column data.
data = {
'Name': ['Alice', 'Bob', 'Charlie', 'David'],
'Age': [24, 27, 22, 32],
'Score': [88.5, 92.0, 79.5, 96.0],
'Graduated': [True, True, False, True]
}
df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)
print("\nType:", type(df))
# Output:
# Name Age Score Graduated
# 0 Alice 24 88.5 True
# 1 Bob 27 92.0 True
# 2 Charlie 22 79.5 False
# 3 David 32 96.0 True
# <class ’pandas.core.frame.DataFrame’>

# You can specify the row index during creation
df_with_index = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print("\nDataFrame with custom index:")
print(df_with_index)

#   DataFrame with custom index:
#         Name  Age  Score  Graduated
#   a    Alice   24   88.5       True
#   b      Bob   27   92.0       True
#   c  Charlie   22   79.5      False
#   d    David   32   96.0       True


# Create DataFrame from a list of lists (like a 2D array)
# You must specify the column names separately.
 
data_list = [['Alice', 24, 88.5], ['Bob', 27, 92.0], ['Charlie', 22, 79.5]]
df_from_list = pd.DataFrame(data_list, columns=['Name', 'Age', 'Score'])
 
print("\nDataFrame from list of lists:")
 print(df_from_list)









 



