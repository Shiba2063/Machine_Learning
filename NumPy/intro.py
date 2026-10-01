# NumPy (Numerical Python) is an open source Python library that’s widely used in science and engineering.

#How to import NumPy
import numpy as np

a = np.array([1, 2, 3])
print(a)

b=np.array([[1,2,3],[4,5,6]])

print(b)

#Dimension
print(a.ndim)
print(b.ndim)

#Shape
print(a.shape)
print(b.shape)

#Datatype
print(a.dtype)
print(b.dtype)

#Size
print(a.itemsize)
print(b.itemsize)

#otal size
print(a.nbytes)
print(b.nbytes)
