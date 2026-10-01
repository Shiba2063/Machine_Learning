import numpy as np
a=np.ones((2,3))
print(a)

b=np.full((3,2),2)
print(b)

# print(a*b)  # Wrong

print(np.matmul(a,b))  #multiply two matrix

# Find the determinant
c=np.identity(3)
print(np.linalg.det(c))

