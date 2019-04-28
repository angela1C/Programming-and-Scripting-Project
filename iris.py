# iris.py
# Angela Carpenter
# This script contains my script for project 2019.

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
print(f"The iris DataFrame has {iris.ndim} dimensions")

# Look at the shape of the iris DataFrame as this shows the number of rows and columns in the table or matrix of data
# This will show how many rows (containing observations) and columns (containing features/variables)
print(f"The Iris data set consists of {iris.shape[0]} rows and {iris.shape[1]} columns corresponding to the rows and columns of the csv file.")

# the number of elements in the iris object.
print(f"There are {iris.size}  elements in total.")
# the number of elements in the iris object.
print(f"The iris DataFrame has {iris.size} elements in total.")

# The DataFrame has both a row and a column index which were automatically assigned when the DataFrame was created.
# Get the column labels of the iris DataFrame using  'pandas.DataFrame.columns'
print("The column labels of the iris DataFrame are: ", *iris.columns, sep = "   ")

# the row index 
print(f" The index of the DataFrame is: ", iris.index)
print("The index for the rows are ",*iris.index)
print("This index was automatically assigned when the DataFrame was created above.")

# the dtypes (data types) of the iris DataFrame
print(f"The data types of iris DataFrame are as follows:")
print(iris.dtypes)

# Return the ftypes (indication of sparse/dense and dtype) in the iris DataFrame.
print(iris.ftypes)

# pandas.DataFrame.axes return a a list representing the axes of the iris DataFrame which shows the row axis labels and the column axis labels in that order. This returns the same information as the index and columns attribute
print(iris.axes)
#print("The row axis labels of the iris DataFrame are  ", *iris.axes[0])
print("The row axis labels of the iris DataFrame is a range from ", *iris.axes[0][[0]], *iris.axes[0][[1]], *iris.axes[0][[2]],"..." , *iris.axes[0][[-3]],*iris.axes[0][[-2]], *iris.axes[0][[-1]] )
print("The column axis labels of the iris DataFrame are as follows:\n ",*iris.axes[1])

# Now using some of the DataFrame methods to explore the Iris DataFrame

# Look at the first ten observations in the DataFrame. 
print(iris.head(10))

# Look at the last ten observations in the DataFrame
print(iris.tail(10))

# It is possible to check for missing values in the DataFrame using the panda's `isnull()` method.
# This shows that there are no missing values which is as expected for this particular data set.
# Detect missing values in the DataFrame. Sum the values instead of printing the boolean values as True = 1.
print("The number of null or missing values in the iris dataframe for each column: ")
print(iris.isnull().sum())

# Print a concise summary of the iris DataFrame.
print(f"A concise summary of the iris DataFrame: \n")
iris.info()

# Count non-NA cells for each column or row.
print(f"\n The number of non-NA cells for each column or row are: \n {iris.count()}")

# Using the `unique()` method on the 'Class' column to show how many different class or species of Iris flower is in the data set.

iris['Class'].unique()
species_type =iris['Class'].unique()
print("The following are the three class or species types of iris in the data set \n",*species_type, sep = " ")

# count the number of distinct observations for each column 
iris.nunique()

# look at the summary statistics of the DataFrame
print("Here are some summary statistics for the iris DataFrame: \n ")
print(iris.describe())

####   ####   ####   ####   ####   ####

# VISUALISATIONS OF THE IRIS DATA SET

# Make a histogram of the DataFrame for each of the four numeric columns in the iris data set.
# The number of bins can be specified. 

# pandas DataFrame.hist() plots the histograms of the columns on multiple subplots:
print("Histogram of the distribution of the iris data. Make sure to close the plot to continue. ") 
# iris.hist(alpha=0.8, bins=30, figsize=(12,8))

iris.hist(alpha=0.8, bins=30, figsize=(12,8))
plt.suptitle("Histogram of the Iris petal and sepal measurements")
plt.savefig("images/IrisHistograms.png")

# Boxplot can be drawn using DataFrame.plot.box(), or DataFrame.boxplot() 
# This is used to visualize the distribution of values within each column.

iris.plot.box(figsize=(6,4))
plt.suptitle("Boxplots of the Iris petal and sepal measurements")
# plt.show()
# I am going to save the resulting plot to a file rather than printing it here
# to print it to screen just uncomment the code in the line above:     plt.show()
plt.savefig("images/irisbox.png")

# boxplot just showing the distribution of each measurement variable on its own is not very useful 
# next look at boxplots by Class or species of iris plant using 'seaborn' 

# SEABORN PLOTS
# The appearance of the plot can be changed by setting the figure aesthetics.
# set the theme. (The default theme is called darkgrid). Set the color palette.
sns.set(style="ticks", palette="pastel")

