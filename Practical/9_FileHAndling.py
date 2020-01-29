fname=r"C:\Users\swati.avinash.nikam\Desktop\PythonLateralTrainingMaterial\FileForFileHandlingDemo\romeo.txt"
fh=open(fname)
lst=list()
'''
for eachline in fh:
    listofwords=[]
    print(eachline.rstrip())
    listofwords.append(eachline.rstrip())
    for word in listofwords:
        if word not in lst:
            lst.append(listofwords)


print("--------------------------->")
for w in lst:
    print(w)
'''



''' Question
8.4 Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the
split() method.
The program should build a list of words.
For each word on each line check to see if the word is already in
the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''


'''romeo.txt file'''









fname = input("Enter file name: ")
fh = open(fname)

alllines=[]
for eachline in fh:
    print(eachline.rstrip().rstrip())
    alllines.append(eachline.rstrip().rstrip().split())
    

    
print(len(alllines))
lst=[]
for line in alllines:
    for word in line:
        if word not in lst:
            lst.append(word)


lst.sort()
print(lst)
fh.close()

