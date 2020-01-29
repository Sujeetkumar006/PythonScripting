################### Topics #######################

## Difference between interprator and compilar
## What is Pip and conda
python -m pip install <the package name>
python -m pip install numpy
## Different Executable: COmmand prompt, IDE(Eclipse + PyDev, PyCharm, Spyder), Notebook (Jupyter), Editor(Atom, Sublime Text), Distribbution (Anconda, Canopy).
## Python 3.x is the current version and is under active development. Python 2.x is the legacy version and will receive only security updates until 2020.


"""Conda and pip are often considered as being nearly identical. Although some of the functionality of these two tools overlap, they were designed and should be used for different purposes. Pip is the Python Packaging Authority’s recommended tool for installing packages from the Python Package Index, PyPI. Pip installs Python software packaged as wheels or source distributions. The latter may require that the system have compatible compilers, and possibly libraries, installed before invoking pip to succeed.

Conda is a cross platform package and environment manager that installs and manages conda packages from the Anaconda repository as well as from the Anaconda Cloud. Conda packages are binaries. There is never a need to have compilers available to install them. Additionally conda packages are not limited to Python software. They may also contain C or C++ libraries, R packages or any other software.

This highlights a key difference between conda and pip. Pip installs Python packages whereas conda installs packages which may contain software written in any language. For example, before using pip, a Python interpreter must be installed via a system package manager or by downloading and running an installer. Conda on the other hand can install Python packages as well as the Python interpreter directly.

Another key difference between the two tools is that conda has the ability to create isolated environments that can contain different versions of Python and/or the packages installed in them. This can be extremely useful when working with data science tools as different tools may contain conflicting requirements which could prevent them all being installed into a single environment. Pip has no built in support for environments but rather depends on other tools like virtualenv or venv to create isolated environments. Tools such as pipenv, poetry, and hatch wrap pip and virtualenv to provide a unified method for working with these environments.

Pip and conda also differ in how dependency relationships within an environment are fulfilled. When installing packages, pip installs dependencies in a recursive, serial loop. No effort is made to ensure that the dependencies of all packages are fulfilled simultaneously. This can lead to environments that are broken in subtle ways, if packages installed earlier in the order have incompatible dependency versions relative to packages installed later in the order. In contrast, conda uses a satisfiability (SAT) solver to verify that all requirements of all packages installed in an environment are met. This check can take extra time but helps prevent the creation of broken environments. As long as package metadata about dependencies is correct, conda will predictably produce working environments.

Given the similarities between conda and pip, it is not surprising that some try to combine these tools to create data science environments. A major reason for combining pip with conda is when one or more packages are only available to install via pip. Over 1,500 packages are available in the Anaconda repository, including the most popular data science, machine learning, and AI frameworks. These, along with thousands of additional packages available on Anaconda cloud from channeling including conda-forge and bioconda, can be installed using conda. Despite this large collection of packages, it is still small compared to the over 150,000 packages available on PyPI. Occasionally a package is needed which is not available as a conda package but is available on PyPI and can be installed with pip. In these cases, it makes sense to try to use both conda and pip"""

#################### Topics #########################


################ Python Version ##################

$ python --version
# Need to add path of python to the environment variable before using it in command prompt
# System Variables: "C:\ProgramData\Anaconda3"

################ Python Execution #####################
# cmd execution
$ python
C:\Users\hp>python
>>> 1+5
6
>>> print('Hello World')
Hello World
>>> exit()

# Python file execution
C:\Users\hp>cd Desktop
C:\Users\hp\Desktop>python test1.py

# Python file execution in interactive mode
python -i test1.py

# Out of Pythonn prompt
>>> quit()
OR
>>> exit()


################### Comments #######################
    
# This is single line comment
''' This is multiline comment '''
""" This is also Multiple line comment """

############# Keywords in Python #################

import keyword
print(keyword.kwlist)
# Keyword can not be used as Variable name, No complilation error but program will behave weired.


############### Print in python ########################

#do calculation in print

print(2+2)

#Print more than one expression

print("Age : ", 22)

name="Sweety"
salutation="Miss"
greeting="Hello"

print(greeting,salutation,name)
print(greeting,',',salutation,name) 
print(greeting+',',salutation,name)

# ' "  ''' . escape character (\)
quote1="Don't cry becoz it's over, smile beacuse it happened "
print(quote)
quote2='Ram said : "Hello Everyone !" '
print(quote2)
quote3= 'Mr.Seuss said "Don\'t cry becoz it\'s over, smile beacuse it happened "'
print(quote3)

#escape character (\): next character from \ will be ignored.

# raw string using r

path="C:\\Sujeet\\New folder"
print("Path is ---->",path)
path="C:\Sujeet\New folder"
print("Path is ---->",path)
path=r"C:\Sujeet\New folder"
print("Path is ---->",path)
path=r"C:\\Sujeet\\New folder"
print("Path is ---->",path)

#for file extention
path2="Test.java"
path1=path2.split('.')   #output:- ['Test', 'java']
print(path1)

print(type(path1)) 

#if we know if how many token are there
a,b=path2.split('.')
print(a)
print(b)

#Multiple lines on same line
print("Mesaage1");print("Mesaage2")


################### Code Indention #######################
#The number of spaces in the indentation is variable
#but all statements within the block must be indented the same amount
#Example
if True:
    print("True")
else:
    print("false")





