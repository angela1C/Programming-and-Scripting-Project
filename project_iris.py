# project_iris.py
# Angela Carpenter
# This script contains my script



# 1. IMPORT PYTHON LIBRARIES

# In order to use python libraries that are not part of the standard python library, they first need to be imported.
# Here I import the pandas library, the matplotlib pyplot library and the seaborn library using short name aliases pd, plt and sns. 
# This seems to be the conventional way to import these particular packages.

print("First importing the python libraries")
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
print(f"The iris dataframe has {iris.ndim} dimensions")

# Look at the shape of the iris DataFrame as this shows the number of rows and columns in the table or matrix of data
# This will show how many rows (containing observations) and columns (containing features/variables)
print(f"The Iris data set has {iris.shape[0]} rows and {iris.shape[1]} columns")

# the number of elements in the iris object.
print(f"The Iris DataFrame has {iris.size} elements in total")

# The DataFrame has both a row and a column index which were automatically assigned when the DataFrame was created.
# Get the column labels of the iris DataFrame using  'pandas.DataFrame.columns'
print("The column labels of the iris DataFrame are: ", *iris.columns, sep = "   ")

# the row index 
print(f" The index of the dataframe is: ", iris.index)
print("The index for the rows are ",*iris.index)
print("This index was automatically assigned when the DataFrame was created above")

# the dtypes (data types) of the iris DataFrame
print(f"The data types of iris dataframe are as follows:")
print(iris.dtypes)

# Return the ftypes (indication of sparse/dense and dtype) in the iris DataFrame.
print(iris.ftypes)

# pandas.DataFrame.axes return a a list representing the axes of the iris DataFrame which shows the row axis labels and the column axis labels in that order. This returns the same information as the index and columns attribute
print(iris.axes)
print("The row axis labels of the iris DataFrame are  ", *iris.axes[0])
print("The column axis labels of the iris DataFrame are as follows:\n ",*iris.axes[1])

# Now using DataFrame methods to explore the Iris DataFrame

# Look at the first ten observations in the DataFrame
print(iris.head(10))

# Look at the last ten observations in the DataFrame
print(iris.tail(10))

# It is possible to check for missing values in the DataFrame using the panda's `isnull()` method.
# This shows that there are no missing values which is as expected for this well known data set consisting of 150 instances of 5 attributes.
print("The number of null or missing values in the iris dataframe: ")
print(iris.isnull().sum())

# look at the summary statistics of the DataFrame
print("summary statistics for the iris dataframe")
print(iris.describe())

# Print a concise summary of the iris DataFrame.
print(iris.info())

# Count non-NA cells for each column or row.
print(iris.count())

# It is possible to check for missing values in the DataFrame using the panda's isnull() and isna() methods.
# There should be no missing values in this DataFrame as there are no missing values in the csv file from which it is created. 

# Detect missing values in the DataFrame. Sum the values instead of printing the boolean values as True = 1.
# iris.isna().sum()
iris.isnull().sum()
iris.notnull().sum()
# iris.notna().sum()
iris.count()

# Make a histogram of the DataFrame. 
# A histogram will be produced for each of the four numeric columns in the iris data set.
# The number of bins can be specified. 

# DataFrame.hist() plots the histograms of the columns on multiple subplots:
print("Histogram of the distribution of the iris data. Make sure to close the plot to continue. ") 
iris.hist(alpha=0.8, bins=30, figsize=(12,8))
plt.show()

print("Boxplot the distribution of the iris data. Make sure to close the plot to continue. ") 
iris.plot.box(figsize=(12,8))
plt.show()

# count distinct observations.
iris.nunique()

# Using the `unique()` method to show how many different class or species of Iris flower is in the data set.

iris['Class'].unique()
species_type =iris['Class'].unique()
print("The following are the three class or species types of iris in the data set \n",*species_type, sep = " ")


# pandas.DataFrame.plot.scatter
# Create a scatter plot with varying marker point size and color. 
# DataFrame.plot.scatter(x, y, s=None, c=None, **kwds)[source]



# 4. EXPLORING IRIS DATA SET BY SPECIES

## Here I am subsetting the data to meet a given criteria su
# http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-with-isin
values =  {'Class': ['Iris-versicolor', 'Iris-virginica']}
row_mask = iris.isin(values).any(1)
iris[row_mask].head()

# select from the iris DataFrame only the rows where the Class equals the string "Iris-setosa"
iris_setosa = iris[iris['Class'] == "Iris-setosa"]
print("Selecting from the iris dataframe only those rows containing the Class Iris-setosa")
print(iris_setosa.head())

# subsetting the data to meet a given criteria.
# http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-with-isin
values =  {'Class': ['Iris-versicolor', 'Iris-virginica']}
row_mask = iris.isin(values).any(1)
print(" subsetting the dataframe using Boolean masks")
print(iris[row_mask].head())
# GROUP BY 

print("using groupby to split the iris dataframe by Class of iris species")
# Using groupby functions to look at statistics at the class / species level
iris_grouped = iris.groupby("Class")

# Compute count of group, excluding missing values.
print(iris.groupby("Class").count())

# Groupby Class and return the mean of the remaining columns in each group.
print(iris.groupby('Class').mean())

# Group by class and then return the first observations in each group
iris.groupby("Class").first()

