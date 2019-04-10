# using this script for plotting for now so not running the whole script all the time
# will move it all into one script for the project submission

# working from https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#basic-plotting-plot
import matplotlib.pyplot as plt
import pandas as pd

plt.close('all')
# Matplotlib is a plotting library for Python. It is not part of the standard library so first needs to be installed.

# reading in the csv with the column names from iris_expl.py 

iris = pd.read_csv('iris_data.csv')
## first creating an empty figure
print(iris.head())
print(iris.describe())

# plt.figure()
# iris.plot()
# plt.show()

# Plotting methods allow for a handful of plot styles other than the default line plot. 
# These methods can be provided as the kind keyword argument to plot().

# matplotlib

#Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms
# Seaborn is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures.
# iris.plot(kind = "hist")

# plt.show()
# iris['Sepal_Length'].plot.hist()

# import the seaborn library
import seaborn as sns  
# apply the default seaborn theme, scaling and color palette
# sns.set() 

# setting theme for all plots
sns.set(style="ticks", palette="muted")

f, axes = plt.subplots(1, 2, sharey=True, figsize=(10, 4))
sns.scatterplot(x="Petal_Length_cm", y="Sepal_Length_cm", hue = "Class",data=iris, ax=axes[0])
sns.scatterplot(x="Petal_Width_cm", y="Sepal_Width_cm", hue="Class", data=iris, ax=axes[1])
plt.show()

# sns.relplot(x='Sepal_Length_cm', y= 'Sepal_Width_cm', col = )

# draw a facetted scatter plot. The measurement variables determine the psition of each pooint on the axes.
# The function relplot() is used to visualize many different statistical relationships.
sns.relplot(x="Sepal_Length_cm", y="Sepal_Width_cm", col="Class",hue="Class",
            data=iris)

# The plot method on Series and DataFrame is just a simple wrapper around plt.plot()

plt.show()


# sns.catplot(x="Sepal_Length_cm", y="Sepal_Width_cm", hue="Class",
#             kind="violin", data=iris)

# plt.show()

# iris1 = sns.load_dataset("iris")
# sns.jointplot(x="sepal_length", y="petal_length", data=iris1)
# plt.show()
# print(iris1.head())

sns.pairplot(data=iris, hue="Class")
plt.show()



