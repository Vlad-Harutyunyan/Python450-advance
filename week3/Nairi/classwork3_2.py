import numpy as np
import sys

a = np.zeros((2,2))
print(a)
a1 = np.ones((1,2))
print(a1)
a2 = np.eye(2)
print(a2)
a3 = np.random.random((2,2))
print(a3)

# indexation

a4 = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(a4)
print(a4[:2,1:3])
a5 = np.array([[1,2,3,4,5],[1,2,31,2,4],[13,6,443,2,3]])
print(a5[[0,1,2],[0,1,2]])
print(a5[a5>5])
# + - / * if arrays length equal  for 2 or more numpy arrays
print(np.sqrt(a5))
b1 = np.array([1,2,3])
b2 = np.array([1,2,3])
print(b1.dot(b2))
print(a4.T) # row to colum colum to row
print(np.sum(b1))

print(np.zeros_like(a4))
print(np.reshape(a5,(3,5)))



print(sys.getsizeof([]))
print(sys.getsizeof(np.array([])))


print(sys.getsizeof([1,2,3,4,12,21,12,21,12,211,21,2,1,1,1,1])) #every element 8 bytes
print(sys.getsizeof(np.array([1,2,3,42,2,5,5,3,23,2,23,1,1,1,1]))) #every element 4 bytes



x = np.array([1,2,3])

print(x.__array_interface__['data'][0])

y = x[1:]
print(y.__array_interface__['data'][0])

# in array every element close to another 