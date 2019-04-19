# Project Iris
# This is from the Jupyter notebook I have been working on which I have copied in here.
# I am deleting out background to the data set as this is in the README file. 
# I am deleting out any of my analysis as this is going into the readme file also.
# I am currently looking at the groupby statistics at line 162.
# anything below that is from my jupyter notebook that I was working on and has yet to be edited!
#


# In order to use python libraries that are not part of the standard python library, they first need to be imported.
# Here I import the pandas library, the matplotlib pyplot library and the seaborn library.
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns

# help can be obtained using the python help function
# help(pd) or help(pd.DataFrame.describe())


# LOADING / READING IN THE IRIS DATA SET

# Create a variable `csv_url` and pass to it the url where the data set is available 
# at 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'. 
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# I have also saved the csv file to the folder or repository and can read it in from there in case for some reason the url is not available.

# As the data does not have any column names, I can specify header = None to avoid reading the first row of data as a header or column name
# Create a list of column names `col_names` using the iris attribute information available at the UCI machine learning repository.
# When the column names are passed in as a parameter to read_csv, then it is not necessary to include 'header = none'

# using the iris data set attribute information as the column names, create a list of column names to use
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

iris =  pd.read_csv(csv_url, names = col_names)
# iris = pd.read_csv('iris_data.csv', names = col_names)

# using the pandas DataFrame method head to return the first rows of the DataFrame and check that the file was correctly loaded
print(iris.head(10))
# using the pandas DataFrame method tail to return the last rows of the DataFrame and check that the file was correctly loaded
print(iris.tail(10))


# EXPLORING / INVESTIGATING THE IRIS DATA SET

## ATTRIBUTES OF THE IRIS DATA FRAME
# First looking at the attributes of the iris DataFrame created from importing the iris data set above.

# Get the column labels of the iris DataFrame.
print(iris.columns)

# the number of axes / array dimensions of the iris DataFrame
print(iris.ndim)
# Look at the shape of the iris DataFrame - this shows the number of rows and columns
print(iris.shape)
# the number of elements in the iris object.
print(iris.size)

# The DataFrame has an index which was automatically assigned when the DataFrame was created
# on reading in the csv file. The index is a range from 0 to 150
print(iris.index)

# the dtypes (data types) of the iris DataFrame
print(iris.dtypes)

# Return the ftypes (indication of sparse/dense and dtype) in the iris DataFrame.
print(iris.ftypes)

# return a a list representing the axes of the iris DataFrame.
print(iris.axes)

# **************** **************** **************** **************** ****************

# USING DATAFRAME METHODS TO EXPLORE THE IRIS DATAFRAME

# Look at the first ten observations in the DataFrame
print(iris.head(10))

# Look at the last ten observations in the DataFrame
print(iris.tail(10))

# It is possible to check for missing values in the DataFrame using the panda's `isnull()` method.
# This shows that there are no missing values which is as expected for this well known data set consisting of 150 instances of 5 attributes.

print(iris.isnull().sum())

# look at the summary statistics of the DataFrame
print(iris.describe())

# Print a concise summary of the iris DataFrame.
print(iris.info())

# Count non-NA cells for each column or row.
print(iris.count())

# It is possible to check for missing values in the DataFrame using the panda's isnull() and isna() methods.
# There should be no missing values in this DataFrame as there are no missing values in the csv file from which it is created. 

# Detect missing values in the DataFrame. Sum the values instead of printing the boolean values as True = 1.
iris.isna().sum()
iris.isnull().sum()
iris.notnull().sum()
iris.notna().sum()
iris.count()

# Make a histogram of the DataFrame. A `histogram` is a representation of the distribution of data.
# This function calls :meth:`matplotlib.pyplot.hist`, on each series in the DataFrame, resulting in one histogram per column.
# A histogram will be produced for each of the four numeric columns in the iris data set.
# The number of bins can be specified. For now I go with the default settings.
    
iris.hist()

# count distinct observations.
iris.nunique()

# Using the `unique()` method to show how many different class or species of Iris flower is in the data set.

iris['Class'].unique()

# GROUP BY 

# Using groupby functions to look at statistics at the class / species level
iris_grouped = iris.groupby("Class")

# Compute count of group, excluding missing values.
iris.groupby("Class").count()

# Groupby Class and return the mean of the remaining columns in each group.
iris.groupby('Class').mean()

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

# get mean of group values
iris.groupby("Class").mean()

# get median of group values
iris.groupby("Class").median()

print(iris_grouped.count())

print(iris_grouped.mean())

# now looking at the summary statistics for each class of Iris in the data set.
# I transposed the results to make it easier to read.
print(iris_grouped.describe())
iris_grouped.describe().T

# THIS IS WHERE I AM!
# 

# Using the mean function to see the average measurements by species.
iris_means =iris_grouped.mean()
iris_means

iris_grouped.median()

