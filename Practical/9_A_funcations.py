#function in python --> create clean repeatable code is a key part of becoming
# an effective prog
#function allow us to create block of code that can be easily exe 
#many times without needing to constantly rewrite the entire block of code


# global and local variable name space:
#If the same variable name has been used inside and outside of funcation , the local variable inside the funcation will have scope only till inside. and both local and global variable will have different name sapce. local funcation variable update inside the funcation will only limit to inside. In case we want to refer global variable from inside of funcation which is having same local variable name, we can use global keyword.     

#Case1
counter = 300
def myfunc():
  counter = 10
  counter = counter+200
  print(counter) # 210 
myfunc()
print(counter) # 300

#Case2:
counter = 300
def myfunc():
  global counter
  counter = 10
  counter = counter+200
  print(counter)  #210
myfunc()
print(counter) #210


#write a function to add two numbers

def addition(x,y):
    '''
    DOCSTRING : Information about function
    INPUT: Two numbers
    OUTPUT: addition of given numbers
    '''
    sum = x+y   
    print("Addition is",sum) 
print("Function definition done")

addition(10,20)
addition(10.11,11.11)
addition('a','a')
addition('aa','aa')

# addition('a',10)  Will not work


#Great feature to print doc in function
#Case 1. it will pick up the only comment which we provide just after
#function name.
#Case 2. we will not be able to retrieve other comments in function
#in that case it will return None
#Case 3: it will not work for single line comment
print("commnets is",addition.__doc__)


#return statement

def squareOfNumber(num):
    '''This functions returns the square of given number'''
    result=num*num*num;
    return result

print("Square of 2 is ",squareOfNumber(2))



#Prog to return multiple values.we can use normal values or simply return a tuple

def function1():
    return 1,2,3

a,b,c=function1()
print(a,b,c)



#below code will also work
a=function1() # Can assign multiple retrun to same collection type tuple variable.
print(a,b,c)
print(a)
print(type(a))


#pass by value and pass by ref

def swapbyvalue(num1,num2):
    temp=num1
    num1=num2
    num2=temp

n1=11
n2=22
swapbyvalue(n1,n2)
print(n1,n2)


list1=[11,22]

def swapbyref(l):
    temp=l[0]
    l[0]=l[1]
    l[1]=temp


swapbyref(list1)
print(list1)

# Pass by value and pass by reference example along with global and local varaiable:

a=[10,20,30] # Mutable, Passing . XXX
b='ab' # Imutable , Passing . XXY
c=123 # Immutable ,  Not Passing
d=['a','b','c'] # Mutable , Not passing.
def addition(a,b):  # addition(xxx, xxy)
    d=['1','2']
    c=456
    a[0]=100 # a id : xxx
    b='Pq' # XXY to XXZ.
    print('Printing add:',a,b,c,d) #  XXX, XXZ, Id(c), id(d)
addition(a,b) # additinon(10,20) # addition (id(a), id(b))
print('Printing add:',a,b,c,d) # XXX, XXY, Id(c), id(d)

#-------------------------------------------------------------------------------------------------------------



#***************  types of args in python default,positional,keyword args *****


#****************************** Default args  ***************************************


#Python default arguments
#example 1
#In below example name does not have a default value and is required during a call.
#WHile message has a default value so it is optional during call.

def greet(name,message="Happy New Year"):
    '''This function greets to the person with the provided message.
        If message is not provided it defaults to "Happy New Year"
        '''
    print("Hello ",name +' , '+message)
greet("Swati")
greet("Anagha","How do you do?")




#Any number of args in a function can have a default value. But once we have a default arg, all the args to its right must also have default values
#Means non-default argumnets cannot follow default argumnets
#gets error
'''def greet(message="Hello",name):
    pass'''

print("************************************")

#Example 2
def display(Id,Name,Age=21):
    '''printing passed values'''
    print(Id)
    print (Name)
    print (Age)
    return


display(Id=100,Name='Swati',Age='33')

display(Id=101,Name='Anagha')

