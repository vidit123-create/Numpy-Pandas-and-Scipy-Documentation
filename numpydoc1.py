import numpy as np
import math
arr4=np.array([[math.pi/2,math.pi/3],[math.pi*2,math.pi*3]])
print(arr4)
#Use of trigonometric()
print(np.sin(arr4))
print(np.cos(arr4))
print(np.tan(arr4))
print(np.cos(arr4)**-1)#for sec()
print(np.sin(arr4)**-1)#for cosec()
print(np.tan(arr4)**-1)#for cot()
#Use of round_()
print(np.round_(arr4))
#Use of arange function in numpy
arr5=np.array(np.arange(0,5))
print(arr5)
arr6=np.array(np.arange(0,13))
print(arr6)
arr7=np.array(np.arange(0,17))
print(arr7)
#Use of reshape function in numpy
arr8=np.array(np.arange(0,16).reshape(4,4))
print(arr8)
print(arr8.shape)
#Use of identity function to create identity Matrix
arr2=np.eye(5)
print(arr2)
#To create a matrix with all the elements with zeros
arr3=np.zeros([2,2])
print(arr3)
#To create a matrix with all the elements with ones
arr5=np.ones([3,3])
print(arr5)
#Use of log function
print(np.log(arr4))
#Use of std function
print(np.std(arr4))
#Use of exponential function
print(np.exp(arr4))
#Use of arange function with start,stop index and with step size
arr3=np.array(np.arange(0,17,2).reshape(3,3))
print(arr3)