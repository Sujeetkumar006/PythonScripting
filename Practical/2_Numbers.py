################### Topics #######################

#What is variable
## DIfferent between mutable and immutale type Variable Type: Change in value in same memory (Mutable) and change in memory address when value changes (immutable).
## Stack and Heap memory : Queue and List . RAM and ROM
#python is case sensitive
# Precedence 

#################### Topics #########################

###############Naming rules #########################

#must begin with letter or _.
#Followed by any number of letters, digits, or underscores
#Should not be a built-in name or Keyword
#PEP 8, the style guide for Python, recommends lowercase with underscores as necessary: first_name

# Immutable types: String , Integer, floating , Tuples .
# Mutable: Lists, dictionaries, and sets are mutable

# Python memory allocation for small and large values : Dynamic allocation: Bit/Bytes: Medical shop example

############## Variables ############################

#int, FLoat, String is immuable still below will  give fdififerent id

a=10.12
b=10.12
print(id(a))
a=20.12  
print(id(a))

# FOr int -5 to 256 use same id , for FLoat every variable will have different id even having same value.
#for  string small string like "Hello" will have same address ut long string will have different address.
# TO prove these are immutale we have to mdify the variale value and check if memory adress is changig.

###################################################

Item_name="Computer"
Item_qty=10
Item_value=12000.11

print(Item_name)
print(Item_qty)
print(Item_value)

#Multiple assignment

x=y=z=1
print(x)
print(y)
print(z)

a,b,c=10,'ABCD',11.11
print(a)
print(b)
print(c)

#we can reuse the variable by simply assigning new values
x=100
print(x)
x="Python"
print(x)

#Exercise 1. swap two numbers
x=10
y=20
print("Before swapping",x,y)
x,y=y,x
print("After swapping",x,y)


print("********************Data Type*********************************")
#Numbers , String , List, Tuple , Dictionary

###Numbers  --> int float double complex

a=1243
print(type(a))
print(id(a))
print(a)

b=-123
f1=11.11
f2=.22
a=15555.3838888888888888888888888888888888
b=1555544444444444444444555555555555555555555556666666666666.3838888888888888888888888888888888
c=222222222222233333333333333333333455555555555555555555999999999999999666666666666
print(a)
print(b)
print(c)

# No limit on Lenght of Integer and float. Only values after floating point (Decimal values use to roud off ) 

# Updating variables
count=100
print (count)
count+100
print(count)
count=count+100
count+=100
print(count)

# Compare variables:
a=10
b=a
c=10
print(a is b)
print(a is c)  # Check memory address point to same object
print(a==b) # check values
print(a==c)

###complex numbers   
aComplex= -8.3 - 1.4j
print("*********************")
print(aComplex)
print(type(aComplex))
print(id(aComplex))
print(aComplex.real)
print(type(aComplex.real))
print(id(aComplex.real))
print(aComplex.imag)
print(type(aComplex.imag))
print(id(aComplex.imag))
print(aComplex.conjugate())


### Boolean

print(True)
print(False)
print(True==1)
print(False==0)
#python assumes any non-zero and non-null values as TRUE. And if it is zero or null then it is assumed as false

#Use booleans numerically

foo=42
bar=foo <100
print('**************************')
print(bar)
print(bar+100)
print('%s'%bar)  #if we print using %s it print true 
print('%d'%bar)  #if we print using %d it orints one


# Results of operations on objects of the same type yield results of the same type
# Results of operations on objects of mixed types are converted to the bigger type
# Python 3 integer division always yields a floating point result

5/3
5/3.0
5*3
5%3
5//3
5/-2

# The float() and int() functions return the argument in the specified type
 #Argument may be the string representation of a numeric value
 #Argument may be an expression

num='100'
num1=100
num2=100.12
print (int(num))
print (float(num))
print (int(num1))
print (float(num1))
print (int(num2))
print (float(num2))

num='100.12'
num1=100.12
print (int(num)) # Will throw error while converting STRING float values to int .
print (int(num1))  # NOT throw error and work fine while converting normal float to int. 
print (float(num))
print (float(num1))

num='abc'
print (int(num)) # Will throw error 
print (float(num)) # Will throw error

print (int(9/5))
print (int(9/5.0))
#print (int('9/5'))  # Throw an error : int() method can not have STRING expressions. 
print (float(9/5.0))
#print (float('9/5.0')) # Throw an error: float() method can not have STRING expressions.

# Converting Int/Float to String
num=100
print(str(num))


#The oct(), hex(), and bin() functions return the argument as a string in the specified base
num1 = 12
print(oct(num1))
print(hex(num1))
print(bin(num1))

Oct,Hex, bin to base 10 
print(int(0b1100))
print(int(0xc))


#Delete Variable:

del var1[,var2[,var3[....,varN]]]] 





	
	