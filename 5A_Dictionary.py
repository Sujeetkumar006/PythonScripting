#import copy
#Dictionary in Python -->
#1.Python dictionary is an unordered collection of item.
#2.While other compund data types have only value as an elemnet a dictionary has a key value pair
#3. Dict are optimized to retrieve values when the key is known


#How to create dict
#Creating a dictionary is as simple as placing items inside curly braces{} separated by comma
#An item has a key value pair
#Values can be of any data type and can repeat, keys must be of immutable type (string,number or tuple)must be unique


#NOTE:- List is a linear collection of values that stay in order
#NOTE:- DIct is a bag of values each with its own label


#Nice example of courseera
purse=dict()
purse['money']=12
purse['candy']=3
purse['tissue']=75

print(purse)

print(purse['candy'])

#add more candys to purse

purse['candy']=purse['candy']+2

print(purse)

#IMP Note:- dict contents are mutable


#Empty dictionary
my_dict={}
tuple1=(1,2,3)
list1=[1,2,3]
print(type(list1))
print(type(tuple1))
print(type(my_dict))


#dict with integer keys
my_dict={1:'LKM',2:'IRC'}

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)


#How to grab a particular value like print(phonebook["Swati"]). it will show error
#so better approcach is  if "Swati" in phonebook







phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))



#Preparation for next assignmnt i.e. to find out occ of each and every elemnets
#for this i need to create a ppt which is having keywords . with animation
#Key observatioin. as a human being we are doing hypothesis and give a count. but comp doesnt like that
#if data is more in that case what we can do is we can mark lines and keep track

	
	
#### @@@@@@@  IMP assignment for dict # IMP assignment for dictionary
#give count of occ of each elemnet in list
#Similar assignment of courseera in Demo11-1.py file
    
list1=[1,2,3,1,2,"swati","Anagha","Swati"]    

#print("-------------------Logic 1----------------")
#
#count=0
#
#for i in list1:
#    count=0
#    for j in list1:
#       # print(i,j)
#        if i==j :
#            count=count+1
#    print(i,"occured " ,count, " times ")     
#      
#print("-------------------  ***     ----------------")



print("-------------------Logic 2----------------")
dict1={}
for i in list1:
    if i in dict1:
       dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
print(dict1)
        

for key,val in dict1.items():
    print(key , " occured " ,val , "times ")

print("-------------------  ***     ----------------")


print("-------------------Logic 3----------------")
count=dict()
names=['java','c++','python','java','Java','Python','python']

for name in names:
    count[name]=count.get(name,0)+1
print(count)

