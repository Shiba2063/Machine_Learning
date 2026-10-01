# #all 0s matrix
import numpy as np
print(np.zeros(5))

print(np.zeros((2,3)))
print(np.zeros((2,3,3)))

#all 1s matrix

print(np.ones(5))
print(np.ones((2,3)))
print(np.ones((2,3,3)))

# for all others number
print(np.full((2,2),88))
print(np.full((2,2,2),99))

#Any others number (full_like)
a= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(np.full_like(a.shape,4))
print(np.full_like(a,4))


#Random decimal number
print(np.random.rand(4,2))
print(np.random.random_sample(a.shape))

#Random integer number
print(np.random.randint(4))
print(np.random.randint(7, size=(3,3)))   
print(np.random.randint(4,7, size=(3,3)))  

#The Identity matrix
print(np.identity(5))

# Repeate an array
arr=np.array([1,2,3])
r1=np.repeat(arr,3)
print(r1)


arr=np.array([1,2,3])
r1=np.repeat(arr,3,axis=0)
print(r1)


copy array
a=np.ones((5,5))
print(a)
b=np.zeros((3,3))
print(b)
b[1,1]=9
print(b)
a[1:4,1:4]=b
print(a)



a=np.array([1,2,3])
b=a
print(b)
b[0]=200
print(b)


#operation on element of array
a=np.array([1,2,3,4])
print(a)

a=a/2
print(a)

a=np.array([1,2,3,4])
a=a*5
print(a)

a=np.array([1,2,3,4])
a=a+5
print(a)

a=np.array([1,2,3,4])
a=a-5
print(a)

a=np.array([1,2,3,4])
b=np.array([1,0,1,0])
c=a+b
print(c)

print(a**2)


#Take sin and cos
print(np.sin(a))
print(np.cos(a))
