import numpy as np
filedata = np.genfromtxt('data.txt',delimiter=',')
print(filedata[filedata>50])


### You can index with a list in NumPy
a=np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])

print(np.any(filedata>30,axis=1))
print(np.all(filedata>30,axis=1))





