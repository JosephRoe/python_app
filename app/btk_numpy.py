import numpy as np

py_list = [1,2,3,4,5,6,7,8,9]


np_array = np.array(py_list)

print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]

np_multi = np_array.reshape(3,3)

print(np_multi)
print(np_array.shape)
print(np_multi.ndim)


