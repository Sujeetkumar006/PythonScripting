# Numpy

import numpy,
import numpy as np, 
from numpy import *

#Arrays : Arrays are similar to lists in Python, except that every element of an array must be of the same type, typically a numeric type like float or int.  Arrays make operations with large amounts of numeric data very fast and are generally much more efficient than lists. 

#===================================================================
#It creates an ndarray from any object exposing array interface
#darray : numpy.array 
#numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
#===================================================================

"""object : Any object exposing the array interface method returns an array, or any (nested) sequence like for example List.
dtype : Desired data type of array, optional 
copy : Optional. By default (true), the object is copied 
order : C (row major) or F (column major) or A (any) (default) 
subok : By default, returned array forced to be a base class array. If true, sub-classes passed through 
ndimin : Specifies minimum dimensions of resultant array """

## Data Types: 
#bool_ Boolean ,int_ Default ,intc , intp ,int8 ,int16 ,int32 , int64 , uint8 ,uint16 , uint32 ,uint64 , float_ ,float16 ,float32 , float64 ,complex_ ,complex64 ,Complex number, ,complex128 ,Complex number, ,

#object : Any object exposing the array interface method returns an array, or any (nested) sequence like for example List.
#dtype : Desired data type of array, optional
#copy : Optional. By default (true), the object is copied
#order : C (row major) or F (column major) or A (any) (default)
#subok : By default, returned array forced to be a base class array. If true, sub-classes passed through
#ndimin : Specifies minimum dimensions of resultant array

import numpy as np

l= [1, 4, 5, 8]
a = np.array(l) 
print(type(a)) 
a

## Array elements are accessed, sliced, and manipulated just like lists
print (a[0:2])
print(a[3])

## Multidimensional Array:
# Two DImensional
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[0,0])
print(a[0])
print(a[1,0])
print(a)
print ('****************')
# THree Dimesnional
a = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(a[0,0,0])
print(a[0,1])
print(a[1,0])
print(a[1])
print(a)

## Shape : It gives a tuple with the size of each array dimension in reverse manner (ROw first, coulmns next: 3rd Dimesion -2nd Dimension: 1st Dimension):
a.shape

## Array Should always be of same dimesion , if the dimension mismatch it will become list as ab in below:

a = np.array([[1, 2,3], [4, 5, 6]])
ab= np.array([[1, 2], [4, 5, 6]])
print(a)
print(ab)
print(a.shape)
print(ab.shape)

## dtype : type of values

a.dtype 

## len : returns the length of the first axis:

import numpy as np
a = np.array([[1, 2,3], [4, 5, 6]])
abc = np.array([[1, 2,3], [4, 5, 6],[1, 2,3]])
print(len(a))
len(abc)

## in : to check if the value is present in the array

x= [1,2,3] in a
y= 1 in a
print(x,y)

## range(x): to create value for range
a = np.array(range(10), float) 
print(a)

## reshape: Reshape or redimension of the array
import numpy as np
a = np.array(range(12), float) 
print(a)
a = a.reshape((12, 1))
print(a)

# reshape with -1 : deafult reshape
import numpy as np
a = np.array(range(12), float) 
print(a)
a = a.reshape((12, 1))
a1 = a.reshape((3, -1))
a2 = a.reshape((-1, 3))
print(a.ndim)
print(a1.ndim)
print(a2.ndim)
print(a.shape)
print(a1.shape)
print(a2.shape)



# initalize numpy array from nested python list.
a1=[1,2,3]
a2=[4,5,6]
a3=[7,8,9]
a = np.array([a1,a2,a3])
print(a)

# reshape using shape:
a = np.array([a1,a2])
print(a.shape)
print(a)
a.shape=(3,2)
print(a)


## arange: Range method in array which directly return array instead of list
#arrange(start,end,step) 
a= np.arange(1, 30, 3, dtype=int) 
print(a)

# itemSize:
a= np.arange(1, 30, 3, dtype=np.int8) 
print(a.itemsize)
a= np.arange(1, 30, 3, dtype=np.float) 
print(a.itemsize)


## copy : To copy a array from one to another 
a = np.array([1, 2, 3], float) 
b = a 
c = a.copy() 
print(a)
print(b)
print(c)
a[0]=6
print(a)
print(b)
print(c)

## tolist: An array can be converted to list
a = np.array([[1, 2, 3, 4], [1, 2, 3, 4]]) 
a=a.tolist()
print(a)
type(a)

## fill: TO fill the complete array with given value
a = np.array([1, 2, 3])
print(a)
a.fill(0)
print(a)

## flatten: TO make multi dimensional array as one dimension
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
a=a.flatten()
print(a)

