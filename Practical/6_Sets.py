## Sets....
 # Unsequenced/Ordered mutable collections of unique objects
 # • Created with the set() function Or by assignment with {}
 #   Slicing or fetching element at index ??

 # First way to create set.
 
a = set(['HNL', 'ITO']) # Creatig a set from List. Argumet should be list or tuple
b = set(('HNL', 'ITO')) # Argumet should be list or tuple

 # Aother way to create set.
 
b= {'HNL', 'NRT'}

# Copy of set to aother set.
e = {'HNL', 'ITO'} # another way to create set.
c = set(e)   # copy the set e to set c. 
d = c
print(id(c))
print(id(d))
print(id(e))

# Sorted and unique element in list
a= ['abz','aac',1233,34,56,678,3435,56]
b=set(a) # this will work as set sorts the multi type daata , here string and int.
a.sort() # This will trow error as in sorting we should always have homogenious data type
b

# Sorting with multi type element is Set.
a={123,34,45,657,67,78} # Will be sorted in ascending order
b={'pqr','abc','xyz'} # Will be sorted in ascending order 
c={45, 123,34,45,657,78,67,'pqr','abc'} # In this case the sorting will happen but the integer will be treated as String and wil be sorted accordingly. SO here 123 having start element as 1 and dhould be come very first.
d={45, 45.0, 45.1, 45.2, 45, 47,123, '123'} # In this case even 123 and '123' both considered as string fro sorting rule but also is unique element so both will appear in set. 
# The above will happen as set works in two part. in Part 1 it will find the unique value so it will consider both 123 and '123' as they are different so in 2nd part i.e. sorting both 123 and '123' will be considered. 

# in case similar value of int and float which ever will come first be kept as unique value. E.G: 45 and 45.0 is same and will come only once
c={45, 45.1, 45.2, 45, 47, 'abc', 'pqr'} # In this case int 45 will be considered as no flot value equivalent to it.
d={45.0, 45, 45.1, 45.2, 45, 47} # in this case among 45.0 and 45 only one will be considered which ever will appread first in the set. 
d

# Set will always have unique values. Duplicate will be removed automatically.
e = {'ac', 'pq','pq'}
print(e)
>>{'pq', 'ac'}

# Add and remove items: The set.add() and set.remove() methods can add or remove members
a = {'ac','pq','rc'}
a.add('mn')
a.remove('pq')
print(a)


# Set should always have the immutable objects : in Python 3. 
# No set of Set is possible in terms of set.
 b={1,2,3,4,5,(1,2,3,4)}
print(b)
b={1,2,3,4,5,[1,2,3,4]} # will trhow an error. 
print(b)


#Arithmatic style operatio in set.

a = {'ac','pq','rc'}
b= {'pq', 'mn'}
#a-b
#b-a
#a|b # Unioun
a&b # Interset


# Collection membership testing: Syntax: value in collection
  #• Returns True if the value is a member
  #• Works for all collection types and strings
  # Limited to testing keys for dictionaries

 a = {'ac','pq','rc'}
'ac' in a

# variale type 'None' in python.
