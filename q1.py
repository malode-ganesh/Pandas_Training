import numpy as np

# Create a 5×5 2D numPy array and retrieve bottom right corner 2×2 array from it.
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]
                ])

# print(arr[3:,3:]) #bottom right corner 2*2 
# [[19 20]
#  [24 25]]

# top left corner 2*2
# print(arr[0:2, 0:2])
# 9,10,14,15
print(arr[1:3,3:])