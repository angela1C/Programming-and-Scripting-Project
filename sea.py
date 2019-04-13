# learning seaborn 
import matplotlib.pyplot as plt 

import seaborn as sns
sns.set()
tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", col="time",
            hue="smoker", style="smoker", size="size",
            data=tips)


plt.show()

# The Seaborn library gallery shows many examples of how to visualise the Iris data set!

# SCATTER PLOT MATRIX

# https://seaborn.pydata.org/examples/scatterplot_matrix.html
sns.set(style="ticks")

df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")

# SWARMPLOT
# https://seaborn.pydata.org/examples/scatterplot_categorical.html

sns.set(style="whitegrid", palette="muted")

# Load the example iris dataset
iris = sns.load_dataset("iris")

# "Melt" the dataset to "long-form" or "tidy" representation
iris = pd.melt(iris, "species", var_name="measurement")

# Draw a categorical scatterplot to show each observation
sns.swarmplot(x="measurement", y="value", hue="species",
              palette=["r", "c", "y"], data=iris)

