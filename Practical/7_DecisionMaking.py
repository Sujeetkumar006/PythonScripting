#Decision making

#Yield a Boolean True or False value
# 	• The strings 'True' and 'False' both evaluate to Boolean True

#Types of conditional expressions
#	Object identity, is
#	Arithmetic relational; e.g., > or ==
#	Strings use the same equality and inequality operators as numeric objects


# Several simple conditions joined by Boolean operators
#	and yields True if both operands are True
#	or yields True if either is True 
#	not reverses the Boolean value


"""Begin with a header statement that is terminated by a colon, :
Followed by a group of statements that are syntactically treated as a unit—a suite
• A code block
• For example: a loop body
Following statements are tied to the header based on the same 
indentation
• One of Python’s readability features
•  Python Enhancement Proposal (PEP) 8 recommends indentation of four spaces
End of code block detected by lack of indentation
Or an empty line if entering statements into the interpreter"""

#Evaluates an expression’s Boolean value and executes the associated block
• False is 0, empty string, empty collection, and None; anything else is considered True


# simple if else 
a=10
if a==10:
    print("Hello")
else:
    print("Mpt Hello")
	
	
# Other type of if else: 	
a=100
#Type1
if a is 10 :
    print("Hello User")
    print("statement2")
print("Statement3") #This statement is not associated with if block.

#Type2
if a== 100 :
    print("Using == operator to check equality")

    
#Type3 with parenthesis
if (a==100): print("value is 100")
print("Good Bye !!!")


#Type4
num1=10
if num1:
    print("True")
    print(num1)

#Type5
num2=0
if num2:
    print("True")
    print(num2)
print("Normal prog execution starts here...1")    

#Type6
flag=None
if flag:
    print("True")
print("Normal prog execution starts here...2")


#Type7  #oops python is case sensitive and T is capital here in True
var=True
if var:
    print("It's True")


# Syntax of If and elif. The block associated with first condition that yields True is executed• The else: block is executed if no condition yields True.

if conditionA:
	blockA
elif conditionB:
	blockB
elif conditonC:
	blockC
else:
	blockD
restOfCode

#####
# As soon as the first criteri wil match the other conditions will not be checked.
a=10
if a>5:
    print("Helo")
elif a>7: 
    print ("Hi")
elif a>9:
    print('Hey')
else:
    print('Not hello')

#python assumes any non-zero and non-null values as TRUE. And if it is zero or null then it is assumed as false

#Evaluates an expression’s Boolean value and executes the associated block
• False is 0, empty string, empty collection, and None; anything else is considered True	
	
#Try with a=0,[],(),'',None,True,False,'True','False' 	
a='True'
if a:
    print("Hello")
else:
    print("Mpt Hello")	    

#---------- IF ELSE ---------------------


age=19
if age > 18:
    print("Welcome to vote")
    print("statement 1")
else  :
    print("Need to wait")
    print("statement 2")
print("Normal program starts here")
    


#---------- ELSE IF Ladder -------------------

a=10
if (a>=20):
    print("Condition is true")
elif (a>=10):
    print("Checking second value")
else:
    print("All conditions are false")

# Switch case with Python . 
	
choice='a'	
choice=input("Enter your choice among a,b,c")
if choice == 'a': 
	function_a() 
elif choice == 'b': 
	function_b() 
elif choice == 'c': 
	function_c() 
else: 
print "Invalid choice."
	
	
		
	
	
#----------- NESTED IF ELSE ------------------------

num=100
if num>= 200:
    print("True")
else:
    if num>=150:
        print("Checking second value")
    else:
        print("All conditions are false")
        


#---- AND Or operator : Multi comparison in if else. 

x=False 
y=True
if x and y:
	print('Both x and y are True')

# Multi condition : AND and OR rule will be followed..if all true then true , if anything false then all false. 	
a=10
b=20
c=30
if a<b<c:
    print('Hello')

	
## and/or condition in if:
a=200
b=300
c=50
if (a==200 and b==300): 
    print("value is 100")
print("Good Bye !!!")	
	
# If with in statement: simiar as is statement.
name="Sachin"
listOfPlayers=["Rahul","Saurav","Sachin"]
if name in listOfPlayers:
	print("Selected in team")
	

	
# 	The pass Statement: Explicitly does nothing,Serves as a placeholder where a statement is required
if not sea:
	pass 
else:
	print ('Hello')

	
#code optimization write it in single line
#if n is greater than 500, n is multiplied by 7, otherwise n is divided by 7
n=150
result= n*7 if n> 500 else n/7
print(result)







#*****************  PROG TIP **********************************************************

'''

0 is false; all other numbers are true.

An empty string ("") is false, all other strings are true.

An empty list ([]) is false; all other lists are true.

An empty tuple (()) is false; all other tuples are true.

An empty dictionary ({}) is false; all other dictionaries are true.


The following are defined as having false values in python


None
False (Boolean)
Any numeric zero:
0 (integer)
0.0 (float)
0L (long integer)
0.0+0.0j (complex)
"" (empty string)
[] (empty list)
() (empty tuple)
{} (empty dictionary)
'''

#Exercise 1. write a program to accept number from user and check its data type



	
	

	
