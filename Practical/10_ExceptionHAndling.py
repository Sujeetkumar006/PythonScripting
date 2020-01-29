
#Exception Handling

#Errors are bound to happen in your code! .Espcially when someone else ends up using it in unexpectected way
#we can use use error handling to attempt to plan for possible errors

#Example file opened in r mode trying to attemp write to file
#Keywords:- try except finally

def add(n1,n2):
    print(n1+n2)

add(10,20)


num1=10
#num2=input("please provide a number")
#add(num1,num2) #TypeError

try:
    #WANT TO ATTEMPT THIS CODE
    #MAY HAVE AN ERROR
    result=10+10
except:
    print("hey it looks like you aren't adding correctly!")
else: #else block gets executed when no exception is raised
    print("Add went well")
    print(result)
    

print("************* Handling multiple exceptions ****************************")

try:
    f=open('testfile','w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print('Hey you have an OS Error')
except: #we can write only except , but it is not a good prog practice
    print("All other exceptions")
finally:
    print("I always run")



#Example 1
'''
finally The finally clause is commonly used to define clean up actions 
which must be performed under any circumstance. 
If try-except statement has an else clause then finally clause must appear after it.
'''



def ask_for_int():
    while True:
        try:
            result=int(input("Please provide a number"))
        except:
            print("Whoops ! that is not  number")
            continue
        else:
            print("yes thank you")
            break
        finally:
            #print("End of try/except/finally")
            #print("I will always run at the end")
            print("I am going to ask you again")

ask_for_int()

#*******************  Except clause with multiple exception ********************

try:
    f=open('testfile','w')
    f.write("Write a test line")
except (TypeError,OSError):
    pass
finally:
    print("I always run")

    

#****************  How to raise exception *******************************
#An exception is simply an object raised by a function signaling that something
# unexpected has happened which the function itself can't handle

#few common exception in python ZeroDivisionError,Exception (common base class for all not exit exception)
# IndexError when sequnce out of range
#IOError when IO op failed


try:
    num1=int(input("Enter number1"))
    num2=int(input("Enter number2"))
    if num2==0:
        raise ZeroDivisionError("demo is 0")
    else:
        result=num1/num2
except ZeroDivisionError:
	print("error ocurred")
except ValueError:
        print("please enter valid number")
else:
	print("div went well")
	
	
	


#********************* How to create own exception ****************************

class InvalidAgeException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message




def validateAge(age):
    if age < 18:
        raise InvalidAgeException("Need to wait")
    
try:
    age=int(input("Enter age"))
    validateAge(age)
except InvalidAgeException as e:
    print("Error:", e)
else:
    print("Done with voting.....")


