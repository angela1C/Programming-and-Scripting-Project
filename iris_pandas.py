import numpy as np 
import pandas as pd  

import pandas as pd

# located the data at the UCI Machine Learning Repository

# here I am reading in the file directly from the URL by giving the full path  to the read_csv command.
# Alternatively I could download the dataset and save in the folder but this is working ok.

# save link to data and reference the link 
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# The data read in does not have any column names. Specify header = None to avoid reading the 
# first row of data as a header or column name
# This creates a panda dataframe. 
iris_data = pd.read_csv(csv_url, header = None)

# View the top and bottom of the dataframe

print(iris_data.head())
print(iris_data.tail())

## give column names to the read_csv command. 
# The column names are the attribute information from the iris.names files
# (https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names)

# create a list containing the correct column names for the iris dataset
col_names = ['Sepal_Length','Sepal_Width','Petal_length','Petal_Width','Species']

# read in the dataset again from the UCI Machine Learning Repository link and this time specify column names to use
# save as iris_df
iris_df =  pd.read_csv(csv_url, names = col_names)

# describe() shows a quick summary statistic of the data including count, mean, standard deviation, percentiles.
# It generates descriptive statistics summarising the central tendancy, dispersion and shape of the 
# dataset's distribution. 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe
print(iris_df.describe())

# using basic pandas features

print(iris_df.head())

# A Column in a DataFrame can be retrieved as a Series as follows:

SL = iris_df['Sepal_Length']
print(SL.head())

SW = iris_df.Sepal_Width
print(SW.head())

# 'Sepal_Length','Sepal_Width','Petal_length','Petal_Width','Species'

#Rows can be retrieved by position or name using the `loc` attribute

obs0 = iris_df.loc(1)

# can filter with Boolean expressions