# plotting 4 plots on a 2 by 2 grid, do not want to share the y axis between plots. Setting the figure size 
f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
# pass a panda Series as the x and y parameters to the boxplot. 
# Using the Class column (categorical) and one of the sepal or petal measurements (numerical) for each subplot

# setting the hue = Class so that the points will be coloured on the plot according to their Class/species type.
sns.boxplot(x="Class", y="Sepal_Length", data=iris, ax=axes[0,1])
sns.boxplot(x="Class", y="Sepal_Width", data=iris, ax=axes[1,1])
sns.boxplot(x="Class", y="Petal_Length",data=iris, ax = axes[0,0])

sns.boxplot(x="Class", y="Petal_Width",hue = "Class",data=iris, ax=axes[1,0])

# adding a title to the plot
f.suptitle("Boxplot of the Petal and Sepal measurements by Iris plant Species")

plt.savefig("images/irisBoxbyClass.png")



# 4. EXPLORING IRIS DATA SET BY SPECIES
# There are many ways to filter the data


# subsetting the data to meet a given criteria using the isin operator and boolean masks. only selecting where class is iris-versicolor or Iris-virginica
values =  {'Class': ['Iris-versicolor', 'Iris-virginica']}
row_mask = iris.isin(values).any(1)
iris[row_mask].head()

# select from the iris DataFrame only the rows where the Class equals the string "Iris-setosa"
iris_setosa = iris[iris['Class'] == "Iris-setosa"]
# print(iris_setosa.head())

# Using boolean masks to subset the data to meet a given criteria.
values =  {'Class': ['Iris-versicolor', 'Iris-virginica']}
row_mask = iris.isin(values).any(1)
# print(iris[row_mask].head())


# GROUP BY 

print("using groupby to split the iris dataframe by Class of iris species")
# Using groupby functions to look at statistics at the class / species level
iris_grouped = iris.groupby("Class")

# Compute count of group, excluding missing values.
iris.groupby("Class").count()
print("The number of observations for each variable for each Iris species in the data set are as follows: \n \n",iris.groupby("Class").count())

# Groupby Class of Iris plant and return the mean of the remaining columns in each group.

print("The mean or average measurement for each group of Iris Species in the dataset is \n",iris.groupby('Class').mean())
iris.groupby('Class').mean()
# Group by Class of Iris plant and then return the first observations in each group
iris.groupby("Class").first()
print("the first observation in each Class of Iris plant in the Iris dataset are: \n  \n",iris.groupby("Class").first())

# Group by Class of Iris and then return the last observations in each group
print("the last observation in each Class of Iris plant in the Iris dataset are: \n  \n",iris.groupby("Class").last())
iris.groupby("Class").last()

# get the first 3 rows in each group 
iris.groupby("Class").head(3)
print("The first three rows for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").head(3))

# get the last 3 rows in each group
iris.groupby("Class").tail(3)
print("The last three rows for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").tail(3))

# get max of group values
iris.groupby("Class").max()
print("The maximum value for each measurement for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").max())

# get min of group values
iris.groupby("Class").min()
print("The minimum value for each measurement for each Class of Iris plant in the Iris dataset are: \n\n",iris.groupby("Class").min())

# There does not seem to be a range function to see the range of values so I am going to calculate these ranges here.
# by taking the differences between the mimimum and the maximum values

iris_ranges = iris_grouped.max() - iris_grouped.min()
print(iris_ranges)

# sorting the range of values in ascending order, first by petal lengths, then petal widths and then by sepal lengths.
iris_ranges.sort_values(["Petal_Length","Petal_Width","Sepal_Length"])

# these stats are available from the describe() summary function
# get mean of group values
iris.groupby("Class").mean()

# get median of group values
iris.groupby("Class").median()

print(iris_grouped.count())

print(iris_grouped.mean())

# Can look at the summary statistics for each class of Iris in the data set.
# I transposed the results to make it easier to read.
print(iris.groupby("Class").describe())
# print(iris_grouped.describe())
# print(iris_grouped.describe().T)

# PAIRWISE SCATTER PLOTS

# SCATTER PLOTS OF THE IRIS DATA SET

print(" Here is a pairplot scatter matrix")
sns.pairplot(iris, hue="Class")

plt.savefig("images/irispairplots.png")

## correlation matrix of the iris dataset

# First getting the correlation between pairs of the measurement variables across the dataset

print("correlation between pairs of measurement variables for the dataset \n")
print(iris.corr())

print("correlation between pairs of measurement variables for the dataset by Class of iris \n")
iris.groupby("Class").corr()