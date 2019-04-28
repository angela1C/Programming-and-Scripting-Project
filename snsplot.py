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

# I want to save my plots to a pdf file instead of to the screen
# https://stackoverflow.com/a/11329151

from matplotlib.backends.backend_pdf import PdfPages
pp= PdfPages("iris_plots.pdf")

csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

iris =  pd.read_csv(csv_url, names = col_names)
print(iris.head(10))

iris2 = sns.load_dataset("iris")
# snsplot1 = sns.relplot(x="Petal_Length",y="Petal_Width", col ="species", hue = "species", data = iris2)

# set a white grid for the figure
# sns.set(style ="whitegrid")
# # using a facet grid and setting hue = Class which means the points will be coloured on the plot according to their Class/species.
# sns.relplot(x="Sepal_Length",y="Sepal_Width", data = iris, hue ="Class")
# # plt.show()
# pp.savefig(snsplot)



# apply the default default seaborn theme, scaling, and color palette.
sns.set()
# draw a faceted scatter plot with multiple semantic variables, two numeric and one categorical.
# The numeric variables determine the position of each point on the axes
# sns.relplot(x="petal_length",y="petal_width", data = iris2, hue ="species")
# plt.show()

# sns.relplot(x="sepal_length",y="sepal_width", data = iris2, hue ="species")
# plt.show()


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


# sns.boxplot(x="Class", y="Petal_Length",data=iris, ax = axes[0,0])
# sns.boxplot(x="Class", y="Sepal_Length", data=iris, ax=axes[0,1])
# sns.boxplot(x="Class", y="Petal_Width",data=iris, ax=axes[1,0])
# sns.boxplot(x="Class", y="Sepal_Width", data=iris, ax=axes[1,1])

# plt.show()

g = sns.pairplot(iris, hue="Class")

plt.show()