import numpy as np
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

# after=before.reshape((8,1))
after=before.reshape((2,2,2))
# after=before.reshape((2,3))  #cannot reshape array of size 8 into shape (2,3)
print(after)


#vertically stacking vector
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v2,v2,v2]))

#Horizontal stacking vector
v3=np.array([1,2,3,4])
v4=np.array([5,6,7,8])
print(np.hstack((v3,v4,v4,v4)))

