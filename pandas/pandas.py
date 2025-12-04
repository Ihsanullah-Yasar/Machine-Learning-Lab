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

#Understanding Data Frame Structure

# .head() and .tail() show the first/last n rows (default n=5)
print("First 2 rows:")
print(df.head(2))
# Output:
# Name Age Score Graduated
# 0 Alice 24 88.5 True
# 1 Bob 27 92.0 True

print("\nLast 2 rows:")
print(df.tail(2))


# .info() provides a concise summary of the DataFrame
# This is one of the MOST USEFUL methods for understanding your data.
print("\nDataFrame Info:")
print(df.info())
# Output:
# <class ’pandas.core.frame.DataFrame’>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 4 columns):
# # Column Non-Null Count Dtype
#---------------------------
# 0 Name 4 non-null object
# 1 Age 4 non-null int64
# 2 Score 4 non-null float64
# 3 Graduated 4 non-null bool
# dtypes: bool(1), float64(1),
# memory usage: 198.0+ bytes

# .describe() generates descriptive statistics for numerical columns
print("\nDescriptive Statistics:")
print(df.describe())
# Output:
# Age Score
# count 4.000000 4.000000
# mean 26.250000 89.000000
# std 4.349329 7.098965
# min 22.000000 79.500000
# 25% 23.500000 85.125000
# 50% 25.500000 90.250000
# 75% 28.250000 92.750000
# max 32.000000 96.000000

# Access the underlying NumPy array
print("\nNumPy representation:")
print(df.values)
# Output:
# [[’Alice’ 24 88.5 True]
# [’Bob’ 27 92.0 True]
# [’Charlie’ 22 79.5 False]
# [’David’ 32 96.0 True]]



#Data Access and Indexing in DataFrames
#Accessing data in a DataFrame is versatile but requires understanding a few key methods to
#avoid confusion: [], .loc[] , and .iloc[]. 



# Select a single column-> Returns a Series
age_series = df['Age']
print("Age Column (Series):")
print(age_series)
print("Type:", type(age_series))
# Output:
# 0 24
# 1 27
# 2 22
# 3 32
# Name: Age, dtype: int64
# <class ’pandas.core.series.Series’>


# Select multiple columns-> Returns a DataFrame
subset_df = df[['Name', 'Score']] # Note the double brackets
print("\nSubset DataFrame (Name and Score):")
print(subset_df)
print("Type:", type(subset_df))
# Output:
# Name Score
# 0 Alice 88.5
# 1 Bob 92.0
# 2 Charlie 79.5
# 3 David 96.0
# <class ’pandas.core.frame.DataFrame’>


# Create a new column through assignment
df['Passed'] = df['Score'] > 85 # Creates a Boolean column
print("\nDataFrame with new ’Passed’ column:")
print(df)

#Selecting Rows: .loc[] and .iloc[]
#This is a critical concept. Pandas provides two primary indexers for selecting rows and columns
#by label or by integer position.


# .loc[] is primarily LABEL-BASED indexing.
# Syntax: df.loc[row_labels, column_labels]
# Select a single row by its index label-> Returns a Series
row_0 = df.loc[0] # Get row with index label ’0’
print("Row 0 (using .loc):")
print(row_0)
print("Type:", type(row_0))


# Select specific rows and columns by their labels
subset_loc = df.loc[[0, 2], ['Name', 'Age']] # Rows 0 & 2, Columns ’Name’ & ’Age’
print("\nSubset using .loc:")
print(subset_loc)


# .iloc[] is primarily INTEGER POSITION-BASED indexing.
# Syntax: df.iloc[row_positions, column_positions]
# It works just like indexing a NumPy array.
# Select the first row (position 0)
row_0_iloc = df.iloc[0] # Get row at integer position 0
print("\nRow 0 (using .iloc):")
print(row_0_iloc)


# Select specific rows and columns by their integer positions
# df.iloc[[row_start:row_stop], [col_start:col_stop]]
subset_iloc = df.iloc[1:3, 0:2] # Rows at position 1 to 2 (exclusive of 3), Columns at position 0 to 1 (exclusive of 2)
print("\nSubset using .iloc (rows 1-2, cols 0-1):")
print(subset_iloc)
# Output:
# Name Age
# 1 Bob 27
# 2 Charlie 22


# Selecting a single value (scalar)
# Get the value at the intersection of row label 2 and column ’Score’
value_loc = df.loc[2, 'Score'] # Output: 79.5
# Get the value at the intersection of row position 2 and column position 2
value_iloc = df.iloc[2, 2] # Output: 79.5
print(f"\nValue using .loc: {value_loc}, Value using .iloc: {value_iloc}")



# Filtering Data(Boolean Indexing)
# Just like in NumPy, you can filter DataFrames using Boolean conditions. This is one of the
# most common operations in data analysis

# Create a Boolean Series based on a condition
high_score_mask = df['Score'] > 90
print("Boolean Mask (Score > 90):")
print(high_score_mask)
# Output:
# 0 False
# 1 True
# 2 False
# 3 True
# Name: Score, dtype: bool


# Use the Boolean mask to filter the DataFrame
# This returns only the rows where the condition is True.
high_scorers_df = df[high_score_mask]
print("\nStudents with score > 90:")
print(high_scorers_df)
# Output:
# Name Age Score Graduated Passed
# 1 Bob 27 92.0 True True
# 3 David 32 96.0 True True
# The most common way is to write the condition directly inside the brackets
graduates_df = df[df['Graduated'] == True]
print("\nStudents who have graduated:")
print(graduates_df)

# You can combine conditions using & (AND), | (OR), and ~ (NOT)
# IMPORTANT: You MUST wrap each condition in parentheses.
young_graduates_df = df[(df['Age'] < 30) & (df['Graduated'] == True)]
print("\nYoung graduates (Age < 30 AND Graduated):")
print(young_graduates_df)

high_score_or_young = df[(df['Score'] > 90) | (df['Age'] < 25)]
print("\nHigh scorers OR young students:")
print(high_score_or_young)



#Handling Missing Data
#Real-world data is messy and often has missing values.Pandas represents missing data as ‘NaN‘
#( Not a Number) and provides tools to handle it.


























 



