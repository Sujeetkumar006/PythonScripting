################### Topics #######################
# List: Similar to an array in other languages , No maximum size
 #Contents may be a combination of different types : Numeric literals, string literals, Booleans, and any other type

#List in python --> a compound datatype . very versatile datatype used in python
#List is created placing all the items inside square separated by commas
#Python provides several types of collections
 # Compound data types or data structures
  #Composed of elements of various types

#Sequential
 # Access individual values by a numeric offset:  Strings, lists, and tuples
#Mapped or associative
 # Access individual values by a key : Dictionaries
#Unordered : Sets

# what is difference between order and shorting? . (Value and indexing)

#May be mutable or immutable
    #• Lists, sets, and dictionary values are mutable : memory addess remain same.
    #• Strings, tuples, and dictionary keys are immutable

#################### Topics ##########################STring in python
# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed datatypes
my_list = [1, "Hello", 3.4]

# nested list : List of List
my_list = ["mouse", [8, 4, 6], ['a']]

#How to access elements from a list?
#List index We can use the index operator [] to access an item in a list. Index starts from 0
#Nested list are accessed using nested indexing.

my_list = ['p','r','o','b','e']
print(my_list[0])
print(my_list[2])
print(my_list[4])

my_list[4.0]  # Error! Only integer can be used for indexing

# Nested List
n_list = ["Happy", [2,0,1,5]]
# Nested indexing
print(n_list[0][1])    
print(n_list[1][3])

#Access list elements by negative indexing
my_list = ['p','r','o','b','e']
print(my_list[-1])
print(my_list[-5])

#How to slice the list  We can access a range of items in a list by using the slicing operator (colon).
my_list = ['a','c','c','e','n','t','u','r','e']
# elements 3rd to 5th  --> c  e  n  2 inclusive and 5 excluded
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-5])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

#How to change or add elements to a list?
#List are mutable, meaning, their elements can be changed unlike string or tuple.
#we can use = operator or range of item

# init values
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  
print(odd)

# add additional item in list in update
odd = [2, 4, 6, 8]
print(odd)
odd[1:4] = [3, 5, 7,9,11,12,15,17] # instead of 3 elements 8 elements has been added and it will work.
print(odd)  

# Assigmet
z =  ['Hello', 'world', 'Program']
#z[0] = 123  # THis will work as z[0] is idex ad we are replacig one value with 1 value.
#z[0:3] =123 # This will not work as i left side we have slicing so right should should have value whcih support slicing like list, string. 
z[0:3] ='acd' # This will work ad assig a,c,d elemet to List as separate elemet.
z[0:2] =[] # Tjis will work
z

# to add last elemet i list:
z =  ['Hello', 'world', 'Program']
z[3] =  'pqr' # This will not work as we can not assig the value i last idex.
z[3:0] OR z[len(z):]=  'pqr' # This will work as slicing work with last idex also. 
z

#We can add one item to alist using append() method or add several items using extend() method

odd=[1,3,5]
odd.append(7)  # Append uses index and add the value in last index of list.
print(odd)

odd.extend([9,11,13]) # Extend uses slicing and add value from last of the list.
print(odd)

#How to delete or remove elements from a list?
my_list = ['p','r','o','b','l','e','m']

# delete one item
del my_list[2]

# delete multiple items
del my_list[1:5] 

# delete entire list
del my_list       
print(my_list)

# List Mutability:

odd = [2, 4, 6, 8]
print(odd)
print(id(odd[0])) 
odd[0]=3
print(odd)
print(id(odd[0])) # Address is different than above as element of list is immutable so change in value will change in address.

odd = [2, 4, 6, 8]
print(odd)
print(id(odd)) 
odd[0]=3
print(odd)
print(id(odd)) # Address is same as above as List is mutable &address of list will not chnage even in cahnge of value of list/list element.


