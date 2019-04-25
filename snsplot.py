# Angela Carpenter
# I am usins the Seaborn python package here for plotting and visualising the Iris data set.
#

# First I need to import the data as in the main python script.
# note that the iris data set actually comes loaded with the seaborn package which I will use here as it is quicker to load.

# 1. IMPORT PYTHON LIBRARIES

print("First importing the python libraries")
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns


csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

iris =  pd.read_csv(csv_url, names = col_names)
print(iris.head(10))

iris2 = sns.load_dataset("iris")
# sns.relplot(x="Petal_Length",y="Petal_Width", col ="species", hue = "species", data = iris2)





# #set a white grid for the figure
# sns.set(style ="whitegrid")
# # using a facet grid and setting hue = Class which means the points will be coloured on the plot according to their Class/species.
# sns.relplot(x="Sepal_Length",y="Sepal_Width", data = iris, hue ="Class")
# plt.show()

import seaborn as sns
# apply the default default seaborn theme, scaling, and color palette.
sns.set()
# draw a faceted scatter plot with multiple semantic variables, two numeric and one categorical.
# The numeric variables determine the position of each point on the axes
# sns.relplot(x="petal_length",y="petal_width", data = iris2, hue ="species")
# plt.show()

# sns.relplot(x="sepal_length",y="sepal_width", data = iris2, hue ="species")
# plt.show()


"""
the  above plots are made with “figure-level” functions. 
These are optimized for exploratory analysis because they set up the matplotlib figure containing the plot(s) and 
make it easy to spread out the visualization across multiple axes. 
They also handle some tricky business like putting the legend outside the axes. To do these things, they use a seaborn FacetGrid.

Each different figure-level plot kind combines a particular “axes-level” function with the FacetGrid object. 
For example, the scatter plots are drawn using the scatterplot() function, and the bar plots are drawn using the barplot() function.
These functions are called “axes-level” because they draw onto a single matplotlib axes and don’t otherwise affect the rest of
the figure.

The upshot is that the figure-level function needs to control the figure it lives in, 
while axes-level functions can be combined into a more complex matplotlib figure with other axes 
that may or may not have seaborn plots on them:
"""

import matplotlib.pyplot as plt
f, axes = plt.subplots(1, 2, sharey=True, figsize=(6, 4))
sns.scatterplot(x="sepal_length",y="sepal_width", data = iris2, ax=axes[0], hue ="species")

sns.scatterplot(x="petal_length",y="petal_width", data = iris2, ax=axes[1], hue ="species")
plt.show()

sns.boxplot(x="species",y="petal_length", data = iris2)
plt.show()


f, axes = plt.subplots(1, 2, sharey=True, figsize=(6, 4))
sns.boxplot(x="species",y="sepal_width", data = iris2, ax=axes[0])
sns.boxplot(x="species",y="petal_width", data = iris2, ax=axes[1])

plt.show()


sns.boxplot(x="Class", y="Petal_Length",data=iris, ax = axes[0,0])
sns.boxplot(x="Class", y="Sepal_Length", data=iris, ax=axes[0,1])
sns.boxplot(x="Class", y="Petal_Width",data=iris, ax=axes[1,0])
sns.boxplot(x="Class", y="Sepal_Width", data=iris, ax=axes[1,1])

plt.show()