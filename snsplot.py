# here I will do some plotting using the seaborn library

# 1. IMPORT PYTHON LIBRARIES

print("First importing the python libraries")
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns


csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']

iris =  pd.read_csv(csv_url, names = col_names)
print(iris.head(10))


# instead use the seaborn library to do a scatter plot and colour code each iris plant species/class
# seaborn has been imported as sns above

#set a white grid for the figure
sns.set(style ="whitegrid")
# using a facet grid and setting hue = Class which means the points will be coloured on the plot according to their Class/species.
sns.relplot(x="Sepal_Length",y="Sepal_Width", data = iris, hue ="Class")
plt.show()


sns.relplot(x="Petal_Length",y="Petal_Width", data = iris, hue ="Class")
plt.show()