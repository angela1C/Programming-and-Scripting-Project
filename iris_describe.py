# iris_describe.py
# Angela Carpenter

# This script contains a subsection of the code from the main python script so that the entire scripy including graphs does not need to be run each time.
#


# 1. IMPORT PYTHON LIBRARIES

# In order to use python libraries that are not part of the standard python library, they first need to be imported.
# Here I import the pandas library, the matplotlib pyplot library and the seaborn library using short name aliases pd, plt and sns. 
# This seems to be the conventional way to import these particular packages.

print("First importing the python libraries...")
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns

# help can be obtained using the python help function.
# help(pd) or help(pd.DataFrame.describe())

# 2. LOADING / READING IN THE IRIS DATA SET INTO PYTHON


# Create a variable `csv_url` and pass to it the url where the data set is available at 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'. 
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# I have also saved the csv file to the folder or repository and can read it in from there in case for some reason the url is not available.

# Create a list of column names `col_names` using the iris attribute information available at the UCI machine learning repository.
# passing the column names to the names parameter of read_csv
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

iris =  pd.read_csv(csv_url, names = col_names)

# to read the csv file from a csv file in the same folder as this script.
# iris = pd.read_csv('iris_data.csv', names = col_names)

# using the pandas DataFrame method head to return the first rows of the DataFrame and check that the file was correctly loaded
print("The first 10 rows of the iris dataframe:")
print(iris.head(10))

# using the pandas DataFrame method tail to return the last rows of the DataFrame and check that the file was correctly loaded
print("The last 10 rows of the iris dataframe:")
print(iris.tail(10))

# check the data types to ensure they have been correctly inferred by read_csv
print(iris.dtypes)

# 3. EXPLORING AND INVESTIGATING THE IRIS DATA SET 

# Having imported the iris data set from a csv file into a pandas `DataFrame`, all the attributes and methods of `DataFrame` objects can be used on the iris DataFrame object.

# First looking at the attributes of the iris DataFrame created from importing the iris data set above.

# Getting the number of axes / array dimensions of the iris DataFrame using ndim attribute
print(f"The iris DataFrame has {iris.ndim} dimensions.\n")

# Look at the shape of the iris DataFrame as this shows the number of rows and columns in the table or matrix of data
# This will show how many rows (containing observations) and columns (containing features/variables)
print(f"The Iris DataFrame set consists of {iris.shape[0]} rows and {iris.shape[1]} columns corresponding to the rows and columns of the csv file.\n")

# the number of elements in the iris object.
print(f"There are {iris.size}  elements in total.\n")

# The DataFrame has both a row and a column index which were automatically assigned when the DataFrame was created.
# Get the column labels of the iris DataFrame using  'pandas.DataFrame.columns'
print("The column labels of the iris DataFrame are as specified when reading in the csv file: \n", *iris.columns, sep = "   ")

# the row index 
print(f"\n The index of the DataFrame is: \n", iris.index)
#print("The index for the rows are ",*iris.index)
print("\n This index was automatically assigned when the DataFrame was created above.\n")

# the dtypes (data types) of the iris DataFrame
print(f"The data types of iris DataFrame are as follows:\n")
print(iris.dtypes)

# pandas.DataFrame.axes return a a list representing the axes of the iris DataFrame which shows the row axis labels and the column axis labels in that order. This returns the same information as the index and columns attribute
print(iris.axes)
#print("The row axis labels of the iris DataFrame are  ", *iris.axes[0])
print("\n The row axis labels of the iris DataFrame is a range from ", *iris.axes[0][[0]], *iris.axes[0][[1]], *iris.axes[0][[2]],"..." , *iris.axes[0][[-3]],*iris.axes[0][[-2]], *iris.axes[0][[-1]],"\n" )
print("The column axis labels of the iris DataFrame are as follows:\n ",*iris.axes[1])

# Now using some of the DataFrame methods to explore the Iris DataFrame

# Look at the first ten observations in the DataFrame. The number of 
print(iris.head(10))

# Look at the last ten observations in the DataFrame
print(iris.tail(10))

# It is possible to check for missing values in the DataFrame using the panda's `isnull()` method.
# This shows that there are no missing values which is as expected for this particular data set.# Detect missing values in the DataFrame. 
# Sum the values instead of printing the boolean values as True = 1.
print("The number of null or missing values in the iris dataframe for each column: ")
print(iris.isnull().sum())

# Print a concise summary of the iris DataFrame.
print(f"A concise summary of the iris DataFrame: \n")
iris.info()

# Count non-NA cells for each column or row.
print(f"\n The number of non-NA cells for each column or row are: \n {iris.count()}")

print(f"Checking to see if there are missing values. \n {iris.isnull().sum()}")

# Using the `unique()` method on the 'Class' column to show how many different class or species of Iris flower is in the data set.

iris['Class'].unique()
species_type =iris['Class'].unique()
print("The following are the three class or species types of iris in the data set \n",*species_type, sep = " ")

# count  the number of distinct observations for each column 
iris.nunique()

# look at the summary statistics of the DataFrame
print("Here are some summary statistics for the iris DataFrame: \n")
print(iris.describe())

####   ####   ####   ####   ####   ####§