# List of List Mutability. 
my_list = ["mouse", [8, 4, 6], ['a']]
#print(id(my_list)) # 2165930925960
print(my_list)
print(('Mylist1: ', id(my_list[1]))) #2165931646088
#my_list[1]=[8,4]   # This is reassignement of valriable my_list[1] and not the update of variable my_list[1]
#print(my_list)
#print(('Mylist1: ', id(my_list[1]))) #2165931792008 : Here we are changing the my_list[1] itself to have different list, although the value is almots similar but it is different list so address of my_list[1] will change. . Parent list still have same address and follow mutability. 
my_list[1][1]=5 # Here we are modifying the element in my_list[1] and not reassinging the whole list so my_list[1] address will not chnage. This is update of valriable my_list[1] element and not reassignment. 
print(my_list) 
print(('Mylist1: ', id(my_list[1])))# 2165931646088
#print(id(my_list)) #2165930925960 : List id will remian same even if value of list changes



# List value assignemnt to other list and update.
my_list = ["mouse",'Dog' ,[8, 4, 6], ['a']]
my_list1=my_list
print(my_list)
my_list[0]='rat'
my_list1[1]='cat'
print(my_list)
print(id(my_list))
print(id(my_list1))

# Difference between String and List mutablility
a= 'abc'
b= 'abc'
p=a
c=['abc', 'pqr']
d=['abc', 'pqr']
e=c
print(id(a))
print(id(b))
print(id(p))
print (a==b)
print (a is b)
print (a==p)
print (a is p)
print(id(c))
print(id(d))
print(id(e))
print (c==d)
print (c is d)
print (c==e)
print (c is e)

# The list(arg) function returns its argument as a list
airports = ['LAX', 'HNL', 'YYZ', 'NRT', 'CDG']
dest=airports
dest1=list(airports) # this is a shallow copy. list(args) use shallow copy.
print(dest is airports)
print(dest1 is airports)
print(id(airports))
print(id(dest))
print(id(dest1))
dest[0] = 'abc'
dest1[1] ='pqr'
airports[2] = 'xyz'
print(dest1)
print(airports)
print(dest)

## Shallow and Deep copy: Mainly for nested object like nested List. Please note that list or object copy work differently for nested object. Like copy of list of list will be different from list of string/Int. list(args) also use shallow copy.
import copy
copy.copy(x) # Shallow copy.
copy.deepcopy(x) # Deep Copy.

#A shallow copy creates a new object which stores the reference of the original elements. So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.
# Mainly for nested object like nested List.

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list) # This will create new and independent 'new_list' object with same content as of 'old_list'.
new_list1=list(old_list)
print(id(old_list))
print(id(new_list)) # Have different memory address than old_list as new list has been created . 
print(id(new_list1)) # Have different memory address than old_list as new list has been created .
print("Old list:", old_list)
print("New list:", new_list)
print("New list:", new_list1)
print(id(old_list[0]))
print(id(new_list[0])) # Have same memory address as of old_lis[0] as reference has only been copied and not created newly for nested 
print(id(new_list1[0])) # Have same memory address as of old_lis[0] as reference has only been copied and not created newly for nested object. 
# Adding [4, 4, 4] (New object) to old_list, using shallow copy : Will not reflect in new_list or new_list1
old_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)
print("New list:", new_list1)
 
#Adding/updating in existing nested object using Shallow copy : Will refelect in both the list
old_list[1][1] = 'AA'
print("Old list:", old_list)
print("New list:", new_list)
print("New list:", new_list1)

#In above we made changes to old_list i.e old_list[1][1] = 'AA'. Both sublists of old_list and new_list at index [1][1] were modified. This is because, both lists share the reference of same nested objects.

# The above concept will only be applicable for Nested object i.e list[a][b]. in case if the elements of objects is string/number insted of list this above concept will not work and change is old_list will not reflect in new_list and vice versa.  Also, in case of above nested object if insted of nested element directly sub element (i.e list[a] instead of list [a][b]) will modify in old_list then it will not reflect in new_list and vice versa.

import copy
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[10,11,12]]
new=old_list
new1=list(old_list)
new2 = copy.copy(old_list)
print(id(new))
print(id(old_list))
print(id(new1))
print(id(new2))
print(id(new[0]))
print(id(old_list[0]))
print(id(new1[0]))
print(id(new2[0]))
old_list[0]=['a','b','c']
new[1]=['p','q','r']
new1[2]=['x','y','z']
new2[3] = ['m','n','o']
old_list.append(['r','t','s','u'])
print(old_list)
print(new)
print(new1)
print(new2)


