# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# The standard way to import NumPy. Always use this alias.
import numpy as np

#Purpose: Converts regular Python lists into NumPy arrays.

#Key Difference: Python lists can contain different data types, but NumPy arra--
#--ys must be homogeneous (all elements same type).

#ML Importance: Machine learning algorithms require--
#--numerical data in consistent formats. NumPy arrays provide this structure efficiently.

list_1 = [1, 2, 3, 4, 5]
arr_1d = np.array(list_1)

#==========================================================================

#Special Array Creation Functions

zeros_arr= np.zeros(5) #:: Initialize weights in neural networks
ones_arr= np.ones((2,3)) #: Create bias terms
range_arr= np.arange(0,10,2) #: Generate sequences for testing

linear_arr = np.linspace(0, 100, 5) # Creates 5 numbers from 0 to 100:
[0., 25., 50., 75., 100.]
print("Linear space array:", linear_arr)

# Create an identity matrix (square matrix with 1s on the diagonal and 0s elsewhere).
identity_matrix = np.eye(3) # Creates a 3x3 identity matrix
print("Identity matrix:")
print(identity_matrix)

# Create an array filled with random numbers between 0 and 1.
random_arr = np.random.rand(2, 4) # Creates a 2x4 array of random numbers
print("Random array:")
print(random_arr)

#==========================================================================

#3. Array Attributes

# Creating a 2D array (a matrix) from a list of lists
list_2d = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(list_2d)
print("2D Array:")
print(arr_2d)


#Purpose: Understand the structure of your data.

#ML Context: In machine learning:

#Shape tells you: (number of samples, number of features)

#Data type affects memory usage and computation precision

#Always check these attributes after loading data to avoid dimension mismatches


print("Shape:", arr_2d.shape)      # (2, 3) - dimensions
print("Data Type:", arr_2d.dtype)  # int64 - element type
print("Dimensions:", arr_2d.ndim)  # 2 - number of dimensions
print("Size:", arr_2d.size)        # 6 - total elements

# Let’s use our 2D array from earlier: arr_2d = [[1 2 3], [4 5 6]]
# .shape: Returns a tuple representing the dimensions of the array.
print("Shape of arr_2d:", arr_2d.shape) # Output: (2, 3)-> 2 rows, 3 columns
# .dtype: Returns the data type of the elements in the array.
print("Data Type of elements:", arr_2d.dtype) # Output: int64 (orsimilar, depending on system)
# .ndim: Returns the number of array dimensions (axes).
print("Number of Dimensions (ndim):", arr_2d.ndim) # Output: 2
# .size: Returns the total number of elements in the array.
print("Total Number of Elements (size):", arr_2d.size) # Output: 6

#==========================================================================

#Array Indexing and Slicing

#Purpose: Access specific elements or subsets of data.

#ML Application: Selecting specific features or samples from your dataset.

arr = np.array([10, 20, 30, 40, 50])
print("Element at index 0:", arr[0]) # Output: 10
print("Elements from index 1 to 3 (exclusive):", arr[1:4]) # Output: [20 30 40]
print("Every other element:", arr[::2]) # Output: [10 30 50]
 
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[1, 2])  # 6 (row 1, column 2)


# Get an entire row: array[row_index, :] (The colon ’:’ means "all columns")
print("Entire first row:", arr_2d[0, :]) # Output: [1 2 3] (1st row, allcolumns)

 # Get an entire column: array[:, column_index] (The colon ’:’ means "all rows")
print("Entire second column:", arr_2d[:, 1]) # Output: [2 5 8] (all rows , 2nd column)


# Get a sub-matrix (slicing on both dimensions)
# array[start_row:end_row, start_col:end_col]
# Note: end_row and end_col are exclusive, just like Python list slicing.
print("Sub-matrix (first two rows, last two columns):")
print(arr_2d[0:2, 1:3])
# Output:
# [[2 3]
# [5 6]]

#==========================================================================

#Boolean Indexing

#Purpose: Filter data based on conditions.

#ML Importance: This is crucial for data preprocessing --+
# +--removing outliers, selecting specific classes, or creating subsets.

arr = np.array([5, 10, 15, 20, 25])
filtered = arr[arr > 12]  # [15, 20, 25]

# Step 1: Create a Boolean mask (an array of True/False values)
# based on a condition applied to each element.
filter = arr > 12
print("Boolean mask (arr > 12):", filter) # Output: [False False True True True]
# Step 2: Use this mask to index the original array.
# Only elements where the mask is True are returned.
print("Filtered array using the mask:", arr[filter]) # Output: [15 20 25]
# This is always done in a single, concise line of code.
# This one-liner is what you will use constantly in data analysis.
print("Direct filtering (one-liner):", arr[arr > 12]) # Output: [15 20 25]
# You can use any logical condition
print("Elements less than or equal to 15:", arr[arr <= 15]) # Output: [5 10 15]

#==========================================================================44

#Purpose: Perform operations on entire arrays without loops.

#Performance Benefit: Vectorized operations are 10-100x faster than Python loops.

# ML Context: Machine learning involves massive matrix operations. Vectorizat
# ion makes training practical on large datasets.