print("-------------------  ***     --------------
#dict with mixed keys
my_dict={'name':'Swati',1:[1,2,3]}

#using dict()
my_dict=dict({1:'LKM',2:'IRC'})

#from sequence having each item as a pair
my_dict=dict([(1,'LKM'),(2,'IRC')])


#How to access elements from dictionary
#dict uses key to access values
#keys can be used either inside square brackets or with the get() method
#The diff is get() is return None instead of keyerror message if the key is not found.


my_dict={'name':'Swati','project':'LKM'}
print(my_dict['name'])

print(my_dict.get('project'))

#Try to access keys which does not exist
print(my_dict.get('address'))
#print(my_dict['address'])


#nested dict
d={'k1':{'nestkey': {'subnestkey' :'value'} }  }

print(d)
print(d['k1']['nestkey']['subnestkey'])
print(d['k1']['nestkey']['subnestkey'].upper())

#builtin methods
d={'k1':1 ,'k2':2 ,'k3':3}
print(d.keys()) #return list of keys
print(d.values()) #return list of values
print(d.items()) #return key and values


#How to change or add elements in a dictonary
#dict is mutable. We can add new item or change the value of existing items using assignment operator
#If key is already present value gets updated else a new value pair is added to the dict


my_dict={'name':'Swati','project':'LKM'}

#update value
my_dict['project']="Merk"

print(my_dict)

#add item
my_dict['address']='pune'

print(my_dict)




dicto = {'Bookname' : 'Python', 'Price' : 210}

#Adding new entries
dicto ['Author'] = 'TutorialsCloud' ;
dicto ['Discount']= '10 Percent';

#Updating an Entry
dicto ['Price']  = 200;


#Delete or remove elements from a dictionary
#using method pop() removes item and return the value
#popitem() can be used to remove and return an arbitrary item(key,value) form the dictionary.
#clear() can be used to remove all items at once
#del() method can be used to delete individual or entire dict itself.


projects={101:'LKM',102:'IRC',103:'MERK',104:'Vodafone',105:'Barclays'}

#remove a particular item
print(projects.pop(102))

#remove an arbitrary item (it shld delete any item but its deletig last item
print(projects.popitem())


#delete particular item using del()
del projects[104]

print(projects)

#delete the dict itself

#del projects


projects.clear()

print(projects)   #it will delete only items


#copy() method  --> This method returns a shallow copy of dict
#it doesn't modify the original dict


print("Trying copy...............................................")

original={1:'One',2:'Two'}

new=original.copy()

print("Below two are same..................")
print('original dict is --->',original)

print('New dict --->',new)



new[4]='New Number'

print("After adding.... new element ........")
original.clear()
print('original dict will get modified  --->',original)
print('New dict dict will get modified--->',new)


#In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.
#In python, this is implemented using “deepcopy()” function.


o1={1:'Roman 1',2:'Roman 2'}
n1=copy.deepcopy(o1)

print("Below two are same..................")
print(o1)
print(n1)

n1[3]='Roman 3'
print("After adding.... original will not get modified ")
print(o1)
print("After adding.... onew will  get modified ")
print(n1)



#NOTE:-
#When copy() method is used, a new dictionary is created which is filled with a copy of the references from the original dictionary.
#When = operator is used, a new reference to the original dictionary is created.



#copy by = operator

originalDict={1:'ONE',2:'TWO'}
newDict=originalDict;

print(originalDict)
print(newDict)

originalDict.clear()

print("After clearing original dict will impact on new will also get cleared")
print("but this will not happen with copy method")
print(originalDict)
print(newDict)





print("*********************************************************************************")


#How to sum up all dictionary items
dict1={'data1':100,'data2':200,'data3':300}

print(sum(dict1.values()))

      


#@@@@@@@@@@@@@@@@@@@@ Udemy @@@@@@@@@@@@@@@@@@@@@@@@@@@@

#nested dict
d={'k1':{'nestkey': {'subnestkey' :'value'} }  }

print(d)
print(d['k1']['nestkey']['subnestkey'])
print(d['k1']['nestkey']['subnestkey'].upper())

#builtin methods
d={'k1':1 ,'k2':2 ,'k3':3}
print(d.keys()) #return list of keys
print(d.values()) #return list of values
print(d.items()) #return key and values




#Dictionary from data camp web site

#https://www.datacamp.com/community/tutorials/python-dictionary-tutorial

#Agenda
#1. how to create a dictionary
#2. load data
#3. filter
#4. get data
#5. sort values
#6. other dict op


#Dict is special data structure which Python provides natively .
#How we search for python like p then y then t and onwords and we get diff ans
#This is how dict helps us to find any word within minute

#python keep track of where to find a specific piece of info


#1. How to create a python dict
#Suppose we need to make an inventory of the fruit .
#DIct are the curly brackets {} and for each item in dict, the separation of the key and value by a colon :



fruit = {"apple" : 5, "pear" : 3, "banana" : 4, "pineapple" : 1, "cherry" : 20}

# Access the `fruit` dictionary directly (without using get) and print the value of "banana"
print(fruit["banana"])

# Pick one of 5 the fruits and show that both retrieval styles obtain equal results
print(fruit["cherry"] == fruit.get("cherry"))


#2. Loadind data in python dict --> nested dict  --> This way table and matrices can easily be stored in a dictionary













































