#Tuple is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is
#assigned whereas in a list elements can be changed.
# No change in size or content after creation of tuple
#Adv of Tuple
#1. we generally use tuple for heterogeneous data types and list for homogeneous datatype
#2. since tuple are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
#3. Tuple that contain immutable elements can be used as key for a dict. with list this is not possible
#4. If you have data that doesnt change implementing it as tuple will gurantee that it remains write-protected


#IMP NOTE:- Things NOT TO DO with tuple
# sort, append , reverse

#Creating Tuple
#Empty tuple
my_tuple=()
print(my_tuple)

#tuple having integers
mu_tuple=(1,2,3)
print(my_tuple)

#tuple with mixed datatype
my_tuple=(1,"Hello",11.11)
print(my_tuple)

#nested tuple
my_tuple=("mouse",[2,3,4],(5,6,7))
print(my_tuple)

# Update in tuple element.
my_tuple=("mouse",[2,3,4],(5,6,7))
my_tuple_1=("mouse",'rat', 'cat')
my_tuple[0]='rat' # Will throw error as tuple is immutable.
my_tuple[1]=[4,5,6] # Will throw error as tuple is immutable.
my_tuple[1][0]=9 # Will work fine as we are modifying nested element which is list and is mutable. 
my_tuple=my_tuple_1 # Reassignment of tuple is fine and possible . 
print(my_tuple)
print(my_tuple_1)


#tuple can be created without paranthesis also called tuple packing
my_tuple=3,4.6,"abc"
print(my_tuple)

#Tuple unpacking

a,b,c=my_tuple

print(a)
print(b)
print(c)

#creating a tuple with one elemnet is a bit tricky
#having one element within paranthesis is not enough. we will need a trailing comma to indicate that it is in fact a tuple

my_tuple=("hello")
print("kkkkkkkk",type(my_tuple))

#need a comma at the end
my_tuple=("hello",)
print(type(my_tuple))

#paranthesis is optional
my_tuple="hello",


#Accessing Elements in a tuple by 1)Indexing 2)negative indexing 3)Slicing

#1.Indexing :-

my_tuple=('a','c','c','e','n','t','u','r','e')

print(my_tuple[0])


#nested tuple
my_tuple=("mouse",[1,2,4],(4,5,6))
print(my_tuple[0][3])
print(my_tuple[1][1])

#2. Negative indexing

my_tuple=('a','c','c','e','n','t','u','r','e')

print(my_tuple[-2])  #output r

print(my_tuple[-6])  #output e


#3. SLicing

#we can access a range of items in a tuple by using the slicing operator - colon ":"

my_tuple=('a','c','c','e','n','t','u','r','e')

print(my_tuple[1:4]) #output c c e

print(my_tuple[:-7]) #output a c

print(my_tuple[7:])  #output r e

print(my_tuple[:])    #output a c c e n t u r e

#Changing a tuple unlike lists ,tuples are immutable

#This means that elements of a tupl cannot be chnaged once it has been assigned. But if the element is itself a mutable datatype like list
#its nested items can be changed

my_tuple=(4,2,3,[6,5])

#my_tuple[1]=11  will produce an error


#but item of mutable element like list inside tuple can be changed
my_tuple[3][0]=11
print("uuuuuuuuuuuuuuuuuuu",my_tuple)

'''
my_tuple=('a','c','c','e','n','t','u','r','e')

print(my_tuple)
'''



#we can use + operator to combine two tuples. concatenation and * too for repeat. iT will rsult into new tuple
print((1,2,3) +(4,5,6))
t1=(11,11,11)
t2=(22,22,22)
t3=t1+t2
print(t1)
print(t2)
print(t3)

print(("repeat",)*3)




#Delete tuple --> we cannot change the elements in a tuple. That also means we cannot delete or remove items from a tuple
#But deleting a tuple entirely is possible using the keyword del


del my_tuple

#tuple methods
'''
count(x)	Return the number of items that is equal to x
index(x)	Return index of first item that is equal to x
'''


my_tuple=('a','p','p','l','e',)

