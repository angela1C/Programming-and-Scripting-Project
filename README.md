# pands-project
Project 2019 for Programming and Scripting Module

The instructions for the project are to be found on the [Programming and Scripting Project 2019](https://github.com/ianmcloughlin/project-pands/raw/master/project.pd)

## Problem Statement

The project concerns the well-known Fisher's Iris data set. 
The project entails researching the data set, and then writing documentation and code in the Python programming language based on that research.

## 1. Background information about the dataset

According to the [UCI Iris Data Set Information](https://archive.ics.uci.edu/ml/datasets/iris), Fisher's iris dataset is possibly the best known database to be found in the pattern recognition literature and Fisher's paper is frequently referenced to this day. The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other two which are not linearly separable from each other.

>This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. (See Duda & Hart, for example.) The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. 

[Wikipedia - Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher)
>Sir Ronald Aylmer Fisher FRS[3] (17 February 1890 – 29 July 1962) was a British statistician and geneticist. For his work in statistics, he has been described as "a genius who almost single-handedly created the foundations for modern statistical science"[4] and "the single most important figure in 20th century statistics".

Fisher developed ANOVA, the Analysis of Variance. He used it to analyse data from crop experiments. He also developed the Fisher Distribution. He pioneered the principles of the design of experiments and the statistics of small samples and the analysis of real data.

In 1936 Fisher introduced the Iris flower data set as an example of discriminant analysis. Linear discriminant analysis (LDA) is a generalization of Fisher's linear discriminant, a method used in statistics, pattern recognition and machine learning to find a linear combination of features that characterizes or separates two or more classes of objects or events. The resulting combination may be used as a linear classifier.

The Iris dataset is a multivariate dataset. 
[Wikipedia - Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.




## 2. References
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

- [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)

- [UCI Machine Learning Repository: Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)

- [Python, R and Linux Tips](https://cmdlinetips.com/category/python/)

- [Wikipedia - Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)

- [Wikipedia - Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher)

- Python for Data Analysis - Wes McKinney
Data Wrangling with Pandas, NumPy and IPython


## 3. Download the dataset and investigate it using Python code

https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

The dataset at the UCI Machine Learning repository doesnt have headers attached. However they are to be found in section 7 of the [iris.names](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names)

 Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica

`pandas` has several functions for reading tabular data as a `DataFrame` object. 
`read_csv` loads delimited data from a file, URL or file-like object using a comma as the defauly delimiter.

The Iris data set is located at the URL and it can be read in directly from this url.
Alternatively it can be saved locally and read if from there.

Note to myself - I initially read in the csv file from the URL, however I am now having a problem with the website  as the certificate has expired a day ago.
I will work with the local file for now until I figure out what I need to do or if the certificate is renewed.

`pandas.read_csv` performs type inference because the column data types are not part of the data format. You do not need to specify the data format of each column.

In `terminal` I can look at the csv file using the `cat` command which prints the raw contents of the file to the screen. or the `head` command whoch prints the first 10 rows to the screen. The file has 4 numerical columns and 1 descriptive string column. 

The raw csv file does not contain any headers. However there is a separate file on the website that provides the details under 'attribute_information' and these can be added to the dataframe. 
I set `header = None` on first reading in the file and then specified the names to use as column names using `names = []`.
Instead of settign `header=None` and then adding column names, you could add the names to the `panda.read_csv()` function.

When the data is imported into python using pandas.read_csv function, an index is added by default. This is the far left column which ranges from 0 to 150. 

Having added column names, the dataframe can be saved to a csv file using the `to_csv` method which writes the data out to a comma separated file.


## Exploring the dataset

using `.head()` to look at the observations at the top of the dataset and `.tail()` to lool at the observations at the end of the dataset

The far left (without a column name) contains the index of the dataframe which in this case is a range from 0 to 150 in steps of 1.

The data can be checked for any missing values. In pandas objects, the floating point `NaN` for Not a Number is used to represent missing values.



## 4. Summarise the dataset - high level statistics

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

## 5. Summary write up of the investigations.

## 6. Clearly document how to run the Python code to investigate the dataset, and what the code does.

## 6. Include supporting tables and graphics

### https://guides.github.com/features/mastering-markdown/