##Deep copy : A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)

old_list[1][0] = 'BB' # As old_list to new_list is deep copy so it would not be reflected in new_list. 

print("Old list:", old_list)
print("New list:", new_list)


# Final Conclusion:

import copy
old_list = [[1, 2, 3, 4], [4, 5, 6], [7, 8, 9],[10,11,12]]
new=old_list
new1=list(old_list)
new2 = copy.copy(old_list)
print(id(new))
print(id(old_list))
print(id(new1))
print(id(new2))
print(id(new[0]))
print(id(old_list[0]))
print(id(new1[0]))
print(id(new2[0]))
old_list[0][0]='a'
new[0][1]='b'
new1[0][2]='c'
new2[0][3] ='d'
old_list.append(['l','r','j'])
print(old_list)
print(new)
print(new1)
print(new2)

####

airports = ['LAX', 'HNL', 'YYZ', 'NRT', 'CDG']
dest=airports
dest1=list(airports) # this is a type of shallow copy
print(dest is airports)
print(dest1 is airports)
print(id(airports))
print(id(dest))
print(id(dest1))
dest[0] = 'abc'
dest1[1] ='pqr'
airports[2] = 'xyz'
print(dest1)
print(airports)
print(dest)

### 
#List The + operator concatenates lists and The * operator repeats lists

airports = ['LAX', 'HNL', 'YYZ', 'NRT', 'CDG']
old_list = [[1, 2, 3, 4], [4, 5, 6], [7, 8, 9],[10,11,12]]
print(airports+old_list)
print(old_list*2)

# Few Funcations:

#len(): function returns the number of elements in the list
old_list = [[1, 2, 3, 4], [4, 5, 6], [7, 8, 9],[10,11,12]]
len(old_list)

list_fun=['abc', 'pqr', 'xyz', 123]
#list.append(value)—Add value to the end
list_fun.append('rst')
print(list_fun)
#list.pop(n)—Remove element n and return it 
list_fun.pop(3)
print(list_fun.pop()) # Remove last element in the list if no index has passed.
print(list_fun)
#list.insert(posit,value)—Add value at position posit 
list_fun.insert(3,678)
print(list_fun)
#list.remove(value)—Remove first element containing valu
list_fun.remove('abc')
print(list_fun)
#list.reverse()- Reverse the String
list_fun=['abc', 'pqr', 'xyz', 123]
list_fun.reverse()
print(list_fun)
# list.clear
list_fun.clear()
print(list_fun)
# list.sort(): Sorting the list
list_fun=['abc', 'pqr', 'xyz', 123]
list_fun.sort() # List is having the mix element so will throw error
print(list_fun)
#
list_fun=[1000, 9, 234, 123]
list_fun.sort() 
print(list_fun)
#
list_fun=['abc', 'pqr', 'xyz']
list_fun.sort() 
print(list_fun)
#
list_fun=['aab', 'aac', 'abb','baa']
list_fun.sort() 
print(list_fun)
#
list_fun=[['bbb', 'ccc'], ['aaa','bbb'],['aaa', 'ccc']]
list_fun.sort() 
print(list_fun)

#diff between del,pop,remove
#del --> delets value at a specific index
#remove --> will remove the first matching value in list
#pop--> delets value at specific pos and also returns the value to end user

'''
We can use remove() method to remove the given item or pop() method to remove an item at the given index.

The pop() method removes and returns the last item if index is not provided.
This helps us implement lists as stacks (first in, last out data structure).

We can also use the clear() method to empty a list.
'''

'''
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list
'''

my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list.index(8))
print(my_list.count(8))
#Basic list  operations
print(3 in [1,2,3]) #o/p true

#Built in List Functions & Methods
list1,list2=[123,222],[456,'xyz']
print(max(list1))
print(min(list1))
print(sum(list1))

