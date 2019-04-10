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

col_names = ['Sepal_Length','Sepal_Width','Petal_length','Petal_Width','Species']

iris =  pd.read_csv('iris_data.csv', names = col_names)

print(iris.head())

# the first column of data is the index of the dataframe. It is a range from 0 to 150
#print(iris_df.index())

## check for any missing values.

print(iris.isnull())
print(pd.isnull(iris))
print(iris[pd.isnull()])

# by default index.col is set to a range from 0 to the number of rows. 
# This is fine for here. I would prefer to have the row number starting from 1 and the last observation 150

# can write the DataFrame to a comma separated file to save any changes including column names added

print(iris.head())
iris.to_csv('iris1.csv')
