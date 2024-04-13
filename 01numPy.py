import numpy as np

list = [[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]]
r = np.array(list)
# print(r.ndim)
# print(r[0,3,2]) #5
# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Transpose the array
transposed_arr = np.transpose(arr) #converts rows to columns i.e Transpose
# print(transposed_arr.ndim) 
# Array universal functions
# print(np.sqrt(arr))
arr2 = np.array([
    [1,2,3],
    [4,5,6],
])
arr3 = np.array([
    [1,2,3],
    [4,5,6],
])
# print(arr2.ndim)
# print(np.add(arr2 , arr3))
# sum()
print(np.sum(arr2))