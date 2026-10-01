import numpy as np
filedata = np.genfromtxt('data.txt',delimiter=',')
print(filedata.astype('int32'))
# print(filedata)