## concatenate : TO concatenate or joing multiple arrays of one dimesion or multi dimension. 
a = np.array([1,2]) 
b = np.array([3,4,5,6]) 
c = np.array([7,8,9]) 
d= np.concatenate((a, b, c))
print(d)
a = np.array([[1, 2], [3, 4]], float)
b = np.array([[5, 6], [7,8]], float) 
c= np.concatenate((a,b)) # Default concatenate on axis 0. 
print('\n',c)
d= np.concatenate((a,b), axis=0)
print("After concat")
print('\n',d)
e= np.concatenate((a,b), axis=1) 
print('\n',e)


## Array mathematics: One Dimensioal
## arrays should always be of the same size during addition, subtraction, Multiplication or division

a = np.array([1,2]) 
b = np.array([4,5,6])   
print(a+b) 

a = np.array([1,2,3]) 
b = np.array([4,5,6])   
print(a+b) ## 1+4, 2+5, 3+6
print(a-b) ## 1-4, 2-5, 3-6
print(a*b) ## 1*4, 2*5, 3*6
print(a/b) 
print(a%b)
print(a**b)


## Array mathematics MultiDimensional
import numpy as np
# Two Dimesnional : For two-dimensional arrays, multiplication remains elementwise and does not correspond to matrix multiplication
#TO do MAtrix multiplication we need to use dot method
a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]])  
c=a*b
print(c)

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([[10,11,12],[13,14,15], [16,17,18]])  
c=a*b
print(a.shape)
print(b.shape)
print(c)

a = np.array([5,6])
b = np.array([[1,2], [3,4]])
# In case of multi dimesional array if size doesn not match the tuple will be broadcasted automatically . 
# For Example in above case a will become [5,6], [5,6] automatically 
a+b
# FOr Broadcasting the one varibale should always be on size 1. below will throw error
#a = np.array([[5,6], [7,8]])
#b = np.array([[1,2], [3,4], [5,6]])
#a+b

# In multidimesion Axis:

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(a)
print(np.sum(a)) # gives sum of all.
print(np.sum(a, axis =0)) # Gives sum of each column 
print(np.sum(a, axis =1)) # Gives sum of each Row


## Methods : abs, sign, sqrt, log, log10, exp, sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, arcsinh, arccosh, and arctanh.
print(np.pi) 
print(np.e)
a = np.array([1, 2,3,4])
print( np.sqrt(a))
print( np.abs(a))

## Array iteration and operations
a = np.array([1, 2, 3])
for x in a:
     print (x) 
	 
	 
a = np.array([[1, 2, 3],[4,5,6]])
for x in a:
     print (x)
        

a = np.array([1, 3, 2])
print(np.sum(a))
print(np.prod(a)) 
print(a.mean()) 
print(a.var())
print(a.std()) 
print(a.min()) 
print(a.max()) 
a.sort()
print(a)
print(np.unique(a)) 

a = np.array([[4,5,6], [1, 3, 2]])
print(np.sum(a))
print(np.prod(a)) 
print(a.mean()) 
print(a.var())
print(a.std()) 
print(a.min()) 
print(a.max()) 
a.sort() # Sort inside the elements like 1,3,2 will be sorted to 1,2,3 . 123 and 456 will not be compared to sorted.
print(a)
print(np.unique(a)) 
print(a.diagonal())

## Comparison operators and value testing 
a = np.array([5, 2, 3]) 
b = np.array([3, 4, 5]) 
print(a > b)
print(a == b) 
print(a <= b )

#Arrays can be compared to single values using broadcasting: 
a = np.array([1, 5, 10])
a > 3

 #any and all : To determine whether or not any or all elements of a Boolean array are true
c = np.array([ True, False, False])
any(c)
all (c)

##indices
a = np.array([2, 5, 7, 9], float)
b = np.array([0, 1, 0, 2], int)
a[b]

a = np.array([[1, 3], [9, 15]], float)
b = np.array([1, 0, 0, 1], int)
c = np.array([0, 1, 0, 1], int)
a[b,c]		


## Matrix Multiplicatiosn: dot method
a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6])
np.dot(a, b)

#In multidimesional

a = np.array([[1,2], [3,4]])
b = np.array([[5,6], [7,8]]) 
c = np.array([2, 3])
d=a*b
print(d)
print (np.shape(a))
print (np.shape(c))
print(np.dot(a, b))
print(np.dot(a, c))  

# to apply dot funcation from a and b , second paarameter to shape should always be same. 
#Like a shape (x, y) and b shape (p, q) then y and p should be of same size . 
# Example. 3,2 and 2,3 . Here y and p value is 2. 

p = np.array([[1,2], [3,4], [5,6]])
q = np.array([[5,6], [7,8]])
print (np.shape(p))
print (np.shape(q))
print(np.dot(p, q)) # (3,2 ) dot (2, 2) so should be working fine .
#print(np.dot(q, p)) # should not work as (2,2) dot (3,2) will not work

