################### Topics #######################

#String

#################### Topics ##########################STring in python

myString='Hello'
print(myString)

myString="Hello"
print(myString)

myString='''Hello'''
print(myString)

myString='''Hi welcome
        to accenture 
        Good Luck '''
print(myString)

string1=""" This is new string """
print(string1)

a='abcdefghij'
print(a[0:30:1]) # Will not give error althogu strig is of ot length 30. It has been handled in Python.
print(a[30]) # this will throw an error.

#String within string

print("'You must be the change you wish to see in the world' - Gandhi")
print("\"You must be the change you wish to see in the world\" - Gandhi")
print('''He said ,"What's there ? "''')

#How to access char in string
#indexError if out of index and TypeError if we use float or other data type
#python allows negative indexing


########## String Slicing########################
mystring[a:b:c]
mystring[a:b]
mystring[a:]
mystring[:b]
mystring[:]

mystring ="HelloWorld"
print(mystring)
print(mystring[0])
print(mystring[-10])
print(mystring[-1])
print(mystring[9])
print(mystring[-5])

#Slicing 2nd to 5th char  HelloWorld
print('mystring[1:5]',mystring[1:5])
print('mystring[1:5]',mystring[1:10])
print('mystring[1:5]',mystring[0:10])

# Reverse Triversal
str= 'Hello World'
str[-1:-10:-2]
str[::-1]

mystring='HelloWorld'
# mystring[5]='a'  This code will produce error .

#We can not delete or remove char from a string but deleting the string entirely is possible using the keyword del
del mystring
#print(mystring)

#Concatenation of two or more string  + operator is used
# * operator used to repeat the string for a given number of time

str1='hello'
str2='world'

print('str1+str2  = ',str1+str2)

print('str1*3 = ', str1* 3)

name= 'Hello'
print(name+name+name)
print(name[0]*3+name)

## Interger or Float to String

print(str(-12.5))
print(str(7/3.0))

#Iteration through string
count=0
for letter in 'Hello World':
    if(letter == 'l'):
        count+=1
print(count,' letters found')

#String membership test We can test if a sub string exists within a string or not,using keyword in
print('a' in 'program')
print('at' not in 'battle')

#various built in functions that work with sequence , work with string as well .
#enumerate(): return key value with index.
str='Winter'
list_enumerate=list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)
#len() 
print('length of string is',len(str))
# lower()
print('HeLLo WORld'.lower()) 
#upper()
print('HeLLo WORld'.upper())
#join() : Join the said string with all passed arguments

# Join in string:
#In String the join methpod will add the first string in all the string array element in argument.

a='$'.join('Hello world')
>>H$e$l$l$o$ $w$o$r$l$d # Here the "$" or string on which join is called will be added in all the string indexs Like H,e,l,l,0, ,w,o,r,l,d beacuse argument in join works as a Char array instead of string. join will consider each char if string as seprate element and add the join value separeltly. Also, the value will NOT be added in last eleement. 


print(' '.join(['This','will','join','all','words','into','a','string']))
>> This will join all words into a string
print('Hello '.join(['This','will','join','all','words','into','a','string']))
>>This Hellowill Hellojoin Helloall Hellowords Hellointo Helloa Hellostring

# Join can be used to put commas in between all the elements in list.
mystring = 'Hello World'.split(' ')
word= ','.join(mystring)
print(word)

# elow will not work as join can not concatinate the strinng with INTeger.
strig=['Hello',123]
str4='$'.join(strig)
print(str4)
print(type(str4))

# Difference between concatinate (+) and join.

#split() : Split the string and provide list as return output.
mystring ='hello.py'
mystring1 ='hello world'
mystringsplit=mystring.split('.')
mystringsplit1=mystring1.split(' ')
print(mystringsplit)
print(mystringsplit1)

#find(), rfind() : string.find() and string.rfind() return the offset of the search Or -1 if the string is not found

# find : First occurance
# rfind: last occurance

print('Happy New Year'.find('ew'))
print('Happy New Year'.rfind('e'))

