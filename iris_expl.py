# first importing the following libraries
import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns

# READING IN THE IRIS DATA SET

# save url to data and reference the link 
#csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# As the data does not have any column names, specify header = None to avoid reading the 
# first row of data as a header or column name

#iris_data = pd.read_csv(csv_url, header = None)

iris = pd.read_csv('iris_data.csv', header =  None)

# using the attribute information as the column names
col_names = ['Sepal_Length_cm','Sepal_Width_cm','Petal_Length_cm','Petal_Width_cm','Class']

iris =  pd.read_csv('iris_data.csv', names = col_names)

# EXPLORING THE IRIS DATA SET IN PYTHON

# look at the first 10 observations
print("The top 10 observations are as follows:")
print(iris.head(10))
# look at the last 10 observations
print("The last 10 observations are as follows:")
print(iris.tail(10))

# look at the complete DataFrame
print(iris) 

# The DataFrame has an index which was automatically assigned when the DataFrame was created
# on reading in the csv file. The index is a range from 0 to 150
print(iris.index)

print(iris.shape)
# see the column names of the Data Frame
print(iris.columns)

# MISSING VALUES

#  Check for any missing values using pandas.isnull() or the opposite using pandas.notnull()
# not expecting any missing values in this data set
print(pd.isnull(iris).sum())
print(pd.notnull(iris).sum())


# by default index.col is set to a range from 0 to the number of rows. 

# can write the DataFrame to a comma separated file to save any changes including column names added
iris.to_csv('iris_data.csv')

# BASIC STATISTICS OF THE IRIS DATA SET

iris.mean()  # to get the mean

iris.describe() # to get summary statisitcs of the data set

# basic descriptive statistics for each column of the data in the Iris DataFrame
print(iris.describe())

# Detecting and Filtering outliers
# can then look at observations that have values exceeding some statistic values using boolean.


#  how many rows in the iris DataFrame?
print(len(iris))

# The shape of the dataset
print(iris.shape)

print(iris.columns)
# can retrieve a column of data from the iris DataFrame using dict-like notation
print(iris['Sepal_Length_cm'].head())

# how many different classes or species can be found using unique

species_type =iris['Class'].unique()
print("The following are the three class or species types of iris in the data set \n",*species_type, sep = " ")
# unpack the list and print the sequence without brackets. (https://stackoverflow.com/a/35119046)

## FISHERS TABLES 1 AND TABLE 2
# Table 1 in Fishers paper shows the same data as printing the DataFrame.
iris.head()

# Fisher's table 2 shows the difference in means for the setosa and versicolor species
# use groupby with "Class" variable and then get the mean of each class for each measurement variable.
# Transpose the rows and columns
means = iris.groupby("Class").mean().T
# only getting the columns up to Iris-versicolor
means.loc[:,'Class':'Iris-versicolor'] 
# make it into a DataFrame

# Going to do it for all the species. 
# create a dataframe from grouping the iris dataframe by class and calculating the group means
pd.DataFrame(iris.groupby("Class").mean().T)

# add a new column for the difference in means between the Versicolor and Setosa species
means['diff (Versicolor - Setosa)'] = means['Iris-versicolor'] - means['Iris-setosa']

# add a new column for the difference in means between the Versicolor and Virginica species
means['diff (Versicolor - Virginica)'] = means['Iris-versicolor'] - means['Iris-virginica']

# add a new column for the difference in means between the Versicolor and Virginica species
means['diff (Virginica - Setosa)'] = means['Iris-virginica'] - means['Iris-setosa']



# INDEXING AND FILTERING DATA

# SEPARATE DATA FRAMES FOR EACH SPECIES

# separate the different classes into different dataFrames.

# select from the iris DataFrame only the rows where the Class equals the string "Iris-setosa"
iris_setosa = iris[iris['Class'] == "Iris-setosa"]
print(iris_setosa).head()
# how many setosas is there.
print(iris_setosa.count())

# a quick summary statistics for the Setosa variation only
iris_setosa.describe()

# select from the iris DataFrame only the rows where the Class equals the string "Iris-setosa"
# save to a new DataFrame
iris_versicolor = iris[iris['Class'] == "Iris-versicolor"]
iris_versicolor.head()

iris_versicolor.describe()

# select from the iris DataFrame only the rows where the Class equals the string "Iris-virginica"
# save to a new DataFrame
iris_virginica = iris[iris['Class'] == "Iris-virginica"]
iris_virginica.head()



# Here subsetting the data to meet a given criteria.
# http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-with-isin
values =  {'Class': ['Iris-versicolor', 'Iris-virginica']}
row_mask = iris.isin(values).any(1)
iris[row_mask]

# GROUPBY
# can use the groupby functions to look at statistics at the species level
iris_grouped = iris.groupby("Class")
print(iris_grouped.mean())
print(iris_grouped.count())


"""
http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#the-query-method
DataFrame objects have a query() method that allows selection using an expression.

You can get the value of the frame where column b has values between the values of columns a and c
Using pure python:
df[(df.a < df.b) & (df.b < df.c)]

Using query
df.query('(a < b) & (b < c)')

"""
# Just trying out the filtering here using the query method.
iris[(iris.Sepal_Length_cm > iris.Sepal_Width_cm)].count()

iris.query('Sepal_Length_cm > Sepal_Width_cm & Petal_Length_cm > Petal_Width_cm').count()




# Selecting and Filtering 

# can retrieve a column of data from the iris DataFrame using dict-like notation or by attribute:
print(iris.Petal_Width_cm.head())

# rows of the iris DataFrame can be retrieved by position name or using the loc attribute.
# The index operators can be used to select a subset or rows and columns using loc for axis labels or iloc for integers
# The index for the iris DataFrame at the moment is a range of integers from 0 to 150 
# double square brackets [[]] to retrieve as a DataFrame while single brackets[] ro retrieve as a Series.
iris.loc[[0]] 
# retrieve as a Series
iris.loc[0]

# Index into the dataframe to retrieve one or more columns either with a single value or a sequence
# first 5 rows
print(iris[0:5])

# Boolean operators to select rows that meet certain conditions.

iris[iris.Sepal_Length_cm > 7]

iris.iloc[:,4].head()

iris_setosa = iris[Class =="Iris-setosa"]

# can sort the DataFrame by one or more of the columns, place the columns to first sort by first

iris.sort_values(by =['Petal_Width_cm','Class'])
iris.sort_values(by =['Class','Petal_Length_cm'])
iris.sort_values(by =['Class','Sepal_Length_cm'])
iris.sort_values(by =['Class','Sepal_Width_cm'])

iris.sort_values(by =['Class','Petal_Length_cm'])


## Summary statistics


iris2 = iris.copy()
print(iris2.describe())


iris.cov()
iris.corr()


# Detecting and Filtering outliers

# can see the sumamry statistics of the dataset using the pandas.describe() function.
# can then look at observations that have values exceeding soem statistic values using boolean.