print(my_tuple.count('p'))

print(my_tuple.index('1'))


#***************** Tuple operations *********************************


#1.tuple membership test

print('a' in my_tuple)

print('b' in my_tuple)

print('g' not in my_tuple)


#tuple assignment
(x,y)=(101,'aaa')
#tuples are comparable
(0,1,2) < (5,1,2)



'''

Built-in Functions with Tuple
Function	Description
all()	        Return True if all elements of the tuple are true (or if the tuple is empty).
any()	        Return True if any element of the tuple is true. If the tuple is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of tuple as pairs.
len()	        Return the length (the number of items) in the tuple.
max()	        Return the largest item in the tuple.
min()	        Return the smallest item in the tuple
sorted()	Take elements in the tuple and return a new sorted list (does not sort the tuple itself).
sum()	        Retrun the sum of all elements in the tuple.
tuple()	        Convert an iterable (list, string, set, dictionary) to a tuple.

'''

alist=(123,'xyz','zara','abc')
aTuple=tuple(alist)
print("Tuple elements ",aTuple)

#Reverse the tuple
#As we know that in python tuples are immutable thus it cannot be changed or altered.
#thus provides us with limited ways of reversing a tuple unlike  list
#we will go through few techniques on how a tuple in python can be reversed

#Way 1 --> slicing In this technique, a copy of the tuple is made and the tuple is not sorted in-place.
#Since tuples are immutable, there is no way to reverse a tuple in-place.
#Creating a copy requires more space to hold all of the existing elements. Therefore, this exhausts memory.

a=[1,2,3,4,5]
print(a[::-1])


a="12345"
print(a[::-1])


a=(1,2,3,4,5)
print(a[::-1])

'''  not working below code
x=("accenture","aaa","bbb")
y=reversed(x)
print("Reverse of x is  ",y)


'''


# Sorting and reversal of tuple.
a=(123,35,46)
b=[123,35,46]
#reversed(a)
a=sorted(a)
a=tuple(a)
a
b.sort()
b


#Way 2 --> Using the reversed() built-in function
#In this method, we do not make any copy of the tuple.
#Instead, we get a reverse iterator which we use to cycle through the tuple, similar to the list.


def Reverse(tuples):
    new_tup=()
    for k in reversed(tuples):
        new_tup=new_tup+(k,)
    print(new_tup)


tuple1=(1,2,3,4,5,6,7,8)
Reverse(tuple1)


#Converting list to a tuple  --->Takes a single parameter which may be a list,string,set or
#even a dictionary( only keys are taken as elements) and converts them to a tuple.
list1=[0,1,2]
print(tuple(list1))
print(tuple('python'))

#Tuples in a loop

#python code for creating tuples in a loop
 
tup = ('geek',)
n = 5  #Number of time loop runs
for i in range(int(n)):
    tup = (tup,)
    print(tup)


	
def cmp(a, b):
    return (a > b) - (a < b) 

# Mutaility in tuple
airports = ('LAX', 'HNL', 'YYZ', 'NRT', 'CDG')
dest= ('LAX', 'HNL', 'YYZ', 'NRT', 'CDG')
dest_1=airports
print(airports ==dest)
print(airports is dest) # tuple is immutale still address will be different for two same object.
print(airports ==dest_1)
print(airports is dest_1)
print(id(airports))
print(id(dest_1))
print(id(dest))
	
	
#Using cmp(), max() , min()

# A python program to demonstrate the use of 
# cmp(), max(), min()
 
tuple1 = ('python', 'geek')
#tuple2 = ('coder', 'zz')
tuple2=('python', 'geek')
 
if (cmp(tuple1, tuple2) != 0):
 
    # cmp() returns 0 if matched, 1 when not tuple1 
    # is longer and -1 when tuple1 is shoter
    print('Not the same')
else:
    print('Same')
print ('Maximum element in tuples 1,2: ' +
        str(max(tuple1)) +  ',' +
        str(max(tuple2)))
print ('Minimum element in tuples 1,2: ' +
     str(min(tuple1)) + ','  + str(min(tuple2)))

