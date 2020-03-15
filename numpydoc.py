import numpy as np
#Print Version
print("Version of numpy is",np.__version__)
#Creating Array
arr1=np.array([[6,9,0,3],[3,6,8,2],[2,7,9,1]])
print(arr1)
#Indexing
print("elements at this index is",arr1[[1],[3]])
print(arr1[[0],[1]])
#Slicing
print(arr1[0:1,1:2])
print(arr1[1:2,2:3])
#Operation using Slicing
print(arr1[1:2,2:3]+arr1[2:,[2]])
print(arr1[1:2,2:3]-arr1[2:,[2]])
print(arr1[1:2,2:3]*arr1[2:,[2]])
print(arr1[1:2,2:3]/arr1[2:,[2]])
print(arr1[1:2,2:3]**arr1[2:,[2]])
print(arr1[1:2,2:3]**2)
print(arr1[1:2,2:3]**(1/2))
#Slicing and Indexing both with negative index
print(arr1[[-1],[-2]])
print(arr1[[-1],[-1]])
#Slicing using Single array
arr2=np.array([["Aman","Ankit","Shivam","Rishabh"]])
print(arr2)
print(arr2[[-1],[-2]])
#Use of sum()
print(arr2.sum())
print(arr1.sum())
#To find Datatype of an Matrix in numpy
print(arr1.dtype)
print(arr2.dtype)
#Properities in dtype function
print(arr2.dtype.byteorder)
print(arr2.dtype.itemsize)
#Math operation in numpy
arr3=np.array([[2,4,6,8],[1,3,6,4],[3,6,2,7]])
print(arr3)
#Use of add() using Math operation
print(np.add(arr1,arr3))
print(sum(arr1,arr3))
print(arr3.sum())
#Use of Sqrt()
print(np.sqrt(arr1))
print(np.sqrt(arr3))
#Use of 'T'()
print(arr1.T)
print(arr3.T)