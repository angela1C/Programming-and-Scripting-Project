# I used this script for running and checking individual plots.
# 
# 
# 1. IMPORT PYTHON LIBRARIES

print("First importing the python libraries")
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns


csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

iris =  pd.read_csv(csv_url, names = col_names)
print(iris.head(10))




# print("Histogram of the distribution of the iris data. Make sure to close the plot to continue. ") 
# iris.diff().hist(alpha=0.8, bins=30, figsize=(12,8))
# plt.show()
# iris.drop(['Class'], axis=1).diff().hist()
# # plt.figure()
# # iris.diff().hist(color='k', alpha=0.5, bins=20)
# plt.show()


# sns.set(style="ticks", palette="pastel")
# f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))
# sns.boxplot(x="Class", y="Petal_Length",data=iris, ax = axes[0,0])
# sns.boxplot(x="Class", y="Sepal_Length", data=iris, ax=axes[0,1])
# sns.boxplot(x="Class", y="Petal_Width",hue = "Class",data=iris, ax=axes[1,0])
# sns.boxplot(x="Class", y="Sepal_Width", data=iris, ax=axes[1,1])
# # adding a title to the plot
# f.suptitle("Boxplot of the Petal and Sepal measurements by Iris plant Species")
# plt.show()

# sns.set(style="ticks", palette="deep")
# f, axes = plt.subplots(2, 2, sharey=False, figsize=(12, 8))

# sns.scatterplot(x="Petal_Length", y="Petal_Width", hue = "Class",data=iris, ax=axes[0,0])
# sns.scatterplot(x="Sepal_Length", y="Sepal_Width", hue="Class", data=iris, ax=axes[0,1])
# sns.scatterplot(x="Petal_Length", y="Sepal_Length", hue = "Class",data=iris, ax=axes[1,0])
# sns.scatterplot(x="Petal_Width", y="Sepal_Width", hue="Class", data=iris, ax=axes[1,1])
# f.suptitle("Scatterplots of the Petal and Sepal measurements by Iris plant Species")
# plt.show()

### ### ### ###
# http://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn.pairplot
"""
pairplot is used to plot pairwise relationships in a dataset.
It creates a grid of Axes where each variable in the dataset will by shared in the y-axis across a single row 
and in the x-axis across a single column. The diagonal Axes are treated differently, drawing a plot to show the univariate distribution of the data for the variable in that column.
A plot showing the univariate distribution for the variable in that column is drawn along the diagonal.
"""
# sns.set(style="ticks", color_codes=True)
# sns.pairplot(iris)
# plt.show()

# sns.set(style="ticks", hue = "Class")
# sns.pairplot(iris)
# plt.show()

# sns.distplot(iris)
# plt.show()

# DataFrame.hist() plots the histograms of the columns on multiple subplots:
# print("Histogram of the distribution of the iris data. Make sure to close the plot to continue. ") 
# iris.hist(alpha=0.8, bins=30, figsize=(12,8))

"""
# PAIRPLOT
# a this function will create a grid of Axes such that each variable in the dataframe will by shared in the y-axis across a single row and
# in the x-axis across a single column. 
# the diagonals show  a plot to show the univariate distribution of the data
# for the variable in that column.
sns.set(style="ticks")
sns.pairplot(iris, hue="Class")
plt.suptitle('iris plot')
# plt.show()
plt.savefig("irisplot.png")


# BOXPLOT 
iris.plot.box(figsize=(6,4))
plt.suptitle("Boxplots of the Iris petal and sepal measurements")
# plt.show()
# I am going to save the resulting plot to a file rather than printing it here
# to print it to screen just uncomment the code in the line above:     plt.show()
plt.savefig("images/irisbox.png")


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
plt.show()
"""

# SCATTER PLOTS OF THE IRIS DATA SET

f, axes = plt.subplots(1, 2, sharey=True, figsize=(10, 4))
sns.scatterplot(x="Petal_Length", y="Sepal_Length", hue = "Class",data=iris, ax=axes[0])
sns.scatterplot(x="Petal_Width", y="Sepal_Width", hue="Class", data=iris, ax=axes[1])
f.suptitle("Scatterplots of the Iris petal and sepal measurements")
plt.show()

# DISTPLOT using Seaborn
# sns.distplot(iris, kde=False, rug=True)
# plt.savefig("IrisDistplot.png")
