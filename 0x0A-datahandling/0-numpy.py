# a program that uses numpy library

import numpy as np

a = np.arange(4)
print(a)
# print(a[2])

b = np.array([1, 2, 3, 4])
c = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(a + b)
zeros = np.zeros((3,4))
ones = np.ones((2,2))
range_arr = np.arange(0,11,2)
random_arr = np.random.rand(3,3)
print(zeros)
print(ones)
print(range_arr)
print(random_arr)

print(b.shape)
print(c.shape)
print(c.ndim)
print(c.dtype)
print(c.size)