arr = np.array([1, 2, 3, 4])
# Basic math with a scalar (applied to every element)
print("arr + 2:", arr + 2) # Output: [3 4 5 6]
print("arr * 10:", arr * 10) # Output: [10 20 30 40]
print("arr ** 2 (squared):", arr ** 2) # Output: [1 4 9 16]
# Math between two arrays of the same shape (element-wise operations)
arr2 = np.array([5, 6, 7, 8])
print("arr + arr2:", arr + arr2) # Output: [ 6 8 10 12]
print("arr * arr2:", arr * arr2) # Output: [ 5 12 21 32]

#==========================================================================

#6. Universal Functions (ufuncs)

#NumPyprovides a large collectionof built-inmathematical functions called Universal---
#Functions(ufuncs).These are also vectorized and operate on entire arrays.

#Purpose: Pre-built mathematical functions that work on entire arrays.

#ML Applications:

#np.mean(): Calculate average loss

#np.std(): Feature standardization

#np.sum(): Aggregation in neural networks
arr = np.array([1, 2, 3, 4])

print("Square root:", np.sqrt(arr))  # [1., 1.414, 1.732, 2.]
print("Mean:", np.mean(arr))         # 2.5
print("Sum:", np.sum(arr))           # 10


# Mathematical functions
print("Square root:", np.sqrt(arr)) # Output: [1. 1.4142... 1.732... 2.]
print("Natural logarithm:", np.log(arr)) # Output: [0. 0.693... 1.0986... 1.3862...]
print("Sine (in radians):", np.sin(arr))

# Statistical aggregation functions (reduce the array to a single value)

print("Mean (average):", np.mean(arr)) # Output: 2.5
print("Sum of all elements:", np.sum(arr)) # Output: 10
print("Standard Deviation:", np.std(arr)) # Output: ~1.118
print("Minimum value:", np.min(arr)) # Output: 1
print("Maximum value:", np.max(arr)) # Output: 4

#==========================================================================

# Reshaping and Combining Arrays
#Data rarely comes in the perfect shape.NumPy provides tools to manipulate the structure of
#our arrays without changing the data itself.

#Purpose: Change array dimensions without changing data.

#ML Importance: Neural networks expect specific input shapes. Resh-
#--aping prepares your data for model input.

 # Create a 1D array with 12 elements
arr = np.arange(12) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Original 1D array:", arr)

# Reshape it into a 3x4 2D array.
# The total size (12) must match the original size.
reshaped_arr = arr.reshape(3, 4)
print("Reshaped to 3x4:")
print(reshaped_arr)
# Output:
# [[ 0 1 2 3]
# [ 4 5 6 7]
# [ 8 9 10 11]]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# Concatenate arrays along an existing axis (default is axis=0, the first axis)
print("Concatenated:", np.concatenate((a, b))) # Output: [1 2 3 4 5 6]

# Stack arrays vertically (along a new row axis)
# This creates a new axis at the beginning, resulting in a 2D array.

print("Vertical stack (vstack):")
print(np.vstack((a, b)))
# Output:
# [[1 2 3]
# [4 5 6]]
# Stack arrays horizontally (along a new column axis)
print("Horizontal stack (hstack):", np.hstack((a, b))) # Output: [1 2 3 4 5 6]

#==========================================================================

#Putting It All Together : A Mini Data Science Project
#Let’s simulate a real-world scenario to see how these concepts work in practice. Imagine you
#have data on exam scores for two classes.

# Simulate some data: 5 students in Class A, 5 in Class B
# Columns: [Student ID, Score, Class (0 for A, 1 for B)]
data = np.array([
[1, 87, 0],
[2, 92, 0],
[3, 78, 0],
[4, 95, 0],
[5, 88, 0],
[6, 81, 1],
[7, 74, 1],
[8, 90, 1],
[9, 85, 1],
[10, 77, 1]
])


print("Raw Data:")
print(data)
print() # Print an empty line for readability
# Let’s do some analysis!
# 1. Extract the score column (all rows, column index 1)
all_scores = data[:, 1]
print("1. All Scores:", all_scores)
# 2. Calculate overall statistics using vectorized functions
print("\n2. Overall Statistics:")
print(" Mean Score:", np.mean(all_scores))
print(" Highest Score:", np.max(all_scores))
print(" Standard Deviation:", np.std(all_scores))
# 3. Compare the two classes using Boolean indexing
# Create a Boolean mask for Class A students
class_a_mask = data[:, 2] == 0 # True for all rows where class is 0
# Apply the mask to get only the scores for Class A
class_a_scores = data[class_a_mask, 1]
print("\n3. Class A Scores:", class_a_scores)
print(" Class A Average:", np.mean(class_a_scores))
# Do the same for Class B in one concise line
class_b_scores = data[data[:, 2] == 1, 1] # Get scores where class column equals 1
print(" Class B Scores:", class_b_scores)
print(" Class B Average:", np.mean(class_b_scores))
# 4. Find all students who scored above 85
# This uses Boolean indexing on the entire 2D array.
high_scorers_mask = data[:, 1] > 85
high_scorers = data[high_scorers_mask] # Gets the full rows for high scorers
print("\n4. High Scorers’ Data (Score > 85):")
print(high_scorers)




















