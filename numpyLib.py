import numpy as np
import matplotlib.pyplot as plt
import sys
import time

arr=np.array([(1,2,3),(4,5,6)])
brr=np.array([(1,2,3),(4,5,6)])

print(arr)
print("dimension: ",arr.ndim) #to print the dimension of the numpy array
print(arr.itemsize) #to print each element size
print(arr.dtype) #to print the datatype
print(arr.size) #total number of element int the array
print(arr.shape) #shape of the array
arr=arr.reshape(3,2) #reshape the array to 3 rows 2 columns
print(arr)
print("slicing: ",arr[1:3,1]) #take row frorm 1 to 2 and column 1
print(np.linspace(1,4,6)) #print 6 element between 1 to 4

print(arr.max())
print(arr.sum())
print(np.sqrt(arr))
print(np.std(arr))
print(arr+brr)
# print(np.vstack(arr,brr))
# print(np.hstack(arr,brr))

# print(arr.ravel())
