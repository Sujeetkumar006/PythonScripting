
#********** Decorator ****************************************
#it allows us simple modifications to callable objects like functions,methods,or classes
#we will deal with fun 

#Essentially, decorators work as wrappers,
# modifying the behavior of the code before and after a target function execution,
# without the need to modify the function itself, 
#augmenting the original functionality, thus decorating it.


#*********  What you need to know ***********************
#in python functions are first class citizens they are objects and that means we can do
#a lot of useful stuff with them

#TODO1 assign fun to vars
def greet(name):
	return "Hello"+name

	
greet_someone=greet
print(greet_someone("Swati"))


#TODO2 define fun inside another fun
def greet(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result

print (greet("John"))


#TODO3 fun can be passed as param to other fun
def greet(name):
   return "Hello " + name 

def call_func(func):
    other_name = "Swati"
    return func(other_name)  

print (call_func(greet))


#TODO4 functions can return another fun
def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print (greet())

#https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

#NOOOOO TODO5 Inner functions have access to enclosing scope


#Time to apply decorators


	
def p_decorate(func):
	def func_wrapper(name):
		return "<p>{0}</p>".format(func(name))
	return func_wrapper
	
@p_decorate
def get_text(name):
	return "Hi {0} How are you ?".format(name)


print(get_text("Swati"))


print("****************How to apply multiple decoartors***************************************")

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
   return "Hi, {0} How are you".format(name)

print get_text("John")


print("**** In above case we are writting redudant code .instead we can write simple codeee")

def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
@tags("h1")
def get_text(name):
    return "Hello "+name

print(get_text("John"))

print("*************************************************************************")


#NOTE:- decoratos with class is pending




'''
Excellent examples 
Example 1. 
def cough_dec(func):
	def func_wrapper():
		#code b4 fun call
		print("cough")
		func()
		#code after fun call
		print("cough")
	return func_wrapper


@cough_dec
def question():
	print('Can you give me a discount on that?')
	
	
@cough_dec
def answer():
	print('It is only 50p you cheapskate')



question()
answer()


Example 2. 
#Not we need to cal performance of our code. and its not good pactice to write 
#those repeted lines in each and every fun
#so assign this task to decorator and then apply this to all those fun
#also code of time is not part of business logic

import time
def time_it(func):  #Note:- over here we just want fun name we dont want to exe it.
	def wrapper(*args,**kwargs):  #use this -->  f=calc_square(array) and f=calc_square
		start=time.time()
		result=func(*args,**kwargs)
		end=time.time()
		print(func.__name__+" took "+ str((end-start)*1000)+"mil seconds")
		return result
	return wrapper

@time_it
def calc_square(numbers):
	result=[]
	for number in numbers:
		result.append(number*number)
	return result
	
@time_it
def calc_cube(numbers):
	result=[]
	for number in numbers:
		result.append(number*number*number)
	return result

array=range(1,100000)
a1=calc_square(array)
a2=calc_cube(array)

Example 3:




'''


	
	
	
	
	
	
	
	
	

https://www.thecodeship.com/patterns/guide-to-python-function-decorators/








































