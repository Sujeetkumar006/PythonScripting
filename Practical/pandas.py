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

df=pd.read_csv('zoo.csv', delimiter = ',')

#To put the header on the excel sheet:

df=pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

# Print the whole dataframe
#The most basic method is to print your whole data frame to your screen. Of course, you don’t have to run the pd.read_csv() function again and again and again. Just store its output the first time you run it!

article_read = pd.read_csv('pandas_tutorial_read.csv', delimiter=';', names = ['my_datetime', 'event', 'country', 'user_id', 'source', 'topic'])

#After that, you can call this article_read value anytime to print your DataFrame!

article_read.head()
article_read.head(10)
article_read.tail()
#Or a few random lines by typing:
article_read.sample(5)


# For selecting the particular element:
article_read[['country', 'user_id']]

# filter: 
article_read[article_read.source == 'SEO']


import pandas as pd
df = pd.read_csv('F:/Study/StudyDocs_GoogleDrive/Prwatech/Classes/testdata/test1.csv', error_bad_lines=False)


import pandas as pd
df = pd.read_csv('test.csv', error_bad_lines=False)
df[0:3]

df.columns

df.Name 
df['Name'] # another syntesx for df.Name
df.Marks
df[['Name','Marks']] 


print(df['Marks'].max())
print(df['Marks'].mean())
print(df['Marks'].min())

df.describe() # will only include int and float coloumns


df[df.Marks>89]
df[]

###########missing data in pandas.

In Pandas missing data is represented by two value:

None: None is a Python singleton object that is often used for missing data in Python code.
NaN : NaN (an acronym for Not a Number), is a special floating-point value recognized by all systems that use the standard IEEE floating-point representation

isnull()
notnull()
dropna()
fillna()
replace()
interpolate()

# importing pandas package  
import pandas as pd  
    
# making data frame from csv file  
data = pd.read_csv("employees.csv")  
    
# creating bool series True for NaN values  
bool_series = pd.isnull(data["Gender"])  
   	
# filtering data  : displaying data only with Gender = NaN  
data[bool_series] 

Filling missing values using fillna(), replace() and interpolate()
  
# dictionary of lists 
dict = {'First Score':[100, 90, np.nan, 95], 
        'Second Score': [30, 45, 56, np.nan], 
        'Third Score':[np.nan, 40, 80, 98]} 
  
# creating a dataframe from dictionary 
df = pd.DataFrame(dict) 
  
# filling missing value using fillna()   
df.fillna(0)

### Filling Null value:  
data = pd.read_csv("employees.csv")  
  
# filling a null values using fillna()  
data["Gender"].fillna("No Gender", inplace = True)  
  
data 