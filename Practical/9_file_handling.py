#File Handling in Python
'''
python support many file format
1.normal text file
2.csv file
3.excel file
4.json file
'''


#Read and write data to Text file

#------------ How to write to text file -------------------------

#Try to compilewithout using r It will show runtime error. As it founds \ as
#a escape seq char. so to ignore all escape seq char we tell python
#please consider this as a raw string
#now add r at start

file1=r"F:\Study\StudyDocs_GoogleDrive\Training\Classes\worksapce\Test1.txt"

#now get file pointer / file handle
#do mention w if file is not there it will create it.
#fh=open(file1,"a")
#try to print fh and check

'''
print(fh)

fh.write("Python")
fh.write("Is a programming lang")
'''

#once done close file
#fh.close()

#Now observe the output in file . we will be not able to see new line over there
#as we are writing data programatically
#so if we want to write new line then write it explicitly
#put fh.close () after these lines

'''
fh.write("It supports many file format like")
fh.write("\n Text")  
fh.write("\nExcel")
fh.write("\nJson")
fh.close()
'''


#now as we are observing we are overwrting data
#but i want to append data so lets change mode of file to a
#and now observe the data on file. You will be to see file pointer will strat wrting
#from immediate next char . 



#------ How to read from text file ---------------------------------
#its super simple

'''
fh=open(file1)
print(fh.read())
for data in fh:
    print(data)
'''


#Note:- Now while reading file we do not have to put \n char here

#now lets see \n in data

    
'''    
allLines=[]
fh.seek(0) #Need to seek file pointer at initial
for data in fh:
    allLines.append(data)
fh.close()
print(allLines)
'''


#observer output over here you will be able to see \n char
#we need to delete them using strip() func It will remove last line char.
# strip() can be used to remove any another char too from data
#For Example add 0's at end of each and every line and strip it

print("------------------------")


'''
fh=open(file1)
l1=[]
for data in fh:
    l1.append(data.strip())
    print(data)

print(l1)
fh.close()
'''



#----------- Excercise count total number of lines ----------------------

'''
fh=open(file1)

count=0
for i in fh:
    count=count+1

print("total no of lines",count)
fh.close()
'''



#once you have number of lines we can perfomr any kind of read opeartion read last line read first line read in between


#-------- Exercise to read all line at once --------------------------------
#--- then read last two line ------------


'''
fh=open(file1)
lines=fh.readlines()  #if lines==None menas it has not data Safer side prog
print(lines)
print(len(lines))
print(lines[len(lines)-2  : ])

fh.close()
'''




#--------- Exercise Read data from one file and write to another file

'''
step1. open file1 and file2 in open mode
step2 read data from one file and write to anotehr
step3 and then close them

'''


#------------ Another way to read file ---------------------------------------------

#by using with. here 

with open(file1) as fhandle:
    for line in fhandle:
        print(line.strip())



#-------- BrainStorming Exercise Time  Read data from config file and print it

#STep1 create one file named ConfigurationFile.cfg.txt
#Step2 write data to that
'''

'''


d={}
file2=r"C:\Users\swati.avinash.nikam\Desktop\PythonLateralTrainingMaterial\FileForFileHandlingDemo\ConfigurationFile.cfg.txt"
#print(file2)

with open(file2) as fh1:
    for i in fh1:
        key,value=i.strip().split('=')
        d[key]=value


#test code try to access any key and value
print(d["path"]+d["file"])

#above code is giving me exact path to open file
#so we can make use of it in for loop on th fly

with open(d["path"]+d["file"]) as fh2:
    for i in fh2:
        print(i.strip())


#HAPPY . we are optimizing code


#------------Read and Write to csv file-----------------------


print("sep------------------------")

#Write to csv file


file3=r"C:\Users\swati.avinash.nikam\Desktop\PythonLateralTrainingMaterial\FileForFileHandlingDemo\WriteToFile.csv"
wdata=open(file3,"w")
print(wdata)


wdata.write("pid,prodname,price")
wdata.write("\n101,pen,25")
wdata.write("\n102,pencil,12")
wdata.write("\n103,sharpner,5")
wdata.write("\n104,eraser,3")

wdata.close()



#Read fron csv file
rdata=open(file3,"r")
print(rdata.read())

rdata.seek(0)
print(rdata.readlines())

for i in rdata:
    print(rdata.readlines())

rdata.close()






#------ diff between read() readline() readlines() -------------------
print("^^^^^^^^^^^^^^^^^^^^^^^^")
'''
fp=open(file1,"r")
str1=fp.read()     #return all lines
print(str1)
fp.close()

fp=open(file1,"r")
print(fp.readline()) #return one line at a point of time
print(fp.readline())
print(fp.readline())
print(fp.readline())
fp.close()

fp=open(file1,"r")
print(fp.readlines())  #returns list once we have list we can perfomr any action
fp.close()
'''