display(102,'Avinash',35)


#****************************** Keyword args  ***************************************


#Python keyword arguments
#WHen we call a function with some values these values get assigned to the argumnets according to their position
#Python allows functions to be called using keyword arguments.
#When we call functions in this way the order of arg can be chnaged.

def greet(name,message="Happy New Year"):
    '''This function greets to the person with the provided message.
        If message is not provided it defaults to "Happy New Year"
        '''
    print("Hello ",name +' , '+message)

greet("Swati")
greet("Anagha","How do you do?")




#diff calls to greet function

#2 keyword arguments
greet(name="Swati",message="Welcome to Python")

# 2 keyword arguments (out of order)
greet(name="Swati",message="Welcome to Python")

# 1 positional , 1 keyword argument
greet("Swati",message="Welcome to Python")

#Having positional arg after keyword args will result into errors
greet(name="Swati", "How are you?")



#****************************** Arbitarary args  ***************************************

#Python Arbitrary argumnets

#Sometimes we do not know in adv the number of arg that will be passed into a funtion
#python allows us to handle this kind of situation through function calls with
#arbitrary number of arguments

#in the function definition we use an asterisk before the paramtere to denote
#this kind of argument.


#Example 1

def greet(*names ,message="Hello"):
    '''This function greets all the person in the names tuple'''
    for name in names:
        print("Hello ",name)


greet("Monica","Steve","John","Hello world")        


#Example 2 chnage the seq of param 

def greet(message ,*names ):
    '''This function greets all the person in the names tuple'''
    for name in names:
        print("Hello ",name)


greet("Monica","Steve","John","Hello world")  


#### Example of All type of argument accoring to preceedence:

def addition(cutid, userid, *a, b,c=0,**d):   # Positional, * variable lenght positiona;, Keyword, Keyword with Deafult,* variable lenght  keyword.
  print(cutid)
  print(userid)
  print(a)
  print(b)
  print(c)
  print(d)

addition(123,345,334,4,5,5,6, b=100, c=101,d='anv',e='abc' )

#-----------------------------------------------------------------------------------------------------------


#Exercise Time

#Program using function to make the average of any quantity of number

def average(first, *rests):
    return(first +sum(rests))/(1+len(rests))

#sample use putting values
print(average(11))	
print(average(1,2))
print(average(1,2,3))
print(average(1,2,3,4))

#call to function in diff ways
    #1.provide the mandatory arg only
    #2. provide one of the optional arg
    #3. by giving all the arg



#Exercise Time --> Exercise4


#Example 2




#Example 3
# many args by * shld be last arg

def g(a, *arg,b):
    return a



#Exercise Time
#Write a prog to calculate fibnacci series by using function
#Answer fiboSeries.py



#Functions -related statement

x=10
def printer():
    x=30
    print(x)
print(x)    
printer()
print("global variable" ,x)

#############
counter = 300
def myfunc():
  #global x
  counter = 10
  counter = counter+200
  print(counter)  
myfunc()
print(counter)




''' Not getting below part from
https://www.w3schools.in/python-tutorial/functions/
website
nonlocal:def outer():
    a='old'
    print(a)
    def inner():
        nonlocal a:a='new'
        print(a)
print(outer())
'''




#Example 4
#Prog to return multiple values.we can use normal values or simply return a tuple

def function1():
    return 1,2,3

a,b,c=function1()
print(a,b,c)

#below code will also work

c=function1()
print(c)
print(type(c))






#find out if the word 'test' is in a strin?

# decode the word. if word starts with vowel append ay and if not then append first letter and ay
#Example word --> ordway  apple --> appleay


## Example of all argumets:

def methodallargs(posarg1,posarg2,*arg,keyword,keywordde='Pune',**args):
    print(posarg1)
    print(posarg2)
    print(arg)
    print(keyword)
    print(keywordde)
    print(args)
methodallargs(10,20,30,40,50,60,keyword=40,keywordde='Delhi',address='Pune',rollnumber=123)