#---------- Looping   FOR  used for sequence like list set tuple string dict-----------------------

#the first item in sequnce is assigned to iterating var. next stmt block is executed
#it repeats till until the entire sequence is exhausted. var has the final value processed

#Local variable of loop accessed outside the loop?.Yes it is possible in pyhton. Python loop variables are global variables. 
 
 a=[10,20,30,40,50,60,70,80]
c=50
print(id(c))
for i in a:
    #print(i)
    print(id(c))
    c=10000
    print('After Reassignment in loop',id(c))
print('After loop',id(c))    
print('Printing b',c)

# iterables for loop : #list/tuple/string/Dict:key/Dict:value/ Set (Set should not be used as will cause unexpected error )

for var in 1,2,3:
	print(var)
print(var)	

for fruit in 'Apple','Orange','Strawberry':
	print(fruit)


for letter in 'python':
    print("current letter is",letter)
	
# Local and global variable in Loop. Any variable defined under loop can be used outside. 
temp=0
for temp in 'python':
    a=10
    print("current letter is",temp)
print(a)    
### 
	
names=['Akshay','Payal','Nitin','Ashish']
#To print each element in array
for name in names:
    print("current name is ",name)

# For dict methods keys(), values(), and items() can provide an iterable sequence
	
a={'abc':123, 'pqr':234}
for b in a.keys():
  print(b)
for b in a.values():
  print(b)
for b in a.items():
  print(b)
for b,c in a.items():
  print(b)
  print(c)
	
	
# Nested for loop.	
	
#To print each character in in each element e.g. P a  y a l
for name in names:
    for letter in name:
        print("current name is ",letter)

# 
a=[200,400,500]
b=[20,50]
c=[]
for temp1 in b:
    for temp2 in a:
        c.append(temp2-temp1)
print(c)         


# assignment:Create a list of keys from codes that are also keys in caps

codes = {'France': 33, 'Japan': 81,
'GreatBritain': 44, 'USA': 1}
caps = {'France': 'Paris', 'Cuba':
'Japan': 'Tokyo'}
countries = []
for code in codes: 
 if code in caps:
  countries.append(code)
countries



'''range() function
1.we can generate a sequence of numbers using range() function.
    range(10) will generate numbers from 0 to 9 (10 numbers)
2.we can also define the start,stop,step size as range(start,stop,step size) --> step size defaults to 1 if not provided
3.This function dose not store all the values in memory. it would be inefficient. so it remembers start stop step size and generates the next number on the go


'''


#range(m,n,s)
#– A list of every s value from m to n -
#– Both m and s are optional


#example1 outputs range(0,10)   range(number)
print("----->",range(10))   


#example2 outputs[0,1,2,3,4,5,6,7,8,9]  range(lower upper)
print(list(range(10)))
#or tuple(range(10))

