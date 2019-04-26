# I am creating a script for plots again.


# 1. IMPORT PYTHON LIBRARIES

print("First importing the python libraries")
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns


csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

iris =  pd.read_csv(csv_url, names = col_names)
print(iris.head(10))

# a simple scatter plot
# plot sepal length on the x axis and sepal width on the y axis.
iris.plot(kind="scatter", x = 'Sepal_Length', y="Sepal_Width", c= "DarkBlue")
plt.show()

# note the axes does not start at the origin (0,0)

plt.show()
# a simple scatter plot
# plot petal length on the x axis and petal width on the y axis.
ax3 = iris.plot.scatter(x = 'Sepal_Length', y='Sepal_Width', c= 'Red')
plt.show()


# Histograms can be drawn by using the DataFrame.plot.hist() and Series.plot.hist() methods.
# A histogram can be stacked using stacked=True. Bin size can be changed using the bins keyword.
# DataFrame.hist() plots the histograms of the columns on multiple subplots:
# plt.figure()
# iris['Sepal_Length'].hist()
# plt.show()


# plt.figure()
# iris['Sepal_Length'].diff().hist()
# plt.show()

print("Histogram of the distribution of the iris data. Make sure to close the plot to continue. ") 
iris.hist(alpha=0.8, bins=30, figsize=(12,8))
plt.show()


# Make a histogram of the DataFrame for each of the four numeric columns in the iris data set.
# The number of bins can be specified. 

# DataFrame.hist() plots the histograms of the columns on multiple subplots:
print("Histogram of the distribution of the iris data. Make sure to close the plot to continue. ") 
iris.hist(alpha=0.8, bins=30, figsize=(12,8))
plt.show()

# Boxplot can be drawn using DataFrame.plot.box(), or DataFrame.boxplot() 
# This is used to visualize the distribution of values within each column.

print("Boxplot the distribution of the iris data. Make sure to close the plot to continue. ") 
iris.plot.box(figsize=(12,8))
plt.show()

# Now instead of using just pandas I am using the seaborn package to do some visualisations.
# get_ipython().run_line_magic('pinfo', 'sns.boxplot')

import seaborn as sns
import matplotlib.pyplot as plt


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
plt.show()
