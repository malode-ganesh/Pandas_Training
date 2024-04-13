import numpy as np

arr = np.array([
    [1, 2],
    [3, 4]
])
np.save('myArr.npy', arr)

# load 
loadArr =np.load('myArr.npy')
# print(loadArr)