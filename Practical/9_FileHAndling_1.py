'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
'''

'''
mbox-short.txt file
'''


fname=r"C:\Users\swati.avinash.nikam\Desktop\PythonLateralTrainingMaterial\FileForFileHandlingDemo\mbox-short.txt"

fh=open(fname)

#Try to print fh to chk file exist or not
#print(fh)
count=0
for line in fh:
    if line.rstrip().startswith('From'):
        if line[4] is ':':
            pass
        else:
            count=count+1
            li=[]
            li=line.rstrip().split()
            print(li[1])

print(count)
fh.close()


