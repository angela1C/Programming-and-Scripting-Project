# pands-project
Project 2019 for Programming and Scripting Module

The instructions for the project are to be found on the [Programming and Scripting Project 2019](https://github.com/ianmcloughlin/project-pands/raw/master/project.pd)

## Problem Statement

The project concerns the well-known Fisher's Iris data set. 
The project entails researching the data set, and then writing documentation and code in the Python programming language based on that research.

## 1. Background information about the dataset

The Iris Data Set is available from the UCI Machine Learning Repository. It is a multivariate data set with a default machine learning task of classification. The attribute types are real numbers. It has 150 instances with 5 attributes. The data set was donated in 1988 by Michael Marshall but the data set was created by R.A. Fisher.
http://archive.ics.uci.edu/ml/datasets/Iris

[UCI Iris Data Set Information](https://archive.ics.uci.edu/ml/datasets/iris) states that Fisher's iris dataset is possibly the best known database to be found in the pattern recognition literature and Fisher's paper is frequently referenced to this day. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other two which are not linearly separable from each other.

>This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. 

> The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. 

The predicted attribute of the data set is the class of iris plant. 

[Wikipedia - Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher)
>Sir Ronald Aylmer Fisher FRS[3] (17 February 1890 – 29 July 1962) was a British statistician and geneticist. For his work in statistics, he has been described as "a genius who almost single-handedly created the foundations for modern statistical science"[4] and "the single most important figure in 20th century statistics".

Fisher developed ANOVA, the Analysis of Variance. He used it to analyse data from crop experiments. He also developed the Fisher Distribution. He pioneered the principles of the design of experiments and the statistics of small samples and the analysis of real data.

In 1936 Fisher introduced the Iris flower data set as an example of discriminant analysis. Linear discriminant analysis (LDA) is a generalization of Fisher's linear discriminant, a method used in statistics, pattern recognition and machine learning to find a linear combination of features that characterizes or separates two or more classes of objects or events. The resulting combination may be used as a linear classifier.

[Wikipedia - Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
The Iris dataset is a multivariate dataset consisting of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.




## 2. References

- [Python Data Analysis Library](https://pandas.pydata.org)

- [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)

- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

- [UCI Machine Learning Repository: Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)

- [Python, R and Linux Tips](https://cmdlinetips.com/category/python/)

- [Wikipedia - Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)

- [Wikipedia - Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher)

- [cmdlinetips.com](https://cmdlinetips.com/2018/01/7-tips-to-read-a-csv-file-as-pandas-data-frame/)

- [Iris Dataset - Exploratory Data Analysis](https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis)

- Python for Data Analysis - Wes McKinney
Data Wrangling with Pandas, NumPy and IPython

For this project, I am mainly working through the pandas documentation at - [https://pandas.pydata.org](https://pandas.pydata.org).
I am also reading through the `Python for Data Analysis` book by Wes McKinney who is the creator of the Python Pandas project.

## 3. Download the dataset and investigate it using Python code

The Iris Data Set is available from the UCI Machine Learning Repository. According to the Data Set listing, it is a multivariate data set and the default machine learning task is classification. The attribute types are real numbers. It has 150 instances with 5 attributes. The data set was donated in 1988 by Michael Marshall but the data set was created by R.A. Fisher.
http://archive.ics.uci.edu/ml/datasets/Iris

https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

The actual data set itself at the UCI Machine Learning repository does not have the attribute information included in the csv file. However this information can be found under the section [Iris Data Set: Attribute Information](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names)

 Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica

The python `pandas` library is designed for working with tabular or heteogenous data, i.e. data that is in a tabular format containing an ordered collection of columns and each column can have a different value type.  Python `pandas` is therefore ideal for exploring a dataset such as Iris which has 4 numerical columns and 1 string column. 

`pandas` has several functions for reading tabular data as a `DataFrame` object. 
`read_csv` loads delimited data from a file, URL or file-like object using a comma as the default delimiter.

The Iris data set can be read in directly from the url or alternatively it can be saved locally and read in from there. I haved saved it into this project's repository for convenience. 

`pandas.read_csv` performs type inference because the column data types are not part of the data format. Therefore you do not need to specify the data format of each column.

A `DataFrame` represents a rectangular table of data containing an ordered collection of columns and each column can have a different value type.
A `DataFrame` has both a row and a column index.
When the data is imported into python using `pandas.read_csv` function, an index is added to the DataFrame by default. This is a range of numbers from 0 to 150 with the last observation being at index 149.

In `terminal` I can look at the csv file using the `cat` command which prints the raw contents of the file to the screen. or the `head` command whoch prints the first 10 rows to the screen. The file has 4 numerical columns and 1 descriptive string column. 

The raw csv file does not contain any headers. However this information is available under 'attribute_information'. I can add the column names to the DataFrame. 
I set `header = None` on first reading in the file and then specified the names to use as column names using `names = []`.
Instead of setting `header=None` and then adding column names, you could add the names to the `panda.read_csv()` function.


Having added column names, the DataFrame can be saved to a csv file using the `to_csv` method which writes the data out to a comma separated file.


## Exploring the dataset

### Viewing the dataset.

Can use  `.head()` to look at the observations at the top of the dataset and `.tail()` to lool at the observations at the end of the dataset

The far left (without a column name) contains the index of the dataframe which in this case is a range from 0 to 150 in steps of 1.

The `pandas.index()` can be used to look at the index of the dataframe. and `pandas.columns()` to look at the columns of the dataset.
When the data set is read in using, an index is automatically assigned starting at 0, stopping and 150.

The columns on the dataset will contain the column names I used in reading in the csv file.
'Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width','Species'

The data set has 150 rows and 5 columns. 
`.shape()`



### data cleaning and preparation

(Chapter 7 Python for Data Analysis)
The data can be checked for any missing values. In pandas objects, the floating point `NaN` for Not a Number is used to represent missing values.

Missing data is a common occurence in data analysis. By default the descriptive statistics on pandas objects exclude missing value.

In R programming language, missing data is referenced as NA for Not Available. NA data in statisics is usually data that doesn't exist or was not observed for some reason or other.

The Iris dataset does not have any missing values. `pandas.isnull` can be used to check for missing data. This returns a True or False for each observation. Boolean values are coerced to 1 for True and 0 for False so the `sum` function can be used to count the number of True values.

`pandas.notnull()` is th opposite.

## 4. Summarise the dataset - high level statistics

`pandas` objects have a set of common mathematical and statistical methods. Most of these methods
produce a single value such as the mean or the max or standard deviation
Multiple summary statistics can be obtained in one go using pandas.descibe().

### Descriptive statistics
A quick statistic summary of the data using `.describe()`
 
       Sepal_Length  Sepal_Width  Petal_length  Petal_Width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

### Correlation and Covariance
The correlation and covariance statistics are computed from  pairs of arguments.
The correlation of the measurements can be got using the `corr` method on the DataFrame while the covariance can be obtained using the `cov` method on the DataFrame. 

The correlation matrix is as follows.

              Sepal_Length  Sepal_Width  Petal_length  Petal_Width
Sepal_Length      1.000000    -0.109369      0.871754     0.817954
Sepal_Width      -0.109369     1.000000     -0.420516    -0.356544
Petal_length      0.871754    -0.420516      1.000000     0.962757
Petal_Width       0.817954    -0.356544      0.962757     1.000000

The covariance matrix is as follows.

              Sepal_Length  Sepal_Width  Petal_length  Petal_Width
Sepal_Length      0.685694    -0.039268      1.273682     0.516904
Sepal_Width      -0.039268     0.188004     -0.321713    -0.117981
Petal_length      1.273682    -0.321713      3.113179     1.296387
Petal_Width       0.516904    -0.117981      1.296387     0.582414

The `DataFrame` method `duplicated` can be used to see if any of the rows in the data set are duplicates of another row. I am just using it to see if there are any individual observations that have the exact same measurements as another observation.

There are three observations which appear to have the same measurements as other observations in the dataset as follows. It is possible that these values may have been rounded at some stage when or since the dataset was put together in 1936.

     Sepal_Length  Sepal_Width  Petal_length  Petal_Width         Species
34            4.9          3.1           1.5          0.1     Iris-setosa
37            4.9          3.1           1.5          0.1     Iris-setosa
142           5.8          2.7           5.1          1.9  Iris-virginica

## Visualising the Iris data set.

The `matplotlib` package can be used to create a graph or plot of the Iris Data set. The `pandas` library also has some built in methods to create visualisations from DataFrame and Series objects.
`Seaborn` is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures.
`Seaborn` has dataset-oriented plotting functions that operate on dataframes such as iris.

Can use it to draw a facetted scatter plot. The iris measurement variables determine the position of each point on the axes.

A `scatter plot` can be used to visualize relationships between numerical variables such as the petal measurements and the sepal measurements in the iris data set.  A `catplot()` can capture the relationship between a numeric variable and one (or more) categorical variables, such as the class or species of iris plant. 

The [Visualising dataset structure](http://seaborn.pydata.org/introduction.html#visualizing-dataset-structure) section of the `Seaborn` documentation actually illustrates using the iris data set!




# The function relplot() is used to visualize many different statistical relationships.
https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#visualization
https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#visualization
https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
https://seaborn.pydata.org/introduction.html#introduction

## 5. Summary write up of the investigations.

## 6. Clearly document how to run the Python code to investigate the dataset, and what the code does.

## 6. Include supporting tables and graphics

### https://guides.github.com/features/mastering-markdown/


## How to run the code


Make sure you have Python 3 installed. If not go to https://www.python.org/downloads/ and follow the instructions.

To run each python program, first navigate to the folder downloaded from this repository.

At the command line enter python <program_name> for example: $ python isi_expl.py

The python program can also be run inside the environment of an iPython session using the `%run` command.
 `% run iris_expl.py`

