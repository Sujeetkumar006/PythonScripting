#Iterators in Python:
#Iterator in python is any python type that can be used with a ‘for in loop’. Python lists, tuples, dicts and sets are all examples of inbuilt iterators. These types are iterators because they implement following methods. In fact, any object that wants to be an iterator must implement following methods.
"""1) __iter__ method that is called on initialization of an iterator. This should return an object that has a next or __next__ (in Python 3) method.
2) next ( __next__ in Python 3) The iterator next method should return the next value for the iterable. When an iterator is used with a ‘for in’ loop, the for loop implicitly calls next() on the iterator object. This method should raise a StopIteration to signal the end of the iteration.
#Iterable Object : By default python for loop use the same method internally for iteration.
#The iter() built-in function returns an iterable object
#The __next__() method provides each element
#• Raises the StopIteration exception when sequence is exhausted

airports = ['LAX', 'HNL', 'YYZ']
airport_iter = iter(airports)
airport_iter.__next__()
>>> airport_iter.__next__()
'HNL'
>>> airport_iter.__next__()
'YYZ'
>>> airport_iter.__next__()
Traceback (most recent call last): # Exception raised when iteration is complete
"""



########### Yield and Generator

#Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

#The yield keyword in Python is used to create generators. A generator is a type of collection that produces items on-the-fly and can only be iterated once. By using generators you can improve your application's performance and consume less memory as compared to normal collections, so it provides a nice boost in performance. IN normal we use range funcation in which the iterable object is actually created on which the iteration happens. This object consume the memory so by using generator we can create the collection on the fly which can be used once and do not need memory space as it is not stored.

 #Lists or any iterable collection object like tuple ,set, dict keys store all of the elements in memory at once, whereas generators "create" each item on-the-fly, displays it, and then moves to the next element, discarding the previous element from the memory.
 
 #you can iterate over a list or any iterable collection object like tuple ,set, dict keys as many times as you want but you can iterate over a generator only once. To iterate again, you must create the generator again.
 
 
 ### Yield: Yield is a keyword which is used to create generator in python. Yield is similar to keyword "return" which is used in funcation to return the result. The difference between "return" and "yield" is as return give the value at once (final value) and yield can give the value for multiple times. Like if we have list of elemets , return will give the whole list and yield can give one element of list at a time. If we return whole list it requires to store the list in memory , in yield as each element is getting reutrened on the fly we do not need to store so it is used in generator and ultimately saves memory and also be fast.
 
 
# Suppose we need a itertator as square of values given as list 
def cube_numbers(nums): 
    cube_list =[]
    for i in nums:
        cube_list.append(i*i)
    return cube_list  # Here we are returning the list . so we are returning the whole value at once. we are returning the iterable object as list of sqaue value of nums.
cubes = cube_numbers([1,2,3,4,5]) # now cubes can be used as iterable object . This is same as normal 
print(type(cubes),cubes)
for temp in cubes: # here we are iterating over list cubes and this need a memory to store the cubes list. If we use random keyword also , that also created a list and need memory space. 
  print(temp)


## Same iterable object by using generator:
def cube_numbers(nums):
    for i in nums:
        yield(i**3)  # Here instead ot return we have used yield which will make it generator. we do not need to store the output in any variable like we did in above to store it in cube_list. Although cube_numbers is method it can duirectly be used as genertor object. 
cubes = cube_numbers([1, 2, 3, 4, 5]) #Now, when cube_number function is called, a generator is returned
print(type(cubes),cubes)
for temp in cube_numbers([1, 2, 3, 4, 5]): # here we are iterating over method cube_numbers which weill give the genertor object. we do not have any list created here so no memory wastage.
  print(temp)

#In the above script, the cube_numbers function returns a generator(as yield is used) instead of list of cubed number. It's very simple to create a generator using the yield keyword. Here we do not need the temporary cube_list variable to store cubed number, so even our cube_numbers method is simpler. Also, no return statement is needed, but instead the yield keyword is used to return the cubed number inside of the for-loop.


# Another example:

# A generator function that yields 1 for first time,  2 second time and 3 third time 
def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value) 

# Example to create generator on the fly for any lenght value:
 1 
def genfuncation(): 
    i = 1;   
    # An Infinite loop to generate yield.  
    while True: 
        yield i # we can have i*i if we need iterable of square of all elements or modifiy the i as per our iterable object requirement, like for all even number we can have i+1 and so.                
        i = i+1  # Next execution resumes  
                # from this point        
for num in genfuncation(): 
    if num > 10: 
         break    
    print(num)

# Excersice: A Python program to generate squares from 1 to 100 using yield and therefore generator 
  
# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
    i = 1;   
    # An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes  
                # from this point        
# Driver code to test above generator  
# function 
for num in nextSquare(): 
    if num > 100: 
         break    
    print(num)	


############## Decorator  ###################

#A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate. 

# Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.–

# To understand lets see the powerness of funcation first.
#Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.Functions can be defined inside another function and can also be passed as argument to another function.

#Essentially, decorators work as wrappers,
# modifying the behavior of the code before and after a target function execution,
# without the need to modify the function itself, 
#augmenting the original functionality, thus decorating it.


#*********  What you need to know ***********************
#in python functions are first class citizens they are objects and that means we can do
#a lot of useful stuff with them

# Different funcation capabilities to be understand before getting into decorator:

