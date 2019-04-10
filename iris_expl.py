# first importing the following libraries
import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt 


## save link to data and reference the link 
#csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

## the data read in does not have any column names. Specify header = None to avoid reading the 
# first row of data as a header or column name

#iris_data = pd.read_csv(csv_url, header = None)

iris = pd.read_csv('iris_data.csv', header =  None)

# using the attribute information as the column names
col_names = ['Sepal_Length_cm','Sepal_Width_cm','Petal_Length_cm','Petal_Width_cm','Class']

iris =  pd.read_csv('iris_data.csv', names = col_names)

## Viewing the dataset
# look at the top 5 observations
print("The top 5 observations are as follows:")
print(iris.head())
# look at the bottom 5 observations
print("The last 5 observations are as follows:")
print(iris.tail())
# The Data Frame has 5 columns, with the first 4 being the attributes or features of the data set. 
# The last column is the class or type of iris plant each observation belongs to.
# Each row correspond to an individual observation of an iris plant.

# the first column of data is the index of the dataframe. It is a range from 0 to 150
print(f"The DataFrame has an index of {iris.index}")

# column names of the Data Frame
print(iris.columns)


## Missing Values

## check for any missing values using pandas.isnull() or the opposite using pandas.notnull()
print(pd.isnull(iris).sum())

print(pd.notnull(iris).sum())


# by default index.col is set to a range from 0 to the number of rows. 
# This is fine for here. I would prefer to have the row number starting from 1 and the last observation 150

# can write the DataFrame to a comma separated file to save any changes including column names added


iris.to_csv('iris_data.csv')

# Detecting and Filtering outliers

# can see the sumamry statistics of the dataset using the pandas.describe() function.
# can then look at observations that have values exceeding soem statistic values using boolean.

# basic descriptive statistics for each column of the data in the Iris DataFrame
print(iris.describe())

#  how many rows in the iris DataFrame?
print(len(iris))

# The shape of the dataset
print(iris.shape)

print(iris.columns)
# can retrieve a column of data from the iris DataFrame using dict-like notation
print(iris['Sepal_Length_cm'].head())

# can find how many different plants of each class or species using unique

species_type =iris['Class'].unique()
print("The following are the three class or species types of iris in the data set \n",*species_type, sep = " ")
# unpack the list and print the sequence without brackets. (https://stackoverflow.com/a/35119046)




# Selecting and Filtering 

# can index using the square brackets and this will return a Series corresponding to the column name.
# can retrieve a column of data from the iris DataFrame using dict-like notation or by attribute:
print(iris.Petal_Width_cm.head())

# rows of the iris DataFrame can be retrieved by position name or using the loc attribute.
# The index operators can be used to select a subset or rows and columns.
# loc for axis labels or iloc for integers
# retrieve first observation retrieved as a DataFrame
# The index for the iris DataFrame at the moment is just a range of integers from 0 to 150 
iris.loc[[0]] 
# retrieve as a Series
iris.loc[0]

# I could add a new column by assigning a column that doesn't exist already.
# I might add a new column of labels from 1 to 150 and maybe combined with the species type.
# I dont like the index starting from 0 up to 149! 

# can index into the dataframe to retrieve one or more columns either with a single value or a sequence
print(iris[0:5])

# Boolean Indexing
# can use Boolean operators to select rows that meet certain conditions.

iris[iris.Sepal_Length_cm > 7]

iris.iloc[:,4].head()

# can sort the DataFrame by one or more of the columns.
# put the columns in the order to sort by
iris.sort_values(by =['Petal_Width_cm','Class'])
iris.sort_values(by =['Class','Petal_Length_cm'])
iris.sort_values(by =['Class','Sepal_Length_cm'])
iris.sort_values(by =['Class','Sepal_Width_cm'])

iris.sort_values(by =['Class','Petal_Length_cm'])


## Summary statistics

# Can look at summary statistics for the overall data set.
iris.describe()

# can use boolean indexing to look at the data.
# maybe look at 

# sl_mean =iris.Sepal_Length_cm.mean()
# print(sl_mean)
# print(iris[iris.Sepal_Length_cm] > sl_mean)

iris2 = iris.copy()
print(iris2.describe())


iris.cov()
iris.corr()


## Data Cleaning and Transformation


# the duplicated method can be used to return a boolean series indicating 
# whether each row is a duplicate of another row or not.

#plt.figure()

# Visualising the data set

# can 
# plt.figure()
# iris.plot.hist(bins =50)
# plt.suptitle('iris histograms',fontsize = 14)
# plt.show()

# plt.figure()
# plt.suptitle('iris histograms of measurements',fontsize = 14)
# iris['Class'].plot.hist(bins = 30)
# plt.show()

# plt.scatter()