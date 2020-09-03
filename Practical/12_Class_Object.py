
#This is for classes , objects ,constructor ,inheritance ,overriding ,polymorphism ,access modifier

# OOPS: class, object, polymophism (method overloading),inheritance, encapsulation, Data abstraction (access modifier). 

#self keyword: self keyword in python is like "this" pointer of java. on top of that self has to be the very first parameter.
#self is naming convention we can give any name.

#Special Functions in Python
#Class functions that begins with double underscore __ are called special functions in Python. This is because, well, they are not ordinary. The __init__() function we defined above, is one of them. It gets called every time we create a new object of that class. There are a ton of special functions in Python.

"""Pros and Cons of OOP
Following are some of the advantages of object-oriented programming:

Object-oriented programming fosters reusability. A computer program is written in the form of objects and classes, which can be reused in other projects as well.
The modular approach used in object-oriented programming results in highly maintainable code.
In object-oriented programming, every class has a specific task. If an error occurs in one part of the code, you can rectify it locally without having to affect other parts of the code.
Data encapsulation (which we will study later in the article) adds an extra layer of security to the program developed using the object-oriented approach.

It has some downsides as well, some of which have been enlisted below:
Detailed domain knowledge of the software being developed is needed in order to create objects. Not every entity in software is a candidate for being implemented as an object. It can be hard for newbies to identify this fine line.
As you add more and more classes to the code, the size and complexity of the program grows exponentially.
"""


# attributes and methods in class.


class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass
print(MyNewClass.__doc__)
	

# A class with no attr only default constructor, Need to put self compulsory,its positional arg

#Constructor:  __init__() function. This special function gets called whenever a new object of that class is instantiated.We normally use it to initialize all the variables.
#Constructor is optional and any class can have only one constructor.No multi constructor in Python like java. We can use deafult keyword argrument variable as a work arround.
#We do not explicitly call the __init__ method. This is the special significance of this method.


class Emp():
    def __init__(self): 
        print("inside default ctor")
obj1=Emp()
print(type(obj1))

class Employee():
    def __init__(self,param1='abc',param2):
        self.param1local=param1
        self.param2local=param2

    def some_method(self):
        #perform some action
        print(self.param1local)
obj=Employee(10,20)
obj.some_method()
obj.param1local
obj.param1localnew=30 # creating a new object variable from outside of class, this variable will be limited to only current object 'obj' of class Employee and not for other object.

#class keyword and creating attribute

#Way 1 to put attribute in constructor same name empid
class Employee():
    def __init__(self,empid):
       self.empid=empid 

myObj1=Employee(1111)
print(type(myObj1))
myObj1.empid=111
print(myObj1.empid)

#way2 toput diff names like below
class Employee():
    def __init__(self,employeeid,empname,basicsalary):
       self.empid=employeeid
       self.empname=empname
       self.basicsalary=basicsalary


#now in this case empid is attribute or data member. and employeeid is local var

obj1=Employee(555)
print("Id is",obj1.empid)
#print("Id is",obj1.employeeid) #wont work
obj1=Employee(employeeid=123)
print("Id is",obj1.empid)
emp1=Employee(1111,"Sujeet",12300)
print(emp1.empid,"  ",emp1.empname," ",emp1.basicsalary)

       
#Note:- in above case we are not mentioning data type. as python do not do typecheck
#and it will print it as it is

emp2=Employee(1111,"Sujeet","2500000")
print(emp2.empid,"  ",emp2.empname," ",emp2.basicsalary)


# Variables in class: instance variables and class variables


#Class variables are shared - they can be accessed by all instances of that class. There is only one copy of the class variable and when any one object makes a change to a class variable, that change will be seen by all the other instances. Class object is refered/accessed by class name and not reference object name. Class variables are assigned outside of any method is class and used by class name inside the class. Somethimes it also be used as "self.__class__.variablename" but standared sytax is "class.variablename". Class variable in python is similar to static variable in java.

#Object variables are owned by each individual object/instance of the class. In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the field by the same name in a different instance. This is refered by object refrence variable. object variables are used by self inside the class

# Namespace: object variable with the same name as a class variable will hide the class variable!. SO if some variable is at both class and object level , class variable will be refered by class name and object one will be refered by object reference.  

class Employee():
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    #NO NEED TO USE SELF KEYWORD

    companyname="Accenture"
    def foo():
        print("foooo")   
    def __init__(self,employeeid,empname,basicsalary):
       self.empid=employeeid
       self.empname=empname
       self.basicsalary=basicsalary
       self.companyname='Abc'
    def displayData(self):
        print(self.empid,"  ",self.empname," ",self.basicsalary," ",Employee.companyname)
    def calculateTotalSalary(self,variableBonus):
        return self.basicsalary+variableBonus       

