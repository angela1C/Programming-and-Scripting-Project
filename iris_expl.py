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

col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']

iris =  pd.read_csv('iris_data.csv', names = col_names)

## Viewing the dataset
# look at the top 5 observations
print("The top 5 observations are as follows:")
print(iris.head())
# look at the bottom 5 observations
print("The last 5 observations are as follows:")
print(iris.tail())
# the first column of data is the index of the dataframe. It is a range from 0 to 150
print(f"The DataFrame has an index of {iris.index}")
print(f"The names of the DataFrame are {iris.columns}")
print(iris.columns)
## check for any missing values using pandas.isnull() or the opposite using pandas.notnull()
print(pd.isnull(iris).sum())

print(pd.notnull(iris).sum())


# by default index.col is set to a range from 0 to the number of rows. 
# This is fine for here. I would prefer to have the row number starting from 1 and the last observation 150

# can write the DataFrame to a comma separated file to save any changes including column names added


iris.to_csv('iris1.csv')

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
print(iris['Sepal_Length'].head())

## Selecting and Filtering 

# can retrieve a column of data from the iris DataFrame using dict-like notation or by attribute:
print(iris.Petal_Width.head())

# rows of the iris DataFrame can be retrieved by position name or using the loc attribute.
# The index operators can be used to select a subset or rows and columns.
# loc for axis labels or iloc for integers
# retrieve first observation retrieved as a DataFrame
# The index for the iris DataFrame at the moment is just a range of integers from 0 to 150 
iris.loc[[0]] 
# retrieve as a Series
iris.loc[0]

# I could add a new column by assigning a column that doesnt exist already.
# I might add a new column of labels from 1 to 150 and maybe combined with the species type.
# I dont like the index starting from 0 up to 149! 

# can index into the dataframe to retrieve one or more columns either with a single value or a sequence
print(iris[0:5])

 # can use Boolean operators to select rows that meet certain conditions.

iris[iris.Sepal_Length > 7]

iris.iloc[:,4].head()

# can sort the DataFrame by one or more of the columns.
# put the columns in the order to sort by
iris.sort_values(by =['Petal_Width','Species'])
iris.sort_values(by =['Species','Petal_Length'])
iris.sort_values(by =['Species','Sepal_Length'])
iris.sort_values(by =['Species','Sepal_Width'])

iris.sort_values(by =['Species','Petal_Length'])


## Summary statistics

iris.describe()

iris.cov()
iris.corr()


## Data Cleaning and Transformation


# the duplicated method can be used to return a boolean series indicating 
# whether each row is a duplicate of another row or not.

#plt.figure()

iris.plot.hist(bins =50)
plt.suptitle(r'iris histograms',fontsize = 14)
plt.show()

