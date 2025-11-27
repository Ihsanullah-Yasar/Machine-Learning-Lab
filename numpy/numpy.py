# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# The standard way to import NumPy. Always use this alias.
import numpy as np

#Purpose: Converts regular Python lists into NumPy arrays.

#Key Difference: Python lists can contain different data types, but NumPy arrays must be homogeneous (all elements same type).

#ML Importance: Machine learning algorithms require--
#--numerical data in consistent formats. NumPy arrays provide this structure efficiently.

list_1 = [1, 2, 3, 4, 5]
arr_1d = np.array(list_1)

#Special Array Creation Functions

zeros_arr= np.zeros(5) #:: Initialize weights in neural networks
ones_arr= np.ones((2,3)) #: Create bias terms
range_arr= np.arange(0,10,2) #: Generate sequences for testing

#3. Array Attributes

# Creating a 2D array (a matrix) from a list of lists
list_2d = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(list_2d)
print("2D Array:")
print(arr_2d)

