#It may happen that is common in all object. need to define a attribute at class level

emp2=Employee(1111,"Sujeet",2300000)
#print(emp2.empid,"  ",emp2.empname," ",emp2.basicsalary," ",emp3.companyname) #will give error
print(emp2.empid,"  ",emp2.empname," ",emp2.basicsalary," ",Employee.companyname,' ', emp2.companyname)
Employee.foo()

# Methods in class: instance methods, static methods, and class methods
#method is a function that is inside a class

#Instance methods: Those method having self as argument/parameter that is instance method and can be access by creating object of class. This is mostly used method. these methods can modify object as well as class state means it can access both class and object variables.   

# class method: Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called. Because the class method only has access to this cls argument, it can not modify object instance state/variable. Class method can only modify/access class variables. class method can’t access specific instance data, but they can call other static methods.

#Static Methods:Static methods are methods that are related to a class in some way, but don’t need to access any class-specific data. This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters). Therefore a static method can neither modify object state/variables nor class state/variables.

#Summary:
#Instance Methods: The most common method type. Able to access data and properties unique to each instance.
#Static Methods: Cannot access anything else in the class. Totally self-contained code.
#Class Methods: Can access limited methods in the class. Can modify class specific details.


class MyClass:
    rollnumer=123
    def __init__(self,name):
        self.name=name
        
    def method(self):
        print(self.name,MyClass.rollnumer) # instance method can access both class and insatnce variable.
        MyClass.rollnumer=345 # modifying the class variable . 
    @classmethod # decorator, class method
    def classmethod(cls):
        #print(self.name) #this will throw an error as instance (self) variables can not be used from class method.
        print(MyClass.rollnumer) # class method can only access class variables.
        
    @staticmethod # decorator, static method. for static method decorator is optional. we can comment this line. 
    def staticmethod():
        #print(self.name) #this will throw an error as instance (self) variables can not be used from static method.
        print(MyClass.rollnumer) # #this will throw an error as class (cls) variables can not be used from static method.
        print ('static method called')
    
obj=  MyClass('sujeet') 
#print(obj.name) # instance variable, needs to be called by instance object.
#print(MyClass.rollnumer) # class variable, needs to be called by class name. 
#obj.method() # instance method needs to be called by instance object.
#print(MyClass.rollnumer) # class variable, needs to be called by class name.
#obj.classmethod() # class method can be called by both object and class reference but should be called by class name only. 
#MyClass.classmethod() # class method can be called by both object and class reference but should be called by class name only.
obj.staticmethod() # static method can be called by both object and class reference but should be called by class name only.#Behind the scenes Python simply enforces the access restrictions by not passing in the self or the cls argument when a static method gets called using the dot syntax.
#MyClass.staticmethod() 

############ Inheritance , polymorphism (overloading and overriding).

#Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called child classes, and the classes that child classes are derived from are called parent classes

#It’s important to note that child classes override or extend the functionality (e.g., attributes and behaviors) of parent classes. In other words, child classes inherit all of the parent’s attributes and behaviors but can also specify different behavior to follow. The most basic type of class is an object, which generally all other classes inherit as their parent.

#syntax:
class BaseClass():
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
  
 
# Parent class:   
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")
	def dance(self):
        print("I am dancing")
a1=Animal()
a1.who_am_i()
a1.eat()

#lots of factores of animal class can be resued to define dog class: child class.

# Child class.
class Dog(Animal):
    def __init__(self): # init/constructor defination in child class, this is optional , if this is not defined the child object will be initalize with the parent class init method syntax/argument. 
        Animal.__init__(self) # parent class init call from child class. This is again optional if needed to initialize/assign parent class variables/attributes.   
        print("Dog created") # own code of child class init method.
    #METHOD OVERIDDING
    def who_am_i(self):   # Method overriding, updating the parent class method completely.
        print("I am dog")
    def eat(self):         # Method overriding, updating the parent class method.
        Animal.eat(self)   # Calling the parent method funcationality first and then addimg the ectra code in next line.
        print("Dog eating")
    def bark(self):           # new method in child class.
        print("WOOF !")
		# if we do not want to modify/override the method from parent class (example : dance () method)we do not need to mention it in child class, by default those will be part of child class with the same defination/funcationality in parent class.
print("----------------->")
d1=Dog()
#we can resue method from animal class
d1.who_am_i()
d1.eat()
d1.bark()
d1.dance() # dance method is not defined in child class but still it can be accessed by child class reference as it is member of child class by default due to inheritance, defination of dance method will be same as defined in parent class as it has not been overriden in child class. 

#overriding and overloading: Overloading occurs when two or more methods in one class have the same method name but different parameters. Overriding means having two methods with the same method name and parameters (i.e., method signature). One of the methods is in the parent class and the other is in the child class.