#A) Assigning Functions to Variables
#To kick us off we create a function that will add one to a number whenever it is called. We'll then assign the function to a variable and use this variable to call the function.
def plus_one(number):
    return number + 1
add_one = plus_one
add_one(5)	

#B)Defining Functions Inside other Functions
#Next, we'll illustrate how you can define a function inside another function in Python. 
def plus_one(number):
    def add_one(number):
        return number + 1
    result = add_one(number)
    return result
plus_one(4)
	
#C) Passing Functions as Arguments to other Functions
#Functions can also be passed as parameters to other functions. Let's illustrate that below.
def plus_one(number):
    return number + 1
def function_call(function):
    number_to_add = 5
    return function(number_to_add)
function_call(plus_one)	

# D) Functions Returning other Functions
#A function can also generate another function. 
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()

# E) Nested Functions have access to the Enclosing Function's Variable Scope
#python allows a nested function to access the outer scope of the enclosing function. This is a critical concept in decorators -- this pattern is known as a Closure.
def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message) # Here enclosing funcation message_sender is having access to 'message'
    message_sender()
print_message("Some random message")


# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

#Syntax:

@gfg_decorator  # Decorator.
def hello_decorator(): 
    print("Gfg") 
  
'''Above code is equivalent to -   
def hello_decorator(): 
    print("Gfg")       
hello_decorator = gfg_decorator(hello_decorator)'''

#In the above code, gfg_decorator is a callable function, will add some code on the top of some another callable function, hello_decorator function and return the wrapper function.

# Decorator example:

# defining a decorator 
def hello_decorator(func):   
    # inner1 is a Wrapper function in which the argument is called  .     
    # inner1 function can access the outer local functions like in this case "func" .
    def inner1(): 
        print("Hello, this is before function execution") 
        func()   # calling the actual function now inside the wrapper function.
        print("This is after function execution")           
    return inner1     

# Now we can use the decorator in our methods in two different syntax.
#syntax 1:
@hello_decorator	 # Here we are using decorator funcation in which funcation_to_be_used will be passed as an arguments. like hello_decorator(function_to_be_used).
def function_to_be_used(): 
    print("This is inside the function !!") 
function_to_be_used() 

# Syntax 2:	(This is equivalent to syntax 1 , ultimatley syntax 1 will also be converted something as below)
def function_to_be_used(): 
    print("This is inside the function !!") # passing 'function_to_be_used' inside the decorator to control its behavior or add to its behaviour
function_decorator_call = hello_decorator(function_to_be_used)     
# calling the function 
function_decorator_call() 	


# Excersise 1:decorator that will convert a sentence to uppercase.
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
def say_hi():
    return 'hello there'
decorate = uppercase_decorator(say_hi)
decorate()

# With east syntax:
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()


# Excersise 2: Applying Multiple Decorators to a Single Function
def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper
	
@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
say_hi()	

# Exc ersie 3: Accepting Arguments in Decorator Functions

#Sometimes we might need to define a decorator that accepts arguments. We achieve this by passing the arguments to the wrapper function. The arguments will then be passed to the function that is being decorated at call time.

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")

###############  Lamda Function ###############

# A lambda function is a small anonymous function . 
# A lambda function can take any number of arguments, but can only have one expression
#One is free to use lambda functions wherever function objects are required.
#You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
#Lambda expression also known as anonymous fun. becoz used only one time becoz of that we dont give name nor use def keyword.so instead of keyword def and fun name we replace it with keyword lambda

#NOTE:- lambda is an expression not a statement
#lambda's body is a single expression not a block of statements.
#Becoz it is limited to an expression a lambda is less general that a def. 
#we can only squeeze design to limit prog neating.
#lambda is designed for coding simple functions and def handles larger tasks.


# By using lambda you can simplifies the syntax of simple or small funcation:
#syntax: 
lambda arguments(argument1, argument2, ...argumentn) : expression

# Example:  
# showing difference between def() and lambda(). 
def cube(y):  # This is simple method . 
    return y*y*y; 
print(cube(5))  
 
g = lambda y: y*y*y  # this is lambda expression equivalent to above method. lambda funcation returns funcation object and it is quite faster. 
print(g(7)) 
  
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# Example:
x = lambda a : a + 10
print(x(5))
 
# Lambda funcation with multiple argument
x = lambda a, b : a * b
print(x(5, 6))

# lambda function inside another funcation  
def myfunc(n):
  return lambda a : a * n # here funcation myfunc is returning the another funcation.

mydoubler = myfunc(2) #mydoubler will have the funcation object and 2 will be passed as n.
mytripler = myfunc(3)
print(mydoubler(11)) # 11 will be passed as value a.
print(mytripler(11)) 

#we can use lambda in conjuction with map and filter
#Now in case of map we do write a function and then call inside map
#this thing can be more optimised by using lambda


li1=list(map(lambda num:num**2 , mynumbers))
print(li1)
   
#covert checkevene fun to lambda
li2=list(filter(lambda num:num % 2 ==0 ,mynumbers))
print(li2)
#write a lambda to grab first char of names
allnames=['Sachin','Ashish','Rahul','Mahendrasingh']
li3=list(map(lambda name:name[0],allnames))
print(li3)

#write a lambda to reverse the names
li4=list(map(lambda n:n[::-1],allnames))
print("Reversed names ---->",li4)
#Example
allcars=(lambda a='FordFigo',b='Audi',c='Swift':a+b+c)
print(allcars('Accent','Wolkswagen'))