#example3 outputs[2,3,4,5,6,7]
print(list(range(2,8))

#example4 outputs[2,5,8,11,14,17]    range(lower , upper,step)
print(list(range(2,20,3)))



print("********************Print with index *********************************")
#Iterate by sequence index
colour=['Blue','Green','Orange','Pink']
#but we need range for this

for index in range(len(colour)):
    print("Current element is at [",index,"]  -->",colour[index])

#if 0 to 4 then prints 0 1 2 3
for i in range(0,4):
    print(i)
    
 for i in range(4):       # this is same as range (0,4), lower value/start default value will always be 0.
    print(i)
	
#if 1 to 4 then prints 1 2 3    
for i in range(1,4):
    print(i)


#print 0 1 2 3 4
for i in range(5):
    print(i)

#prints 3,4,5
for i in range(3,6):
    print(i)


# Two different syntax:

a= [1,2,3,4,5]
for b in range(len(a)):
 print (a[b])
for b in a:
 print(b)	
	
print("**********Range ***************")
#prints 3,5,7
for i in range(3,8,2):  #here  it prints number from 3 to 8 by skipping 2 numbers
    print(i)
    


#Write a program to find sum of all numbers stored in a list
allNumbers=[1,2,3,4,5]

sum=0

for i in allNumbers:
    sum=sum+i

print("Sum is  ",sum)  

#***************************  for  loop with else  ***************************************
#A for loop can have an optional else block as well . The else part is executed if the items in seq used in for loop xhauts

#break stmt can be used to stop for loop in such case else part is ignored

### Control flow with in loop: 
#break: 

#break terminates the loop
#continue returns flow control to the top of the loop
#else: defines a block of code executed after the loop terminates normally Without a break. It will always execute if the loop has not be terminated by break. 


digits=[1,2,3]

for i in digits:
    print(i)
else:
    print("no item left")

print("----------------------------------------------last line")

i1=10
for i1 in range(10):
    print(i1)
    if(i1==10):
        print("100")
else:
    print(i1)  #To see last value of i1

# anothr example

airports = ['LAX', 'HNL', 'YYZ']
for airport in airports:
	if airport == 'HNL':
		break                         # Break as soon as find the HNL. ELse will not be executed.
	print airport
else:
print 'The'
for airport in airports:
	if airport == 'HNL':
		continue                      ## Contiue with other  items in list except HNL.
	print airport
else:
print 'The'
	
	
"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))
   
   
   
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

   
#### While Looping
: 
#---------- Looping   WHILE -----------------------

#Evaluates the Boolean value of an expression
#• Executes the loop body so long as the expression is True
#– Terminates on False or execution of a break


x = 0;
while (x < 5):
     print(x)
     x += 1

	 
#infinite loop
x = 10;
while (True):
     print(x)
     x += 1
	 
	 
'''	 
The else clause is only executed when the condition is false 
it may be the first time it is tested and will not execute if the loop breaks, 
or if an exception is raised. 
If a break statement executes in first program block and 
terminates the loop then the else clause does not execute
'''


x = 0;
s = 0
while (x < 10):
     s = s + x
     x = x + 1
else :
     print('The sum of first 9 integers : ',s)  
	 	 	 

x = 1;
s = 0
while (x < 10):
     s = s + x
     x = x + 1
     if (x == 5):
          break
else :
     print('The sum of first 9 integers : ',s)        
print('The sum of ',x,' numbers is :',s) 	 
	 


#Program to calculate temperature from Fahrenheit to Celsius.
keep_calculating = 'y'

while keep_calculating == 'y':
    fah = int(input("Enter temperature in Fahrenheit: "))
    cel = (fah - 32) * 5/9
    print(format(fah, "0.2f"), "°F is same as", format(cel, "0.2f"), "°C")
    keep_calculating = input("\nWant to calculate more: ? Press y for Yes, n for N: ")

print("Program Ends")


#************************Break Continue pass keywords  ************************************

###Break
num_sum = 0
count = 0
while(count<10):
    num_sum = num_sum + count
    count = count + 1 
    if count== 5:
        break
print("Sum of first ",count,"integers is: ", num_sum)


var =10
while var >0:
    print("current var val is",var)
    var=var-1
    if var==5:
        break
print("good bye!!!")  


#### Continue

for x in range(7):
    if (x == 3 or x==6):
        continue
    print(x)

	 
### pass
#when nothing to execute


for i in [1,2,3,4,5]:  
    if i==3:  
        pass  
        print("Pass when value is",i ) 
    print(i)

for letter in 'Python':
    if letter == 'h':
        pass
        print("This is a pass blocl")
    print("Current letter is",letter)

print("Good bye!!")
 
	 

#In Python programming, pass is a null statement. 
#The difference between a comment and pass statement in Python is that, while the interpreter ignores a comment entirely, pass is not ignored.
#However, nothing happens when pass is executed. It results into no operation (NOP).
#We generally use it as a placeholder.
#Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future.
#They cannot have an empty body. The interpreter would complain. So, we use the pass statement to construct a body that does nothing.

# pass is just a placeholder for
# functionality to be added later.
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
	 
# assignement:

1) write a prorgram to find the number of occurance of each char in below list.

a=['Sujeet','Ateev','Saiket','Vivek','Satyam']
countdict={}
for temp in a:
    for temp1 in temp:
        if temp1 in countdict.keys():
            countdict[temp1]=countdict[temp1]+1
        else:
            countdict[temp1]=1
print(countdict)

a=['Sujeet','Ateev','Saiket','Vivek','Satyam']	 

=================
2) write your method for find in string:

arg1='adgdfjgkdfgkjsdf'
#arg1.find('d')
counterindex=0
for temp in arg1:
    if 'd' is temp:
        print(counterindex)
        break
    counterindex =counterindex+1    
    