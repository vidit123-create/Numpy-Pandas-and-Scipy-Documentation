#Scipy Documentation
from scipy import linalg
import numpy as np
arr1=np.array([[2,3,5],[4,8,9],[1,4,7]])
print(arr1)
#To find out the determinant
print(linalg.det(arr1))
#tofind permutation matrix,lower diagonal matrix,upper diagonal matrix
arr2=np.array(np.arange(0,9)).reshape(3,3)
print(arr2)
P,L,U=linalg.lu(arr2)
print(P)
print(L)
print(U)
#find out the dot product of the matrix
print(np.dot(P,U))
print(np.dot(P,L))
#find out the cross product of the matrix
print(np.cross(U,L))
print(np.cross(arr2,arr1))
print(np.dot(arr1,arr2))
#find out the eigenvalues and eigenvector
arr3=np.array(np.arange(0,9)).reshape(3,3)
print(arr3)
eigenvalues,eigenvectors=linalg.eig(arr3)
print(eigenvalues)
print(eigenvectors)
#revision of pandas
import pandas as pd
import time
df1=pd.DataFrame([[7,3,4,5],[2,4,9,6]],columns=['A','B','C','D'])
print(df1)
print(time.sleep(5))
print(time.time())
print(df1.sort_values(['A']))
print(df1['B'].head(1))
print(df1['C'].describe())
print(time.time())
#generate random numbers by using random and time module
import random
import time  
a=random.randint(0,25)
print(a)
initial_time=time.time()
print(initial_time)
for i in range(0,a):
    print(i,end=' ')
    final_time=time.time()-initial_time
    print(final_time)

from scipy import linalg
import numpy as np
#Solve two equations
arr4=np.array(np.arange(4,8)).reshape(2,2)
print(arr4)
arr5=np.array(np.arange(0,2)).reshape(2,1)
print(arr5)
print(linalg.solve(arr4,arr5))
from scipy import sparse
print(sparse.lil_matrix((50,50)))
#To do linear algebra or linear matrix calculation by using sparse function and linalg function
from scipy.sparse import linalg
import numpy as np
arr1=np.array(np.arange(4,13)).reshape(3,3)
print(arr1)
arr2=np.array(np.arange(0,9)).reshape(3,3)
print(arr2)
print(linalg.spsolve(arr1,arr2))
#import numpy as np
#x=np.array(np.arange(0,4))
#print(np.exp(x))
#print(np.log(x))
#print(np.std(x))
#print(x.sum())
#To find the integration of some values using python
import scipy.integrate#SINGLE INTEGRAL
#a=lambda x:x**2
#print(scipy.integrate.quad(a,2,4)) 
x=int(input("enter any number"))
y=int(input("enter any number"))
b=lambda z:x**(y**(1/2))
print(scipy.integrate.quad(b,3,6))