## python does not supports method overloading. We may overload the methods (syntatically it is allowed) but can only use the latest defined method so overloading is not applicabke in python.

def product(a, b):  # first method 
    p = a * b 
    print(p) 
       
def product(a, b, c):  # method overloading 
    p = a * b*c 
    print(p)      
# product(4, 5) # This code will not work as method overloading will not work.   
product(4, 5, 5)# This line will call the second product method.

# *** why python does not support method overloading?. in python we have varibale argument *args, so anyways it can take variable argument which is nothing but indirect overloading. 
def product(*args)

#other funcations:

#The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup.

issubclass(Dog, Animal)

#The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class

isinstance(d1, Dog)

# dir(d1) : this will give the details of attributes and methods to class. 

#Multi Inheritance: Python support multi inheritances:
# syntex:
class A:        # define your class A
.....
class B:         # define your class B
.....
class C(A, B):   # subclass of A and B
.....
####################
## Type 1
class A:
    def explore(self):
        print("explore() method called") 
class B:
    def search(self):
        print("search() method called") 
class C:
    def discover(self):
        print("discover() method called") 
class D(A, B, C):
    def test(self):
        print("test() method called") 
d_obj = D()
d_obj.explore()
d_obj.search()
d_obj.discover()
d_obj.test()

## Type 2: in which we have same method name in two parent class. 
class A:
    def explore(self): # method explore defined in class A.
        print("explore() method in class A") 
class B:
    def search(self):
        print("search() method called") 
    def explore(self): ## method explore defined in class B.
        print("explore() method in class B")     
class C:
    def discover(self):
        print("discover() method called") 
class D(A, B, C): #Mupliple inheritance. Here which ever class we write first will have pref while invoking same merhods from parent class.
    def test(self):
        print("test() method called")
    #def explore(self): # explore method override.
        #A.explore(self) # will call the explore method from class A.
        #B.explore(self) # will call the explore method from class B.
        #print("explore() method in class D, child class")    # custome code addition of class D. 
d_obj = D()
d_obj.explore() # if we do not override(define) the explore method in class D and call the explore method by using d_obj then by default class A explore method will be called because we have defined inheritance as D(A,B,C). If we define inheritance as D(B,A,C) then B class explore method will be called.  
d_obj.search()
d_obj.discover()
d_obj.test()

##########  Operator overloading
#Operator overloading: Python operators work for built-in classes. But same operator behaves differently with different types. For example, the + operator will, perform arithmetic addition on two numbers, merge two lists and concatenate two strings.

# This feature in Python, that allows same operator to have different meaning according to the context is called operator overloading.

#Example: 
#So what happens when we use them with objects of a user-defined class? Let us consider the following class, which tries to simulate a point in 2-D coordinate system.
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
p1 = Point(2,3)
p2 = Point(-1,2)
p1 + p2 # This will support error for now. unsupported operand type(s) for +: 'Point' and 'Point'
 
# The above code p1 + p2 can work by using operator overloading.  
#Overloading the + Operator in Python: To overload the + sign, we will need to implement __add__() function in the class. With great power comes great responsibility. We can do whatever we like, inside this function. But it is sensible to return a Point object of the coordinate sum.

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)
output: (1,5)
		
"""
Operator Overloading Special Functions in Python
================================================
Operator		Expression		Internally
==================================================
Addition			p1 + p2			p1.__add__(p2)
Subtraction			p1 - p2			p1.__sub__(p2)
Multiplication		p1 * p2			p1.__mul__(p2)
Power				p1 ** p2		p1.__pow__(p2)
Division			p1 / p2			p1.__truediv__(p2)
Floor Division		p1 // p2		p1.__floordiv__(p2)
Remainder (modulo)	p1 % p2			p1.__mod__(p2)
Bitwise Left Shift	p1 << p2		p1.__lshift__(p2)
Bitwise Right Shift	p1 >> p2		p1.__rshift__(p2)
Bitwise AND			p1 & p2			p1.__and__(p2)
Bitwise OR			p1 | p2			p1.__or__(p2)
Bitwise XOR			p1 ^ p2			p1.__xor__(p2)
Bitwise NOT			~p1				p1.__invert__()

Comparision Operator Overloading in Python
===================================================
Operator			Expression			Internally
===================================================
Less than					p1 < p2		p1.__lt__(p2)
Less than or equal to		p1 <= p2	p1.__le__(p2)
Equal to					p1 == p2	p1.__eq__(p2)
Not equal to				p1 != p2	p1.__ne__(p2)
Greater than				p1 > p2		p1.__gt__(p2)
Greater than or equal to	p1 >= p2	p1.__ge__(p2)
"""

