# Pandas: Panel Data
#There are two types of data structures in pandas: Series and DataFrames.

#Series: a pandas Series is a one dimensional data structure (“a one dimensional ndarray”) that can store values — and for every value it holds a unique index, too.
#Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). The axis labels are collectively called index. Pandas Series is nothing but a column in an excel sheet.

import pandas as pd
import numpy as np
list = ['g', 'e', 'e', 'k', 's']
data = np.array(['g','e','e','k','s'])
ser = pd.Series(data)
# create series form a list
ser1 = pd.Series(list)
print(ser,ser1)

# Selecting particular value in series
print(ser[:5])


# accessing a element using index element
# creating simple array
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22]) 
print(ser[16])
###################

# Series from Data frame:
import pandas as pd
df = pd.read_csv("C://Users//hp//Desktop//Notebook_Files//nba.csv")  
ser = pd.Series(df['Name']) 
data = ser.head(10)
data

# Data Series:

Note: Sometimes (especially in predictive analytics projects), you want to get Series objects instead of DataFrames. You can get a Series using any of these two syntaxes (and selecting only one column):

article_read.user_id
article_read['user_id']

#Now we access the element of series using .loc[] function.
data.loc[3:6]

# Binary operation: Add and subtract.

data = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
data1 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'e']) 
print(data, "\n\n", data1)
data.add(data1, fill_value=0)
#####################################################

#DataFrame: a pandas DataFrame is a two (or more) dimensional data structure – basically a table with rows and columns. The columns have names and the rows have indexes.

# reading the basic files:

import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame=pd.read_csv('Iris_data_sample.csv') # special character will be populated as it is, The balnk will be populated as NaN.
data_frame

df=pd.read_csv('zoo.csv', delimiter = ',')

# TO get the data without default indexes(Without data series):
data_frame=pd.read_csv('Iris_data_sample.csv',index_col=0)

# TO Make the second column as index column:
data_frame=pd.read_csv('Iris_data_sample.csv',index_col=1)

# TO Make the third column as index column:
data_frame=pd.read_csv('Iris_data_sample.csv',index_col=2)

# TO convert Junk values/Special char with NaN.
data_frame=pd.read_csv('Iris_data_sample.csv',index_col=0,na_values=['###','??']) # This will not change the value in origign or Excel file rather only it will be loaded as so. 

#To put the header on the excel sheet:
df=pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

# Print the whole dataframe
#The most basic method is to print your whole data frame to your screen. Of course, you don’t have to run the pd.read_csv() function again and again and again. Just store its output the first time you run it!

article_read = pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

#After that, you can call this article_read value anytime to print your DataFrame!
article_read

# Reading the excel file:
import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame=pd.read_excel('Iris_data_sample.xlsx',sheet_name='Iris_data')
data_frame

# Reading the text file:
import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame=pd.read_table('Iris_data_sample.txt')
data_frame

 # Default delimeter is tab or /t here so we will get the 1 coulmn above, to get the multiple column we need to provide either sep or delimiter paramenter.
 data_frame=pd.read_table('Iris_data_sample.txt',sep=' ') # default delimiter of text file is '\t'
 #data_frame=pd.read_table('Iris_data_sample.txt',delimiter=' ')
data_frame
 
 
# TExt file can be read using read_csv as well as read_table may be depreciated soon:
data_frame=pd.read_csv('Iris_data_sample.txt',delimiter=' ')
data_frame 
  
# TO get DataFrame indexs:
data_frame.index

# TO get DataFrame columns:
data_frame.columns

# TO get DataFrame Size:
data_frame.size # row*columns

# TO get DataFrame shape:
data_frame.shape # row,columns

# TO get memory uses of each columns in bytes:
data_frame.memory_usage()

# TO check the number of dimension:
data_frame.ndim # one dimension is row and one is column, as we have multiple columns or row but still the dimension is 2 only.  



### Indexing or selecting the data: Row Filter.