#-------  Read and write to JSON (Javascript Object Notation )file ------------------------
'''In computing, JavaScript Object Notation or JSON is an open-standard file format that uses human-readable text
to transmit data objects consisting of attribute–value pairs and array data types'''

import json

'''
myjson={"101":"Max","102":"Paul","103":"Sam"}
data=json.dumps(myjson)
print(data)
print(type(data))
list1=data.split()
print(list1)
'''
#writing to file
myjson={"101":"Max","102":"Paul","103":"Sam"}
jsonfile=r"C:\Users\swati.avinash.nikam\Desktop\PythonLateralTrainingMaterial\FileForFileHandlingDemo\FirstJson.txt"
with open(jsonfile,"w") as jw:
    json.dump(myjson,jw)

    
#read from file

with open(jsonfile,"r") as jr:
    d=json.load(jr)

print(type(d))
print(d)


#Read contents from file. create Test1.txt file and read it.


f=open('Test1.txt')

for lines in open('Test1.txt'):
    print(lines)
	
#But here we can identify few gaps betwween two lines that can be removed by 

for lines in open('Test1.txt'):
    print(lines.strip())
	
#strip can also be used to eliminate last values like . here
for lines in open('Test1.txt'):
    print(lines.strip().strip('.'))

#what if we have path 
file1=r"C:\Users\swati.avinash.nikam\Desktop\PythonLateralTrainingMaterial\Test1.txt"
fd=open(file1)
print(fd) 
for i in fd:
	print(i)
	

	
#Need to read last three lines

#Step 1: seek pointer to 0th position and read lines and line number 
fd.seek(0)

k=0
for k,i in enumerate(fd):
    print(k,i.strip())
	
#Step2 : Now we can calculate total no of lines by saying k+1	

print(k+1)

#stpe 3 fetch in list and print last three items

allLines=fd.readlines()


print(allLines)  # now we have data with us ekbaar list me aa gaya now we do anything
				 #it may 100 lines but we need only last 3 line so extract them first
			
list1=allLines[len(allLines)-3:]	#will give last line too
print(list1)
list1=allLines[len(allLines)-3:]	#so taking from 4
print(list1)

#step 4 Now we need to remove \n but we shld not modify data

data=[]

for i in list1:
	data.append(i.strip())
	
	

#******************* Assignment over here *****************************

	
	
#Now write data to file
	
fd=open(r"C:\Users\swati.avinash.nikam\Desktop\PythonLateralTrainingMaterial\Test2.txt","w")
print(fd)

fd.write("First line\n")
fd.write("second line ")
fd.close()


fd=open(r"C:\Users\swati.avinash.nikam\Desktop\PythonLateralTrainingMaterial\Test2.txt","r")
for i in fd:
	print(i)
fd.close()	


#shortcut with

with open(r"C:\Users\swati.avinash.nikam\Desktop\PythonLateralTrainingMaterial\Test2.txt","r") as file1:
for i in file1:
	print(i)

with open(r"C:\Users\swati.avinash.nikam\Desktop\PythonLateralTrainingMaterial\Test2.txt","r") as file1:
	print(file1.read())

	
## Exercise Read alternate line from two file
## Exercise #read file which have 10 line read them and write in one line in another file


#Real life scenario how to use config file.
'''
Below are the contents in config file.
1. We need to read data from this file . use dict


username=Swati
password=Swati*123
path=C:\Users\swati.avinash.nikam\.spyder-py3
sid=11158542
'''

	

##################### Read and write to csv file ########################
#step1 first create one csv file with col ID,Name,Age,Loc
#Step2 Then read data

#Read csv file
rdata=open("FirstFile.csv","r")
print(rdata.read())
r1.close()

#by using with bhi chalega lekin we will loose access to the pointer
'''
with open(r"C:\Users\swati.avinash.nikam\Desktop\Track1\Python Training\JunaidSirClassDemo\FirstFile.csv","r") as r1:
    print(r1.read())
'''
rdata.seek(0)
print(rdata.readlines()) #beautiful function it will return us list. and once we have list we can do anything to this



#Write to csv file

wdata=open(r"C:\Users\swati.avinash.nikam\Desktop\Track1\Python Training\JunaidSirClassDemo\FirstFile.csv","a")
wdata.write("Id,Name,Age,loc")
wdata.write("\n111,aaa,11,PDC")
wdata.write("\n111,aaa,11,PDC")
wdata.close()


wdata=open("WriteToFile.csv","w")  # w karoge to over write ho jayega go for a mode 
wdata.write("pid,prodname")
wdata.write("\n111,aaa")
wdata.write("\n222,bbb")
wdata.close()







	
	
	
	


##########################################################
#How to read and write excel file	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