#**************** Access modifier ******************************
#The access modifiers in Python are used to modify the default scope of variables. There are three types of access modifiers in Python: public, private, and protected.

#Variables/methods with the public access modifiers can be accessed anywhere inside or outside the class, the private variables can only be accessed inside the class, while protected variables can be accessed within the same package.

#Public: -All member variables and methods are public by default in Python.
# So when you want to make your member public, you just do nothing

class Cup:
    def __init__(self):
        self.color = None
        self.content = None

    def fill(self, beverage):
        self.content = beverage

    def empty(self):
        self.content = None

#We have there a class Cup. And here’s what we can do with it:

redCup = Cup()
redCup.color = "red"
redCup.content = "tea"
redCup.empty()
redCup.fill("coffee")

#Protected Dont touch unless you are subclass
class Cup:
    def __init__(self):
        self.color = None
        self._content = None # protected variable
    def fill(self, beverage):
        self._content = beverage
    def empty(self):
        self._content = None

#Private
class Cup:
    def __init__(self, color):
        self._color = color    # protected variable
        self.__content = None  # private variable
    def fill(self, beverage):
        self.__content = beverage
    def empty(self):
        self.__content = None
		
redCup = Cup("red")
redCup.__content = "tea"  #not accessible

######Summary of access modifier:
class Car:
    def __init__(self):
        print ("Engine started")
        self.name = "corolla"
        self.__make = "toyota" # private variable
        self._model = 1999 # protected variable
    def _protectedmethodexample(self):  # protected method
        print('I am protected method')        
    def __privatemethodexample(self):   # private method
        print('I am private method')
class Audi(Car):
    def _protectedmethodexample(self):  # protected method
        print('I am protected method inside class audi')        
    def __privatemethodexample(self):   # private method
        print('I am private method inside class audi')
car_a = Car()
print(car_a.name) # public variable can be accessed anywhere, within class, subclass and outside of class. 
print(car_a._model) # protected variable can be access within class, subclass and outside of class within same package. 
#print(car_a.__make) # private variable can not be accessed from outside of the class. 
car_a._protectedmethodexample()  #protected method can be access within class, subclass and outside of class within same package. 
#car_a.__privatemethodexample() ## private method can not be accessed from outside of the class.
acar_a=Audi()
print(acar_a.name) # Public variable can be access.
print(acar_a._model) # protected variabvle can be acccess.
print(acar_a.__make) # Private variable can not be accessed. this will throw an error.


##################### Abstract class
# A class which contains one or abstract methods is called an abstract class. An abstract method is a method that has declaration but not has any implementation.

# Abstract classes are not able to instantiated and it needs subclasses to provide implementations for those abstract methods which are defined in abstract classes. 

#While we are designing large functional units we use an abstract class. When we want to provide a common implemented functionality for all implementations of a component, we use an abstract class. Abstract classes allow partially to implement classes when it completely implements all methods in a class, then it is called interface.

## example 1:
from abc import ABC, abstractmethod  # This is needed to implement abstract class.
class Animal(ABC): #just use it as base class by passing implementing Animal class as child class of ABC (abstract class).
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
class Dog(Animal):
    def speak(self):
        return self.name+" says WOOF !"   
class Cat(Animal):
    def speak(self):
        return self.name+" says MEOW !"
fido=Dog("Fido")
isis=Cat("Isis")
print(fido.speak())
print(isis.speak())

## example 2:
from abc import ABC, abstractmethod   
class Polygon(ABC):   
    # abstract method 
    def noofsides(self): 
        pass  
class Triangle(Polygon):   
    # overriding abstract method 
    def noofsides(self): 
        print("I have 3 sides")   
class Pentagon(Polygon):   
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides")   
class Hexagon(Polygon):  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides")   
class Quadrilateral(Polygon):   
    # overriding abstract method 
    def noofsides(self): 
        print("I have 4 sides")   
# Driver code 
R = Triangle() 
R.noofsides()   
K = Quadrilateral() 
K.noofsides()   
R = Pentagon() 
R.noofsides()   
K = Hexagon() 
K.noofsides()
  
  
####################### Special method:

mylist=[1,2,3]
print(len(mylist))
class Sample():
    pass
mysample=Sample()
print(mysample)  #address
print(mylist)    #print data
#I want how can use len and print functions on my objects
#MAGIC METHODS
class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    #Below function we overridden . to print our object
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book has been deleted ")

b1=Book('Python Rocks','Jose',200)
print(b1) #prints address -- 
print(b1)
#NEXT is len
print(len(b1))
#NEXT is del
del(b1)
#print(b1) #get error b1 not defined It will delete obj from memory
#some times we may want other things to occur when we delete var

