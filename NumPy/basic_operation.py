#Accending/changing specific elements, rows,columns, etc.
import numpy as np
a= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#get a specific element
print(a[0,0],a[1,2])
print(a[:,2])

#getting a little more fancy
print(a[0,1:])
print(a[:,1:])
print(a[1,2:4]) #not including 4
print(a[:,2:4])

a[1,5]=20
print(a)

a[:,2]=[1,2]
print(a)


#3-d example
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(b[0,1,1])
print(b[0,1,:])

b[:,1,:]=[[9,9],[8,8]]
print(b)