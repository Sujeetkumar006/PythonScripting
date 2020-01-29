


#************************************  Lambda ************************************


#Lambda expression
#also known as anonymous fun. becoz used only one time
#becoz of that we dont give name nor use def keyword
#so instead of keyword def and fun name we replace it with keyword lambda

#General form of lambda --> lambda arg1,arg2,....argN: expression using arg
#NOTE:- lambda is an expression not a statement
#lambda's body is a single expression not a block of statements.
#Becoz it is limited to an expression a lambda is less general that a def. 
#we can only squeeze design to limit prog neating.
#lambda is designed for coding simple functions and def handles larger tasks.

#Scenario
'''
def squareUp(num):
    result=num*num
    return result

print(squareUp(3))
'''
#we can optimise above code
'''
def squareUp(num):
    return num **2

print(squareUp(3))
'''
def squareUp(num):return num **2

print(squareUp(3))

sq=lambda num:num **2

print("------------->",sq(2))


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




























































#Many more things are here for lambda http://www.bogotobogo.com/python/python_functions_lambda.php




#Map example :- built in used for functional programming
#one of the common things we do with list and other seq is applying an operation to each item and collect the result.
#Example need to square up all items in list. That can be done by for loop

items=[1,2,3,4,5]
squared=[]
for each in items:
    squared.append(each ** 2)

print(squared)


#To do this we have map which takes two param fun and iterable
#map(afunction,aseq)
#IMP NOTE: - here we will be passing fun name as an argument not as a fun call()

def squareNumber(x):
    return x**2

list1=[]
list1=list(map(squareNumber,items))
# cant print list directly
print("-------->",list1)
for i in list1:
    print(i)

'''
#Example2
def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]

names=['Andy','Eve','Sally']

listofnames=list(map(splicer,names))
print(listofnames)
'''

#Filter will return true or false

def check_even(num):
    return num%2==0

mynumbers=[1,2,3,4,5,6]
#only want to grab even number

li=list(filter(check_even,mynumbers))
print(li)