# Simplest Syntax:
data_frame[0:20] # For row selection based on row index 
data_frame.SepalLengthCm # Column Selection
data_frame['SepalLengthCm']  # Column Selection, Different syntax
data_frame[['SepalLengthCm','SepalWidthCm']] # For Multiple column selection based on column name.


#Selecting both rows and columns:
data_frame[5:10][['SepalLengthCm','SepalWidthCm']]
data_frame[['SepalLengthCm','SepalWidthCm']][5:10]
# both of the above syntax will work , but 1st will be more efficient as it will apply the filter or rows first.

# seleting data  
article_read.head() # by default it will return 5 values.
article_read.head(10)
article_read.tail()
#Or a few random lines by typing:
article_read.sample(5)

# Scalar Value: TO get selective columns value at selective row:
# "at" and "iat" is used  
# "at" provides label based scaler lookup: row value should be integer index, column should be name
data_frame.at[4,'SepalLengthCm'] # TO get the value if column SepalLengthCm at row index 4. 
# "iat" provides label based scaler lookup: row value should be integer index, Intead of column name we need to use column index.
data_frame.iat[4,2] 
 
# TO get group of rows and column we use "loc" and "iloc" instead of "at"

#loc is label-based, which means that we have to specify the name of the rows and columns that we need to filter out.
#Syntax: data_frame.loc[A,B] # A: Row values (Index or slice), B: Column (one or many)
data_frame.loc[:,['SepalLengthCm','SepalWidthCm']] # All rows , 2 columns
data_frame.loc[5:10,'SepalLengthCm'] # 5 rows, one columns
data_frame.loc[5:10] # 5 rows, all columns
#On the other hand, iloc is integer index-based. So here, we have to specify rows and columns by their integer index.
data_frame.iloc[5:10,2] # Here instead of column name we have used column index .



