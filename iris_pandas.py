import numpy as np 
import pandas as pd  

# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#getting-data-in-out


# First to read the dataset into Python using Pandas.

# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#getting-data-in-out
import pandas as pd

# located the data at the UCI Machine Learning Repository

# here I am reading in the file directly from the URL by giving the full path  to the read_csv command.
# Alternatively I could download the dataset and save in the folder but this is working ok.
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#csv-text-files

# https://cmdlinetips.com/2018/01/7-tips-to-read-a-csv-file-as-pandas-data-frame/

#data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header =None)

## save link to data and reference the link 
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

## the data read in does not have any column names. Specify header = None to avoid reading the 
# first row of data as a header or column name
iris_data = pd.read_csv(csv_url, header = None)

# View the top and bottom of the dataframe
"""
# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#viewing-data
# `describe` shows a quick summary statistic of the data

""" 

print(iris_data.head())
print(iris_data.tail())

## give column names to the read_csv command. 
# The column names are the attribute information from the iris.names files
# (https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names)

"""
Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica
"""

# create a list containing the correct column names for the iris dataset
col_names = ['Sepal_Length','Sepal_Width','Petal_length','Petal_Width','Species']

# read in the dataset from the UCI Machine Learning Repository link and specify column names to use
# save as iris_df
iris_df =  pd.read_csv(csv_url, names = col_names)
## see the first few rows
print(iris_df.head())
print(iris_df.tail())
print(iris_df.describe())