sea = 'Atlantic Ocean'
sea.find('a')
sea[sea.find('a'):sea.rfind('a')+1]

#replace(): string.replace(old, new) returns a new string after replacing all occurrences of old with new
print('Happy New Year'.replace('Happy','Brilliant'))  
print('Happy New Year Happy'.replace('Happy','Brilliant'))  # Replace all

#isupper()
#islower()


#The format() Method for Formatting Strings Format strings contains curly braces {} as placeholders or replacement fields which gets replaced.
# default(implicit) order

default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)


default_order = "{}, {} and {}".format('John','Bill',123) # FOrmat argument can be int/float as well.
print('\n--- Default Order ---')
print(default_order)


a=input("Enter your Name:")
b=input("Enter your roll number:")
c=input ("Enter your class:")

default_order = "{}, {} and {}".format('John','Bill',123) # FOrmat argument can be int/float as well.
default_order_var= "My NAme is :{}, My Roll Numer is {} and Class {}".format(a,b,c)
print(default_order)
print(default_order_var)


# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)



# extra and less argument
keyword_order = "{}, {} and {}".format('John','Bill','Sean','hi')
keyword_order = "{}, {} and {}".format('John','Bill') # Throw error
print('\n--- Keyword Order ---')
print(keyword_order) 


default_order = "{a}, {c} and {a}".format(c='Bill',a=123) # in case of keyword argument if all name in format will match with {} then even lesser argument will work.  Here a is used twice so argument us only 2 , i.e. a and c.
default_order


## Other String place holder: %S is mailnly for String but can store anything like Number and List and all, %d for numeric and always integer but accepts float and convert it to Integer, String or List or any other data type will throw error for %d.

name = "John"
print("Hello, %s!" % name)

name = "John"
age = 23
print("%s is %d years old." % (name, age))
print("%s is %d years old." % (age, name)) # Will throw an error for sequence of argument.
print("%s is %d years old." % (name, age, age1)) # Will throw an error for number of argument.

age = 23.15
print("%s is %d years old." % (name, age))

name = ["John",'Jhony']
print("Hello, %s!" % name)

name = ["John",'Jhony']
print("Hello, %d!" % name) # Throw an error as name is not Number.

name='123'
print("Hello, %d!" % name) # # Throw an error as name is not Number.

name = ["John",'Jhony',234]
print("Hello, %s!" % name)	 # Will work as %s can take all types

name = 234
print("Hello, %s!" % name)	 # Will work as %s can take all types

#capitalize() It returns a copy of the string with only its first character capitalized.
str = "this is string example....wow!!!";
print ("str.capitalize() : ", str.capitalize())

#center() method The method center() returns centered in a string of length width. Padding is done using the specified fillchar. Default filler is a space.
#str.center(width[, fillchar]) This method returns centered in a string of length width.
str = "Welcome"
print ("str.center(10, '*') : ", str.center(10, '*'))

# Some more funcations and constants in string module.
>>> import string
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.digits
'0123456789'
>>> string.hexdigits
'0123456789abcdefABCDEF'
>>> string.octdigits
'01234567'

>>> string.capwords('now is the time')
'Now Is The Time'
>>> string.capwords('now_is_the_time','_')
'Now_Is_The_Time'


## Escape Sequences:
#\', \", \\ , \r, \n, \t , \0num, \xnum

print ('\t is tab')

#Check
#isdigit isnumeric

#########################

Excersice:
1) Truncate the string using split.
a=a.strip()
OR
a='Hello wolrd    again     again        '
b=a.split(' ')
finalelemt=''
counter=0
for i in b:
    if i !='':
        if counter ==0:
            print('I ma inside first loop')
            finalelemt=finalelemt+i
            counter=1
        else:    
         finalelemt=finalelemt+" "+i
finalelemt


2) String index found for multiple occurnace:

a='abcbcbcsfdjhkkbcjshdjcdlkjkfjckdkjkjbcjjdjjd' # Fid the coccurnce of bc. Hint: find/rfind, split .