# Some examples: 
# crete a sample dataframe
data = pd.DataFrame({
    'age' :     [ 10, 22, 13, 21, 12, 11, 17],
    'section' : [ 'A', 'B', 'C', 'B', 'B', 'A', 'A'],
    'city' :    [ 'Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'gender' :  [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'favourite_color' : [ 'red', np.NAN, 'yellow', np.NAN, 'black', 'green', 'red']
})
# select all rows with a condition
data.loc[data.age >= 15]
# select with multiple conditions
data.loc[(data.age >= 12) & (data.gender == 'M')]
#slice
data.loc[1:3]
# select few columns with a condition
data.loc[(data.age >= 12), ['city', 'gender']]


# update a column with condition
data.loc[(data.age >= 12), ['section']] = 'M'
data
# update multiple columns with condition
data.loc[(data.age >= 20), ['section', 'city']] = ['S','Pune']
data
# select rows with indexes
data.iloc[[0,2]]
#select rows with particular indexes and particular columns
data.iloc[[0,2],[1,3]]
# select a range of rows
data.iloc[1:3]
# select a range of rows and columns
data.iloc[1:3,2:4]
# filter: 
data[data.city == 'Gurgaon']
data[data.section == 'A']


import pandas as pd
df = pd.read_csv('F:/Study/StudyDocs_GoogleDrive/Prwatech/Classes/testdata/test1.csv', error_bad_lines=False)

import pandas as pd
df = pd.read_csv('test.csv', error_bad_lines=False)
df[0:3]


print(df['Marks'].max())
print(df['Marks'].mean())
print(df['Marks'].min())

df.describe() # will only include int and float coloumns

df[df.Marks>89]
df[]


####### COpy of Pandas data to other variable ###############
#Shallow Copy: When the reference of variable a and b is same , means they are pointing to same variable.
#Deep Copy: When both a and b have separate copy of variable, so change in a will not reflect in b and vice versa.

import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
#data_frame=pd.read_table('Iris_data_sample.txt',sep=' ')
data_frame=pd.read_csv('Iris_data_sample.txt',delimiter=' ')
data_frame_new=data_frame # This is shallow copy syntax 1.
data_frame_new_1=data_frame.copy(deep=False) # This is shallow copy syntax 2, default deep copy is true.
data_frame_new_2=data_frame.copy(deep=True) # This is Deep copy syntax 1.
data_frame_new_3=data_frame.copy() # This is Deep copy syntax 2, by default deep=True
print(id(data_frame))
print(id(data_frame_new))


# Data Types in Pandas:Data type is different in Python and Pandas.
#Number:
integer: int (python), int64(Pandas) # 64 stands for 64 bits which is 8 bytes.
float: float(python), float64(Pandas)
# Character Type(String): Two types in pandas: CAtegory and Object.
# Category:  A string variable consisting of only a few different values. Converting such a string variable to a categorical variable will save some memory. A categorical variable takes on a limited, fixed number of possible values .
# object : The column will be assigned as object data type when it has mixed types (numbers and strings). If a column contains ‘nan’(blank cells), pandas will default to object datatype. For strings, the length is not fixed

data_frame.dtypes # this will give the data types for each column.
data_frame.get_dtype_counts() # To get each data type counts.

#Selecting data based on data types
import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
#data_frame=pd.read_table('Iris_data_sample.txt',sep=' ')
data_frame=pd.read_csv('cars_sampled.csv')
data_frame.dtypes # object,int64
# for selective column selection on based of data type
# Syntax: #DataFrame.select_dtypes(include=None, exclude=None) # we can pass what to include and what to exclude, both parameter are optional.
data_frame.select_dtypes(include=[object])


#Concise summary of dataframe:info() 
#returns a concise summary of a dataframe 
# data type of index 
# data type of columns
# count of non-null values 
# memory usage 
data_frame.info()


# Unique elements of columns 
# Syntax: np.unique(dataFrame[ColumnName])
np.unique(data_frame['seller'])
np.unique(data_frame['name'])


#### ####  importing and Cleaning of Data: ######################
# We need to know how missing values are represented in the dataset in order to make reasonable decisions 
# The missing values exist in the form of ‘nan’, "##", "??" or in any special character ◦ Python,by default replace blank values with‘nan’
# Now, importing the data considering other forms of missing values in a datafram


# Replacing characters with NaN values. By dafualt all the blank values is considered as NaN(null), We can replace all the special character in coulmn with NaN as below.

import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame=pd.read_csv('Toyota.csv', index_col=0) 
data_frame.info() # Here we have maximum non-null values as many contians the special character but will not consider as NaN or Null.
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"]) # We are replacing special character "??"m available in coulmn with NaN(Null) values.
data_frame1.info() # here We will less non null values as all the special character passed as na_values will be replaced by NaN(Null)

#Converting variable’s data types

#astype() method is used to explicitly convert data types from one to another 
#Syntax: DataFrame.astype(dtype)
data_frame1['MetColor']= data_frame1['MetColor'].astype('object')
data_frame1.info()

# Changing data type may help in saving the space and memory.
# We can change the object data type to Category to save the memory for string type of variable.
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"]) # We are replacing special character "??" available in coulmn with NaN values.
print(data_frame1['FuelType'].nbytes) # nbytes check the space utilize by that columns.
data_frame1['FuelType']= data_frame1['FuelType'].astype('category')
print(data_frame1['FuelType'].nbytes)

### Code to get the special charaters from row:
abc=list(set(data_frame['KM']))
abc1=list(set(data_frame['Doors']))
def special_char(abc):
 list1=[]
 def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
    return True
 for i in abc:
   if is_int(i):
    pass
   else:
    list1.append(i)
 return list1
res=special_char(abc)  
res1=special_char(abc1) 
print(res)
print(res1)


### Cleaning column 
#Checking unique values of variable ‘Doors’ and replacing those by some other values.:
import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"]) # We are replacing special character "??"m available in coulmn with NaN values.
print(pd.unique(data_frame1['Doors'])) # ['three' '3' '5' '4' 'four' 'five' '2']
# in above we have few values in word and few as numbers , to avoid this we can replace the word values with number.
#replace() is used to replace a value with the desired value #Syntax: DataFrame.replace([to_replace, value, …])
data_frame1['Doors'].replace('three',3,inplace=True) # here we are using inplace so we need to reassign the updated dataframe again to dataframe. If we donot use inplace we need to use below.
data_frame1['Doors']=data_frame1['Doors'].replace('three',3) # Reassignment is needed of inplace is not used.
data_frame1['Doors'].replace('four',4,inplace=True)
data_frame1['Doors'].replace('five',5,inplace=True)
print(pd.unique(data_frame1['Doors']))# [3 '3' '5' '4' 4 5 '2'], please observer we have replace by word by equivalnet int and not converted to string.
print(data_frame1['Doors'].dtype,data_frame1['Doors'].nbytes)
data_frame1['Doors']=data_frame1['Doors'].astype('int64') # once we convert object to int64, all the string value will be converted to int , like '3' with be converted to int 3.  
print(pd.unique(data_frame1['Doors'])) 
print(data_frame1['Doors'].dtype,data_frame1['Doors'].nbytes)


###########missing data in pandas.
# Once all the special character or invalid char has been replaced by NaN we can search for missing values (i.e. NaN or Null) values.

#In Pandas missing data is represented by two value:

#None: None is a Python singleton object that is often used for missing data in Python code.
#NaN : NaN (an acronym for Not a Number), is a special floating-point value recognized by all systems that use the standard IEEE floating-point representation

    
import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.isnull() # TO get bool series of all columns for NaN (True) and not NaN(False)
data_frame1['Age'].isnull() # TO get it for specific column.

#To check the count of missing values present in each column Dataframe.isnull.sum
data_frame1.isnull().sum() # Sum of Null values of each column
data_frame1['Age'].isnull().sum() #Sum of Null values of particlaur column
  	
# filtering data  : displaying data(all columns) only where Age = NaN  
# creating bool series True for NaN values  
bool_series=data_frame1['Age'].isnull()
data_frame1[bool_series] 

# TO check the values of occurance of particular values in a column.
data_frame1['FuelType'].value_counts()
data_frame1['FuelType'].value_counts()
# Difference between size and count.
data_frame1.size
data_frame1.count()
print(data_frame1['FuelType'].size) # This will give the total count of rows including NaN or Null values.
print(data_frame1['FuelType'].count())# this will give only the non null (not NaN) values
print(data_frame1.size) # this will give row * column and also including NaN or Null values. 
print(data_frame1.count()) # this will give only the non null (not NaN) values of each column


# Example and Practice: 
#Filling missing values using fillna(), replace() and interpolate()

dropna()
replace()
interpolate()
  
import numpy as np
import pandas as pd
# dictionary of lists
dict = {'First Score':[100, 90,110, np.nan, 95,30,np.nan], 
        'Second Score': [30, 45, 56,59, np.nan,np.nan, 40], 
        'Third Score':[np.nan, 40, 80,45, 98,50,60]} 
# creating a dataframe from dictionary 
df = pd.DataFrame(dict)
df.isnull() # boolen true flase for null value.
df.notnull() # boolen true flase for null value.
df.isnull().sum() # Sum of all Null value in column
df.notnull().sum() # Sum of all Not Null value in column
df['First Score'].isnull().sum() # Sum of all Null value in column FIrst Score.
df['First Score'].isnull() # Bolean series where value in null in First Column column.
df[df['First Score'].isnull()] # All coulmns details of rows which have "FirstScore" couln value as NaN.
#df=df.fillna(1) # fill all NaN values with 1.
#df
#df=df.fillna(1) # to fill all column NaN value with value 1.
#df
#df['First Score']=df['First Score'].fillna(1) # to fill selective column NaN value with value 1.
#df
#inplace, another syntax to avoid reassignment. 
df['First Score'].fillna(1,inplace=True) #Here we have used inplace so we need not to reassign it to df again. 
df
#df=df.dropna() # drop the rows in which any couln have NaN value.
#df
df[df['First Score'].notnull()] # to select the rows which has "First Score" column value as Non NaN.


########### Exploratory data analysis:

####Frequency tables or frequency distribution:
# pandas.crosstab()  : To compute a simple cross-tabulation of one, two (or more) factors • By default computes a frequency table of the factors .

import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
print(data_frame1.shape)
pd.crosstab(index=data_frame1['FuelType'],columns='count') # Here index is row and columns is Column, We do not have 'count' column in csv file but that will be created on the fly by python to give the frequency count

##Two-way tables: To look at the frequency distribution of gearbox types with respect to different fuel types of the cars
pd.crosstab(index=data_frame1['Automatic'],columns=data_frame1['FuelType'],dropna=True) # Here rows are Automatic and columns are FuelType. SO it will give each fuel type count agaist all the different values in Automatic. In our case we have value as 0 and 1 for Automatic. So this will give us the relatrion between "Automatic" and "FuelType" columns ion our Toyota sheet.

#Two-way table - joint probability:  Joint probability is the likelihood of two independent events happening at the same time.

pd.crosstab(index=data_frame1['Automatic'],columns=data_frame1['FuelType'],normalize=True,dropna=True) # here normalize paarmeter is used to get the joint probability.
# in the output the probability for values (Automatic=0 and FuelType= "CNG") is 0.011228. Similary probability for vales (Automatic=0 and FuelType= "Petrol") is 0.826347
# Above can be said as probability of car being manual (Automatic=0) and FuelType being as CNG is 0.011228.

#Two-way table - marginal probability : Marginal probability is the probability of the occurrence of the single event : So basically it will give the row sum (all) and column sum(all):
pd.crosstab(index=data_frame1['Automatic'],columns=data_frame1['FuelType'],margins=True,normalize=True,dropna=True) # here we will get the row wise and column wise extra colums for sum or all. Here the sum of all values will be 1.

#Two-way table - conditional probability: Conditional probability is the probability of an event ( A ), given that another event ( B ) has already occurred.Example: Given the Type of 'Automatic', probalility of different FuelType.

#Here the addition of each row will be 1

pd.crosstab(index=data_frame1['Automatic'],columns=data_frame1['FuelType'],margins=True,normalize='index',dropna=True) # Here in normalize parametr we need to pass the event B , Lets have a example where we find out probability of fuel type on basis of Automatic gear Type. #Here the addition of each row will be 1.
# In above output the Given the Type of 'Automatic', probalility of different FuelType. SO given the Automatic value as 0(Gear Type Maual), Probability of FuelType ='CNG' as 0.011876.
# Above can also be said as probability of FuelType being CNG , given the car as manual (Automatic=0) is 0.011876.
#Also,given the Automatic value as 1(Gear Type Auto), Probability of FuelType ='CNG' as 0.0  
 
## In the reverse way we can have probability of Automatic gear Type on basis of fuel type  
pd.crosstab(index=data_frame1['Automatic'],columns=data_frame1['FuelType'],margins=True,normalize='columns',dropna=True) # Here each column sum will be 1. 
# In above output the Given the Type of FuelType, probalility of different Gear Type (Automatic) van be found. SO given the FuelType = 'CNG',Probability of Automatic as 0 is 1. Or given the FuelType = 'CNG',Probability of Automatic as 1 is 0 . OR given the FuelType = 'Petrol',Probability of Automatic as 0 is 0.937978.
# Above can also be said as probability of Automatic being 0(Manual) , given the FuelType as "Petrol" is 0.937978.


##### Corelation:: the strength of association between two variables 
#Corelation is measured by scattered plot between 2 variables. if y is also increasing/decreasing in increase/decrease of x , both variables are called as corelated.
#usually the value of corelation between 2 variables is between -1 to +1. negative corelation means increase in x will decrease the y. positive corelation means increase in x will increase the y. anything more than 0.7 (either possitive or negative) is considered as good corelated. corelation value 0 means no corelation and variable x and y are not corelated. 
# Corelation is mainly done on numerical data. In some case it can be for Categorical data as well but that is typical case.

# Syntax to find corelation: DataFrame.corr(self, method='pearson’)
#Above is used To compute pairwise correlation of columns excluding NA/null values .Excluding the categorical variables to find the Pearson’s correlation
import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame_numeric=data_frame1.select_dtypes(exclude=[object]) # Removing all the categorical data to keep only numeric data.
data_frame_numeric
corr_matrix=data_frame_numeric.corr()
corr_matrix

####### Writing Data or Output
#And finally, when you have produced results with your analysis, there are several ways you can export your data:

df.to_csv(filename) # Writes to a CSV file
df.to_excel(filename) # Writes to an Excel file
df.to_sql(table_name, connection_object) # Writes to a SQL table
df.to_json(filename) # Writes to a file in JSON format
df.to_html(filename) # Saves as an HTML table
df.to_clipboard() # Writes to the clipboard

#Exexersie:

# Write a program to read the toyata csv file and create a new csv with one more column for category and mark all the cars as expensive which price is more than 20000.

#Sol:
import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
print(data_frame1.shape)
data_frame1['Price'].isnull().sum() # O, means all the fields have correct values so no cleaning is required.
data_frame1_result=data_frame1[data_frame1['Price']>20000]
data_frame1_result.to_csv('Toyota_result.csv') # this will create a new file which will have all the rows which have price more than 20000.

#Sol2:

import os
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota_1.csv')
data_frame1.insert(2,'Category','') # here we are adding one more coulmn in data frame as "Category" in 2nd place with default value as ' '
#Please note it will be only added in dataframe and not in the csv file. we need to write to csv explicityly.
for i in range(0,len(data_frame1['Price'])):

    if data_frame1['Price'][i]<=10000:
        data_frame1['Category'][i]='Cheaper'
        #print('******A***********')
    elif data_frame1['Price'][i]<=15000:
        data_frame1['Category'][i]='Midium'
        #print('******B***********')
    else:
        data_frame1['Category'][i]='Expensive'
        #print('******C***********')
#data_frame1
data_frame1.to_csv('Toyota_1_result.csv')
data_frame_result=pd.read_csv('Toyota_1_result.csv')
pd.unique(data_frame_result['FuelType']) # 

"""
https://elitedatascience.com/python-cheat-sheet

Pandas, Numpy, and Scikit-Learn are among the most popular libraries for data science and analysis with Python.

Numpy is used for lower level scientific computation. Pandas is built on top of Numpy and designed for practical data analysis in Python. Scikit-Learn comes with many machine learning models that you can use out of the box.

In this cheat sheet, we’ll summarize some of the most common and useful functionality from these libraries. Let’s jump straight in!

Importing Data 
Any kind of data analysis starts with getting hold of some data. Pandas gives you plenty of options for getting data into your Python workbook:
"""

pd.read_csv(filename) # From a CSV file
pd.read_table(filename) # From a delimited text file (like TSV)
pd.read_excel(filename) # From an Excel file
pd.read_sql(query, connection_object) # Reads from a SQL table/database
pd.read_json(json_string) # Reads from a JSON formatted string, URL or file.
pd.read_html(url) # Parses an html URL, string or file and extracts tables to a list of dataframes
pd.read_clipboard() # Takes the contents of your clipboard and passes it to read_table()
pd.DataFrame(dict) # From a dict, keys for columns names, values for data as lists

Exploring Data 
Once you have imported your data into a Pandas dataframe, you can use these methods to get a sense of what the data looks like:

df.shape() # Prints number of rows and columns in dataframe
df.head(n) # Prints first n rows of the DataFrame
df.tail(n) # Prints last n rows of the DataFrame
df.info() # Index, Datatype and Memory information
df.describe() # Summary statistics for numerical columns
s.value_counts(dropna=False) # Views unique values and counts in columns
df.apply(pd.Series.value_counts) # Unique values and counts for all columns
df.describe() # Summary statistics for numerical columns
df.mean() # Returns the mean of all columns
df.corr() # Returns the correlation between columns in a DataFrame
df.count() # Returns the number of non-null values in each DataFrame column
df.max() # Returns the highest value in each column
df.min() # Returns the lowest value in each column
df.median() # Returns the median of each column
df.std() # Returns the standard deviation of each column

Selecting
Often, you might need to select a single element or a certain subset of the data to inspect it or perform further analysis. These methods will come in handy:

df[col] # Returns column with label col as Series
df[[col1, col2]] # Returns Columns as a new DataFrame
df.iloc[0] # Selection by position (selects first element)
df.loc[0] # Selection by index (selects element at index 0)
df.iloc[0,:] # First row
df.iloc[0,0] # First element of first column

Data Cleaning
If you’re working with real world data, chances are you’ll need to clean it up. These are some helpful methods:
df.columns = ['a','b','c'] # Renames columns


pd.isnull() # Checks for null Values, Returns Boolean Array
pd.notnull() # Opposite of s.isnull()
df.dropna() # Drops all rows that contain null values
df.dropna(axis=1) # Drops all columns that contain null values
df.dropna(axis=1,thresh=n) # Drops all rows have have less than n non null values
df.fillna(x) # Replaces all null values with x
s.fillna(s.mean()) # Replaces all null values with the mean (mean can be replaced with almost any function from the statistics section)
s.astype(float) # Converts the datatype of the series to float
s.replace(1,'one') # Replaces all values equal to 1 with 'one'
s.replace([1,3],['one','three']) # Replaces all 1 with 'one' and 3 with 'three'
df.rename(columns=lambda x: x + 1) # Mass renaming of columns
df.rename(columns={'old_name': 'new_ name'}) # Selective renaming
df.set_index('column_one') # Changes the index
df.rename(index=lambda x: x + 1) # Mass renaming of index

Filter, Sort and Group By
Methods for filtering, sorting and grouping your data:
Filter, Sort, and Group ByPython

df[df[col] > 0.5] # Rows where the col column is greater than 0.5
df[(df[col] > 0.5) & (df[col] < 0.7)] # Rows where 0.5 < col < 0.7
df.sort_values(col1) # Sorts values by col1 in ascending order
df.sort_values(col2,ascending=False) # Sorts values by col2 in descending order
df.sort_values([col1,col2], ascending=[True,False]) # Sorts values by col1 in ascending order then col2 in descending order
df.groupby(col) # Returns a groupby object for values from one column
df.groupby([col1,col2]) # Returns a groupby object values from multiple columns
df.groupby(col1)[col2].mean() # Returns the mean of the values in col2, grouped by the values in col1 (mean can be replaced with almost any function from the statistics section)
df.pivot_table(index=col1, values= col2,col3], aggfunc=mean) # Creates a pivot table that groups by col1 and calculates the mean of col2 and col3
df.groupby(col1).agg(np.mean) # Finds the average across all columns for every unique column 1 group
df.apply(np.mean) # Applies a function across each column
df.apply(np.max, axis=1) # Applies a function across each row


Joining and Combining
Methods for combining two dataframes:
df1.append(df2) # Adds the rows in df1 to the end of df2 (columns should be identical)
pd.concat([df1, df2],axis=1) # Adds the columns in df1 to the end of df2 (rows should be identical)
df1.join(df2,on=col1,how='inner') # SQL-style joins the columns in df1 with the columns on df2 where the rows for col have identical values. how can be one of 'left', 'right', 'outer', 'inner'<strong> </strong>



Machine Learning
The Scikit-Learn library contains useful methods for training and applying machine learning models. Our Scikit-Learn tutorial provides more context for the code below.

For a complete list of the Supervised Learning, Unsupervised Learning, and Dataset Transformation, and Model Evaluation modules in Scikit-Learn, please refer to its user guide.
