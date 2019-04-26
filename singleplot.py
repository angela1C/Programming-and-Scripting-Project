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

sns.set(style="ticks",  hue = "Class")
sns.pairplot(iris)
plt.show()