# Now instead of looking at the calculations manually I will try adding a column that shows the differences in means between the three species.
# Having used groupby to the get the summary statistics by species, I will add a column to the DataFrame to calculate the differences in means.
# 
# In the original paper by R.A. Fisher,  'THE USE OF MULTIPLE MEASUREMENTS IN TAXONOMIC PROBLEMS' which is available online by The Annals of Human Genetics, Fisher shows a table of the observed means and differences in the means between the iris versicolor and the iris setosa in centimetres.
# This is Table II *Observed means for two species and their difference (cm.)*.
# This table displays the means for each of the 4 measurements for the Iris-Versicolor and Iris-Setosa species. It also shows the differences between the Versicolor means and the Setosa means for each of the 4 measurement variables.
# 
# This table illustrates the observed means and their differences in centimetres. He shows that the length of the Versicolor is on average  2.8 cm's approximately greater than that of the setosa while the sepal length and petal width between these two species vary by approximately one centimetre at 0.93 cm and 1.08 centimetres respectively. On the other hand, the sepal width of the setosa is 0.66 cm larger than that of the versicolor.
# 
# 
# I will try and get the same information in Table II of Fisher's paper.

# Fisher's table 2 shows the difference in means for the setosa and versicolor species
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


# ### differences in average measurements between species
# ####  Sepal measurements
# The virginica has the highest average Sepal Length while the setosa has the smallest average sepal length.
# The difference in average sepal lengths is therefore greatest between these two species.
# 
# The setosa has the highest average sepal width and that of the versicolor is the smallest, but the differences are not as marked as the differences in sepal lengths between virginica and setosa.
# 
# #### Petal measurements
# The virginica has a much longer average petal length than the setosa.
# It would be better to visualise them.

# Fisher's table II looked at the differences between the Iris-versicolor and the Iris-setosa.In his paper he mentions that these two species were found growing together in the same colony.
# The sample of the third species - the Iris Virginica - differs from the setosa and the versicolor in that the virginica sample was from a different natural colony to the other two samples. 
# The difference of means table above shows the greatest difference in average measurements between the petal lengths, sepal lengths and petal widths of the iris setosa and the iris virginica. The averages sizes of the sepal widths varied the most between the versicolor and the setosa but not by as much.

# ### Visualising the differences
# A boxplot would be a suitable graph to show the differences between the distribution of the measurements of the iris data set. 
# A boxplot is used to show distributions with respect to categories and allow  visual comparison between the variables or across levels of a categorical variable. The box shows the quartiles of the data set while the whiskers extend to show the rest of the distribution. It also shows the outliers.
# The boxplot is suitable for comparing the distribution of the iris petal or sepal measurements and grouping them by the class or species type.
# Below I am plotting the boxplots for each of the four measurements against the iris species.

# get information on the boxplot in the seaborn package
get_ipython().run_line_magic('pinfo', 'sns.boxplot')

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


# The boxplots show that the iris setosa has a much smaller range of petal size than the other two species. There is no overlap at all between the petal lengths of the setosa and the other two species, while there is a small overlap between the versicolor and the virginica. 

# I now want to look at the range of the variables. 
# The pandas describe function shows the minimum and maximum values for the various measurements.
# I can use these to calculate the range of values for each measurement.

iris_ranges = iris_grouped.max() - iris_grouped.min()
iris_ranges

# sorting the range of values in ascending order, first by petal lengths, then petal widths and then by sepal lengths.
iris_ranges.sort_values(["Petal_Length","Petal_Width","Sepal_Length"])

# The iris setosa has the smallest range of values for the petal lengths, petal widths and sepal lengths. However the sepal widths of the setosa have a wider range of values than the other two species. This corresponds to the boxplots above. 

# ### where I am!
# I am currently looking at some plots. Have just looked at the differences between the boxplots for sepal and petal measurements between the species of iris plant.
# 
# I will look at the correlation between the variables.
# I am copying some of the comments and explanations back and forth between by readme file in Visual Studio for the project submission.
# The differences between Petal lengths of the virginica and setosa is quite abvious in the box plot, as is the difference between the petal lengths.
# 
# The boxplot also show the outliers.

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


# #### Filtering the data set
# Looking at some other ways to subset and filter the iris data set

## Here I am subsetting the data to meet a given criteria su
# http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-with-isin
values =  {'Class': ['Iris-versicolor', 'Iris-virginica']}
row_mask = iris.isin(values).any(1)
iris[row_mask].head()

iris_grouped.mean()

# select from the iris DataFrame only the rows where the Class equals the string "Iris-setosa"
iris_setosa = iris[iris['Class'] == "Iris-setosa"]
iris_setosa.head()

# Here I am subsetting the data to meet a given criteria su
# http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-with-isin
values =  {'Class': ['Iris-versicolor', 'Iris-virginica']}
row_mask = iris.isin(values).any(1)
iris[row_mask].head()

