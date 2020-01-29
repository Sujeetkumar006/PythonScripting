#Contents accessed through symbolic keys instead of numeric indices
 # No maximum size
 # Similar to an associative array or hash in other languages
 # Contents may be composed of any combination of types :• Numeric literals, string literals, Booleans, and any other type

# Is represented within curly brackets { } by a comma-delimited series of key:value pairs
# Dict is Mutable.   # # # Keys are immutable and Values are mutable...

# In Dict Values are mutable and the keys are immutable
   #• Change in key implies a new entry for the dictionary
   #• Keys may be numeric literals, strings, or tuple elements


#Example Dict:
a= {'Name': "Sujeet", "ROll NUmber": '123'}
print(a)
# Access the element by its key:
a['Name']

#Keys can be String/Int/FLoat/Tuple/Boolean
var=1234
a= {123: "Sujeet", "ROll NUmber": '123',123.56:'Sujeet',var:"ac",('ac','pr'):"sjjd",True:123}
print(a[123])
print(a[('ac','pr')])

# Keys can not be List as List are mutable. Below will throw error.
a= {123: "Sujeet", "ROll NUmber": '123',123.56:'Sujeet',var:"ac",['ac','pr']:"sjjd"} # Will throw error as List cannot be key.
print(a)

# Values an be anything String/Int/FLoat/Tuple/Boolean/List/Dict

a={'a':'ac','b':123, 'c':123.45, 'd':True, 'e':['abc','pqr'],'f':('abc','xyz'), 'g': {'abc':123, 'pqr':345}}
print(a)

# Values in key are mutable and can be modified.
a={'a':'abc','b':"pqr",'c':'xyz'}
print(a)
a={'a':'abc','b':"pqr",'c':'xyz'}
a['a']='mln' # Value for key 'a' has been modified.
print(a)

# NEw key: value can be added in Dict.

a={'a':'abc','b':"pqr",'c':'xyz'}
a['d']='mln'
print(a)

# Duplicate key. Dict cannot have duplicate key. but reusing the key will not give the error but it will reasiign the latest value to key.

a={'a':'abc','b':"pqr",'c':'xyz'}
a['d']='mln'
a['d']='rst'
print(a)

#Method functions allow modification of contents or data retrieval

#dict.keys()—Returns a list of keys
a={'a':'abc','b':"pqr",'c':'xyz'}
a.keys()
	
a={'a':'abc','b':"pqr",'c':'xyz'}
b={'e':'mln', 'f':'rst'}
c={'a':123}
a.keys()
#dict.values()—Returns a list of values
a.values()
#dict.update(newdict)—Merges contents of newdict into dict 
a.update (b)
a.update(c) # if the key is common , it will be upadted by latest value for that key
print(a)
#dict.get(key)—Returns value at key, else None for undefined key
print(a.get('a'))
print(a['a']) #what is difference between a.get('a') and a['a']. a.get() will return None in case key is not found, a['a'] will return error if key is not found.
print(a.get('n'))
print(a['n']) 
#len(dict)—Returns the number of items in the dictionary
len(a)

#dict.items()—Returns a list of key–value pairs as tuples
a={'a':'abc','b':"pqr",'c':'xyz'}
a.items()

# Copy the dict from anothe dict

a={'a':'abc','b':"pqr",'c':'xyz'}
c=a
b = dict(a.items())
print(b)
print(id(a))
print(id(b))
print(id(c))

#A dictionary can be created from a sequence of key–value pairs
 #dict(arg) returns a dictionary
 #arg is a sequence containing the key–value pairs
 
p=dict([['a','abc'], ['b','pqr']]) # Dict from List of List
q=dict([('a','abc'), ('b','pqr')]) # Dict from List of tuple
r=dict((['a','abc'], ['b','pqr'])) # Dict from tuple of List
s=dict((('a','abc'), ('b','pqr'))) # Dict from tuple of tuple
s=dict(((('a','abc'),['abc','pqr']), ('b','pqr')))  # Dict from tuple of tuple where key is also tuple and value is list.
print(p)
print(q)
print(r)
print(s) 
 
## The argument in above set list/tuple should only have two values.

p=dict([['a','abc','rst'], ['b','pqr','mln']]) # This will throw an error as argument is having 3 values. For key values to happen only 2 value should be there. 
print(p)


# zip() funcation: Combines two collections in parallel and returns a new list
		#• Composed of two element tuples based on position
		#• Returned list is the length of the shorter argument

a = ['FR', 'GB', 'CA', 'JP', 'US'] 
b = [33, 44, 1, 81]
c=list(zip(a, b)) # a is having 5 elemets and b is having 4 element so resulting list will have lessar means 4 elements.
d=tuple(zip(a, b))
e=dict(zip(a, b))
print(c)
print(d)
print(e)

# Practice:
a = [33, 44, 1, 81]
b = ['FR', 'GB', 'CA', 'JP', 'US'] 


		