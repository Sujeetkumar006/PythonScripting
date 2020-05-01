#Data Visualization :
""" Data visualization allows us to quickly interpret the data and adjust different variables to see their effect • Technology is increasingly making it easier for us to do so Why visualize data?
o Observe the patterns
o Identify extreme values that could be anomalies
o Easy interpretation"""

#Python offers multiple graphing libraries that offers diverse features
"""• matplotlib : to create 2D graphs and plots 
• pandas visualization : easy to use interface, built on Matplotlib 
•seaborn :provides a high-level interface for drawing attractive and informative statistical graphics 
• ggplot : based on R’s ggplot2, uses Grammar of Graphics • plotly • can create interactive plots
• cuffeling: dynamic plotting."""

# Matplotlib

"""• Matplotlib is a 2D plotting library which produces good quality figures
• Although it has its origins in emulating the MATLAB graphics commands, it is independent of MATLAB
• It makes heavy use of NumPy and other extension code to provide good performance even for large arrays"""

# ## Scattered Graph
""" A scatter plot is a set of points that represents the values obtained for two different variables plotted on a horizontal and vertical axes.
When to use scatter plots? • Scatter plots are used to convey the relationship between two numerical variables • Scatter plots are sometimes called correlation plots because they show how two variables are correlated"""

from matplotlib import pyplot as plt
x=[2,4,6,7]
y=[10,20,50,30]
z=[11,30,45,70]
#plt.plot(x,y,'g')
plt.scatter(x,z, color ='r')
plt.scatter(x,y, color ='g')
plt.title('FirstPLot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()

# Example 2:
import os
from matplotlib import pyplot as plt
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.dropna(axis=0, inplace=True) # we are removing NaN values.
#data_frame1
plt.scatter(data_frame1['Age'],data_frame1['Price']) 
plt.title('Sctaerrred Plot of Age vs Price')
plt.xlabel('Age')
plt.ylabel('Price')
plt.show()


### Histogram
"""• It is a graphical representation of data using bars of different heights 
• Histogram groups numbers into ranges and the height of each bar depicts the frequency of each range or bin
When to use histograms? • To represent the frequency distribution of numerical variables"""
# Example 1:
x=[2,4,6,7,12,23,4,5,56,76,88,99,76,56,54,46,34,56,78,99,76,43,45,67,8,45,21,36,78,]
y=[0,10,20,30,40,50,60,70,80,90]
z=[0,15,30,45,60,75,90]

plt.hist(x,y,histtype='bar')
#plt.hist(x,z,histtype='bar')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('FirstHist')
plt.show()

#Example 2: 
import os
from matplotlib import pyplot as plt
import pandas as pd
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.dropna(axis=0, inplace=True) # we are removing NaN values.
#data_frame1
plt.hist(data_frame1['KM']) # Here we have not given Y variable value so python will calculate the frequency of variables between some range and consider that as y axis values. this is the practicle and actual example of Histogram.
#plt.hist(data_frame1['KM'],color='green',edgecolor='grey',bins=10,) # methods with some extra parameter. 
plt.title('Histogram of Km')
plt.xlabel('Km Range')
plt.ylabel('Frequency')
plt.show()

# Bar plot 
"""What is a bar plot? • A bar plot is a plot that presents categorical data with rectangular bars with lengths proportional to the counts that they represent When to use bar plot? • To represent the frequency distribution of categorical variables 
• A bar diagram makes it easy to compare sets of data between different groups"""

# example 1:
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x=[2,4,6,7]
y=[10,20,50,30]
p=[1,2,3,5]
z=[11,30,45,50]
plt.bar(x,y, label ='data one')
plt.bar(p,z, label ='data two')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()

#example2:
import os
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.dropna(axis=0, inplace=True) # we are removing NaN values.
fuletype=list(data_frame1['FuelType'].unique()) # To get tyhe unique values of Fuel Type
countoEachFuelTyped=list(data_frame1['FuelType'].value_counts())
index=np.arange(len(fuletype)) # we are taking index as this will act as X-axis , as X axis can not be string we are concerting string to int to have X axis.
plt.bar(index,countoEachFuelTyped,color=['green','blue','red'])
plt.title('Bar chart for petrol Type')
plt.xlabel('Fuel Type')
plt.ylabel('Frequency')
plt.xticks(index, fuletype,rotation=90)
plt.legend()
plt.show()

# ## LIne Graph

from matplotlib import pyplot as plt
#import matplotlib
x=[2,4.5,6,7]
y=[10,20,50,30]
z=[11,30,45,70]
#plt.plot(x,y)
plt.plot(x,y,'k',label='Nifty')
plt.plot(x,z , 'r',label='Sensex')
plt.title('FirstPLot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()

#example 2:
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x=[2,4,6,7]
y=[10,20,50,30]
z=[11,30,45,70]
#plt.plot(x,y,'g',label='firstline',linewidth=3)
#plt.plot(x,z,'r',label='secondline',linewidth=3)
plt.plot(x,y,'g',label='school1',linewidth=3)
plt.plot(x,z,'r',label='school2',linewidth=5)
plt.title('FirstPLot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.legend()
plt.grid(True, color='k')
plt.show()

# stack Plot:
x=[1,2,3,4,5]

y=[5,6,8,3,2]
z=[1,3,2,5,6]
p=[3,7,2,4,7]

plt.plot([],[],color='c', label='y', linewidth ='5')
plt.plot([],[],color='m', label='z', linewidth ='5')
plt.plot([],[],color='r', label='p', linewidth ='5')

plt.stackplot(x,y,z,p,colors=['c','m','r'])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.show()

# Pie CHart:
slices =[2,3,5,2]
language=['eng','Hindi','MArathi', 'TAmil']
col=['b','g','m','c']
plt.pie(slices,labels=language, colors=col,autopct='%1.3f%%')
plt.title('FIrstPieChart') 
plt.show()          
          
		 
########### Seaborn #############
""" Seaborn is a Python data visualization library based on matplotlib 
 It provides a high-level interface for drawing attractive and informative statistical graphics """

# Scatter plot: 
 import os
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.dropna(axis=0, inplace=True) # we are removing NaN values.
sns.set(style='darkgrid')
sns.regplot(x=data_frame1['Age'],y=data_frame1['Price']) # here in seaborn we have advantage that we have regplot which is nothing but regression plot, so the graph will also have the regresion line in  our scattered plot as default.
#sns.regplot(x=data_frame1['Age'],y=data_frame1['Price'],fit_reg=False) # IN Ccase regression line is not needed.
#sns.regplot(x=data_frame1['Age'],y=data_frame1['Price'],marker='*',fit_reg=False) # in case if you want * in place of dot(.) in the graph.
plt.title('Sctaerrred Plot of Age vs Price')
#plt.xlabel('Age') # here in seaborn we need not to write this , it will automtcally be taken from data type. So label will automatically been taken from variable name.
#plt.ylabel('Price')
plt.show()

### Scatter plot of Price vs Age by FuelType
#Using hue parameter, including another variable to show the fuel types categories with different colors
 import os
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.dropna(axis=0, inplace=True) # we are removing NaN values.
sns.set(style='darkgrid')
#sns.regplot(x=data_frame1['Age'],y=data_frame1['Price'])
#sns.regplot(x=data_frame1['Age'],y=data_frame1['Price'],fit_reg=False) # IN Ccase regression line is not needed.
sns.lmplot(x='Age',y='Price',data=data_frame1,fit_reg=True,hue='FuelType',legend=True,palette='Set1')
plt.title('Sctaerrred Plot of Age vs Price')
plt.show()


## Histogram:
#Histogram with default kernel density estimate

import os
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.dropna(axis=0, inplace=True) # we are removing NaN values.
sns.distplot(data_frame1['Age'])
sns.distplot(data_frame1['Age'], kde=False)  # in case keranl density is not needed.
sns.distplot(data_frame1['Age'], kde=False, bins=5) # to fix the number of bins

### Bar Plot:
import os
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.dropna(axis=0, inplace=True) # we are removing NaN values.
#sns.distplot(data_frame1['Age'])
sns.countplot(x='FuelType', data=data_frame1) # if you observer unlike to matplotlib , we do not need to give the count of each Fuel Type manually, rather it has been taken care by Seaborn library so seaborn is more advance. 

#Grouped bar plot of FuelType and Automatic
sns.countplot(x='FuelType', data=data_frame1, hue='Automatic')

### Box and whiskers plot – numerical variable 
#Box and whiskers plot of Price to visually interpret the five-number summary
# it helps in removal of outliears
import os
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.dropna(axis=0, inplace=True) # we are removing NaN values.
#sns.distplot(data_frame1['Age'])
sns.boxplot(y=data_frame1['Price'])

# Box and whiskers plot for numerical vs categorical variable Price of the cars for various fuel types :
sns.boxplot(x=data_frame1['FuelType'],y=data_frame1['Price'])

#Grouped box and whiskers plot  Grouped box and whiskers plot of Price vs FuelType and Automatic
sns.boxplot(x=data_frame1['FuelType'],y=data_frame1['Price'],hue='Automatic',data=data_frame1)

### Multiple plots in same graph:
#Let’s plot box-whiskers plot and histogram on the same window 
#Split the plotting window into 2 parts 
import os
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.dropna(axis=0, inplace=True) # we are removing NaN values.
f,(ax_box,ax_hist)=plt.subplots(2,gridspec_kw={"height_ratios":(0.15,0.85)}) # this is to scale the graph
#sns.distplot(data_frame1['Age'])
sns.boxplot(data_frame1['Price'],ax=ax_box)
sns.distplot(data_frame1['Price'],ax=ax_hist,kde=False)


########Pairwise plots : 
"""
It is used to plot pairwise relationships in a dataset Creates scatterplots for joint relationships and histograms for univariate distributions
"""

import os
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
os.chdir('F:\Study\StudyDocs_GoogleDrive_Latest\Training\workspace')
data_frame1=pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
data_frame1.dropna(axis=0, inplace=True) # we are removing NaN values.
sns.pairplot(data_frame1, kind='scatter',hue='FuelType')
plt.show()

