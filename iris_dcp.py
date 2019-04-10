# Data cleaning and preparation
"""
data preparation tasks include data loading, cleaning, transforming and rearranging


"""
# Loading the data

# first importing the following libraries
import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt 


## save link to data and reference the link.
# The link is now working again. Previously the certificate for the page had expired.
# Therefore I read in the data from the csv file I had initially downloaded
iris_csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# the data read in does not have any column names. 
# Specify header = None to avoid reading the first row of data as a header or column name

iris_data = pd.read_csv(iris_csv_url, header = None)

#iris = pd.read_csv('iris_data.csv', header =  None)

col_names = ['Sepal_Length','Sepal_Width','Petal_length','Petal_Width','Species']

iris =  pd.read_csv(iris_csv_url, names = col_names)

print(iris.head())

# Handling missing data


print(iris.isnull())

# can look at a subset of the data by using square brackets
SL = iris['Sepal_Length']
print(SL.head())