# Group by class and then return the last observations in each group
iris.groupby("Class").last()

# get the first 3 rows in each group
iris.groupby("Class").head(3)

# get the last 3 rows in each group
iris.groupby("Class").tail(3)

# get max of group values
iris.groupby("Class").max()

# get min of group values
iris.groupby("Class").min()

# There does not seem to be a range function to see the range of values so I am going to calculate these ranges here.
# by taking the differences between the mimimum and the maximum values

iris_ranges = iris_grouped.max() - iris_grouped.min()
print(iris_ranges)

# sorting the range of values in ascending order, first by petal lengths, then petal widths and then by sepal lengths.
iris_ranges.sort_values(["Petal_Length","Petal_Width","Sepal_Length"])

# get mean of group values
iris.groupby("Class").mean()

# get median of group values
iris.groupby("Class").median()

print(iris_grouped.count())

print(iris_grouped.mean())

# Can look at the summary statistics for each class of Iris in the data set.
# I transposed the results to make it easier to read.
print(iris_grouped.describe())
print(iris_grouped.describe().T)


# Using the mean function to see the average measurements by species.
iris_means =iris_grouped.mean()
iris_means

iris_grouped.median()

# Now instead of looking at the calculations manually I will try adding a column that shows the differences in means between the three species.
# Having used groupby to the get the summary statistics by species, I will add a column to the DataFrame to calculate the differences in means.

# use groupby with "Class" variable and then get the mean of each class for each measurement variable.

# create a dataframe from grouping the iris dataframe by class and calculating the means for each class
# Transpose the rows and columns
means = iris.groupby("Class").mean().T
# only getting the columns up to Iris-versicolor to match Table II in Fisher's paper
means.loc[:,'Class':'Iris-versicolor'] 

# Instead of doing it for two species, I will do it for all the three species. 

# add a new column for the difference in means between the Versicolor and Setosa species
# I have changed the difference in means to show the absolute differences in means
means['diff (Versicolor - Setosa)'] = abs(means['Iris-versicolor'] - means['Iris-setosa'])

# add a new column for the difference in means between the Versicolor and Virginica species
means['diff (Versicolor - Virginica)'] = abs(means['Iris-versicolor'] - means['Iris-virginica'])

# add a new column for the difference in means between the Versicolor and Virginica species
means['diff (Virginica - Setosa)'] = abs(means['Iris-virginica'] - means['Iris-setosa'])

means


# differences in average measurements between species

# Below I am plotting the boxplots for each of the four measurements against the iris species.

# get information on the boxplot in the seaborn package
# get_ipython().run_line_magic('pinfo', 'sns.boxplot')

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks", palette="pastel")

f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
# pass a panda series as the x and y parameters to the boxplot. 
# the series here are the columns containing the class and the petal and sepal length measurements.
# the sepal length column contains numerical data while the class column contains a categorical variable - the species of the iris flower.
# the hue_order provides the order plot the categorical variables in.
sns.boxplot(x="Class", y="Petal_Length",data=iris, ax = axes[0,0])
sns.boxplot(x="Class", y="Sepal_Length", data=iris, ax=axes[0,1])
sns.boxplot(x="Class", y="Petal_Width",hue = "Class",data=iris, ax=axes[1,0])
sns.boxplot(x="Class", y="Sepal_Width", data=iris, ax=axes[1,1])
# adding a title to the plot
f.suptitle("Boxplot of the Petal and Sepal measurements by Iris plant Species")

plt.show()

# The pandas describe function shows the minimum and maximum values for the various measurements.
# I can use these to calculate the range of values for each measurement.

iris_ranges = iris_grouped.max() - iris_grouped.min()
iris_ranges

# sorting the range of values in ascending order, first by petal lengths, then petal widths and then by sepal lengths.
iris_ranges.sort_values(["Petal_Length","Petal_Width","Sepal_Length"])

# The iris setosa has the smallest range of values for the petal lengths, petal widths and sepal lengths. However the sepal widths of the setosa have a wider range of values than the other two species. This corresponds to the boxplots above. 


iris_std = iris.groupby("Class").std().T
iris_std

# create a dataframe from grouping the iris dataframe by class and calculating the standard deviations for each class
iris_std = iris.groupby("Class").std().T

# add a new column for the difference in standard deviations between the Versicolor and Setosa species
iris_std['diff (Versicolor - Setosa)'] = abs(iris_std['Iris-versicolor'] - iris_std['Iris-setosa'])

# add a new column for the difference in standard deviations between the Versicolor and Virginica species
iris_std['diff (Versicolor - Virginica)'] = abs(iris_std['Iris-versicolor'] - iris_std['Iris-virginica'])

# add a new column for the difference in standard deviations between the Versicolor and Virginica species
iris_std['diff (Virginica - Setosa)'] = abs(iris_std['Iris-virginica'] - iris_std['Iris-setosa'])

# Now doing it for the standard deviations.
iris_std

f, axes = plt.subplots(1, 2, sharey=True, figsize=(10, 4))
sns.scatterplot(x="Petal_Length", y="Sepal_Length", hue = "Class",data=iris, ax=axes[0])
sns.scatterplot(x="Petal_Width", y="Sepal_Width", hue="Class", data=iris, ax=axes[1])
plt.show()

