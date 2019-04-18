# pands-project
Project 2019 for Programming and Scripting Module

This repository contains my submission for the class project for the Programming and Scripting Module at GMIT as part of the Higher Diploma in Computing and Data Analytics. 
The pdf file containing the problem set instructions is available by clicking on the following link.
- [Programming and Scripting Project 2019](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)  


## Problem Statement

The project concerns the well-known Fisher's Iris data set. 
The project entails researching the data set, and then writing documentation and code in the Python programming language based on that research.

The suggested task breakdown for this project (taken from the Project Instructions document) are as follows:
1. Research background information about the data set and write a summary about it.    
2. Keep a list of references you used in completing the project  
3. Download the data set and write some Python code to investigate it.  
4. Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set. A Python script will quickly do this for you.  
5. Write a summary of your investigations.
6. Include supporting tables and graphics as you deem necessary.

The project should contain a repository containing a README and a python script.
The readme should contain  a summary of the dataset and your investigations into it
Readme should list all references.
The project should be well organised and contain detailed explanations
The analysis will be well conceived and and examples of interesting analyses that others have pursued based on the data set will be discussed.
Note that the point of this project is to use Python. You may use any Python libraries that you wish, whether they have been discussed in class or not. You should not be thinking of using spreadsheet software like Excel to do your calculations




# My project plan

I will use a Task List as described on the GitHub Flavoured Markdown Syntax cheatsheet.

Project Task List


- [ ] Research Background information about the Iris data set
- [ ] List all the references used 
- [ ] Download the Iris data set  
- [ ] Investigate the Iris data set using python code
- [ ] Summarise the Iris data set - provide statistics such as means, minimum and maximum values
- [ ] Include tables and graphics
- [ ] Clearly document how to run the code used to investigate the Iris data set  
- [ ] Clearly document what the python code used actually does
- [ ] Look at examples of interesting analyses pursued by other people on the Iris data set 
- [ ] Refer to task list as a guideline
- [ ] Use headings as links, maybe create a table of contents

# Table of Contents

1. Background information about the Iris data set
2. Downlaod the Iris data set [link to loading data](#loading)


## 1. Background information about the dataset

Fisher's Iris data set is a famous database consisting of the measurements of parts of 150 iris flowers. It is available from the UCI Machine Learning Repository where it is listed as a multivariate data set with a default machine learning task of classification. The data set consists of 150 instances with 5 attributes. The data set was donated in 1988 by Michael Marshall but the data set was created by R.A. Fisher in 1936. 
http://archive.ics.uci.edu/ml/datasets/Iris.

The data set includes 50 plants each of three classes of iris plant, where each class is a different type or species of iris plant.
The three classes are Iris Setosa, Iris Versicolor and Iris Virginica. 
Four flower measurements are given for each observation in the data set, which are the lengths and widths of the petals and the sepals of the flowers in the sample.

According to the [UCI Iris Data Set Information](https://archive.ics.uci.edu/ml/datasets/iris), Fisher's iris dataset is possibly the best known database to be found in the pattern recognition literature and is still relevant today. One class is linearly separable from the other two classes, which are not linearly separable from each other. The predicted attribute of the data set is the class of iris plant to which each observation belongs. 

>This is perhaps the best known database to be found in the pattern recognition literature. Fisher's paper is a classic in the field and is referenced frequently to this day. 

Now a little bit about Fisher:

According to a wiki on wikipedia about him, [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher),
>Sir Ronald Aylmer Fisher FRS[3] (17 February 1890 – 29 July 1962) was a British statistician and geneticist. For his work in statistics, he has been described as "a genius who almost single-handedly created the foundations for modern statistical science"[4] and "the single most important figure in 20th century statistics".

Fisher also developed the ANOVA method (Analysis of Variance) which he used to analyse data from crop experiments. He also developed the Fisher Distribution. Fisher pioneered the principles of the design of experiments and the statistics of small samples and the analysis of real data.

In 1936 Fisher introduced the Iris flower data set as an example of discriminant analysis. Linear discriminant analysis (LDA) is a generalization of Fisher's linear discriminant, a method used in statistics, pattern recognition and machine learning to find a linear combination of features that characterizes or separates two or more classes of objects or events. The resulting combination may be used as a linear classifier.

Based on the combination of the four measurement features of the sample of plants in the iris datas set, Fisher developed a linear discriminant model to distinguish the species from each other.

[Wikipedia - Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
>Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

According to Fisher's paper, [The Use of Multiple Measurements in Taxonomic Problems by R.A Fisher](https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x):
>When two or more populations have been measured in several characters, xl, ...,x8, special interest attaches to certain linear functions of the measurements by which the populations are best discriminated.

His paper then applies the principle of the linear discriminant model to the sample of iris flowers to see how it could be used to discriminate or distinguish the species of iris plant. 

The two species Iris Setosa and Iris Versicolor were found growing together in the same colony. The sample of the third species - the Iris Virginica differs from the other two samples as they were not taken from the same natural colony. 

Fisher considered the question of what linear function of the four measurements would maximise the ratio of the difference  between the specific means to the standard deviation between species.


Include images of the three iris class.
Here using a url to the image located online
![iris-setosa](https://en.wikipedia.org/wiki/File:Kosaciec_szczecinkowaty_Iris_setosa.jpg "iris-setosa")
![iris-versicolor](https://en.wikipedia.org/wiki/File:Iris_versicolor_3.jpg "iris-versicolor")
![iris-virginica](https://en.wikipedia.org/wiki/File:Iris_virginica.jpg "iris -virginica")

Here I am linking to an image I am saving into the repository into a folder called `images`
![iris-setosa](/images/iris_setosa.jpg)
![iris-virginica](/images/iris_virginica.jpg)
![iris-versicolor](/images/iris_versicolor.jpg)








Table 1 from Fisher's paper `The Use of Multiple Measurements in Taxonomic Problems` shows the four measurement for each of the three Iris Species. 
- Sepal length
- Sepal width
- Petal length
- Petal Width
insert image of table 1.


Include images of the three iris class.
Here using a url to the image located online
![iris-setosa](https://en.wikipedia.org/wiki/File:Kosaciec_szczecinkowaty_Iris_setosa.jpg "iris-setosa")
![iris-versicolor](https://en.wikipedia.org/wiki/File:Iris_versicolor_3.jpg "iris-versicolor")
![iris-virginica](https://en.wikipedia.org/wiki/File:Iris_virginica.jpg "iris -virginica")

Here I am linking to an image I am saving into the repository into a folder called `images`
![iris-setosa](/images/iris_setosa.jpg)
![iris-virginica](/images/iris_virginica.jpg)
![iris-versicolor](/images/iris_versicolor.jpg)



[Multiple Measurements in Taxonomic Problems by R.A Fisher](https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x)


## 2. References

- [Python Data Analysis Library](https://pandas.pydata.org)

- [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)

- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

- [Github Flavoured Markdown](https://github.github.com/gfm/#what-is-github-flavored-markdown-)

- [UCI Machine Learning Repository: Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)

- [Python, R and Linux Tips](https://cmdlinetips.com/category/python/)

- [Wikipedia - Iris Flower Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set)

- [Wikipedia - Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher)

- [cmdlinetips.com](https://cmdlinetips.com/2018/01/7-tips-to-read-a-csv-file-as-pandas-data-frame/)

- [Iris Dataset - Exploratory Data Analysis](https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis)

- [seaborn:statistical data visualisation ](https://seaborn.pydata.org/index.html)

- [Multiple Measurements in Taxonomic Problems by R.A Fisher](https://onlinelibrary.wiley.com/doi/pdf/10.1111j.1469-1809.1936.tb02137.x)

- Python for Data Analysis - Wes McKinney
Data Wrangling with Pandas, NumPy and IPython



For this project, I am mainly working through the pandas documentation at - [https://pandas.pydata.org](https://pandas.pydata.org). I am also using the `seaborn` library for plotting and hope to explore some of the other python libraries.
I am also reading through the `Python for Data Analysis` book by Wes McKinney, who is the creator of the Python Pandas project.

## 3. Download the dataset and investigate it using Python code
<a name="loading"></a>
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

There are several tables in Fisher's paper which I will try to reproduce.
The first table, Table 1 shows the 4 measurement variables for each observation of the three iris species.
The equivalent data is shown in the iris DataFrame resulting from reading in the csv file, although the layout is slightly different.

Table II in Fisher's paper is entitled *Observed means for two species and their difference (cm.)*
This table displays the means for each of the 4 measurements for the Iris-Versicolor and Iris-Setosa species. It also shows the differences between the Versicolor means and the Setosa means for each of the 4 measurement variables.

I want to try and get the same information in Table 2 of Fisher's paper.
Table II. Observed means for two species and their difference(cm.)

### Viewing the dataset.

Can use  `.head()` to look at the observations at the top of the dataset and `.tail()` to lool at the observations at the end of the dataset

The far left (without a column name) contains the index of the dataframe which in this case is a range from 0 to 150 in steps of 1.

The `pandas.index()` can be used to look at the index of the dataframe. and `pandas.columns()` to look at the columns of the dataset.
When the data set is read in using, an index is automatically assigned starting at 0, stopping and 150.

The columns on the dataset will contain the column names I used in reading in the csv file.
'Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width','Species'

The data set has 150 rows and 5 columns. 
`.shape()`

### Indexing and Filtering the data set

There are several ways of selecting data from the DataFrame that is detailed on the pandas documentation.
http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-and-selecting-data

Indexing with square brackets will return a Series corresponding to the column name.
A column of data can be retrieved from the Iris DataFrame using dict-like notation or by attribute such as 
`iris.Petal_Width_cm`

The rows of the iris DataFrame can be retrieved by position name or using the loc attribute.
The index operators can be used to select a subset or rows and columns using `loc` for axis labels or `iloc` for integers.
The index for the iris DataFrame at the moment is just a range of integers from 0 to 150 
An index into the dataframe can used to retrieve one or more columns either with a single value or a sequence

[Boolean Indexing](http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#boolean-index)ing

Can select rows from a DataFrame using a boolean vector the same length as the DataFrame’s index. This can be used to filter the data here for a particular class or species of the iris plant.

#### Groupby 
Can use groupby to split the iris data into groups based on the species. Can then do groupwise operatations such as summary statistics etc.
This will keep the entire data set in the one file but operations can be applied to each group and the results will be at group level.


http://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
`group by` is a process involving one or more of the following steps:

- First split the data into groups based on some criteria.
Split the data into groups and then do something with the individual groups

- Applying a function to each group independently.
Aggregation function such as computing summary statistic for each group, group sums or means, group sizes and group counts
Transformation function to perform some group-specific computations and return a like-indexed object. 

- Combining the results into a data structure.




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
`Seaborn` is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures. `Seaborn` provides a high-level interface for creating nice looking and informative plots. 
`Seaborn` has dataset-oriented plotting functions that operate on dataframes such as iris.

Can use it to draw a facetted scatter plot. The iris measurement variables determine the position of each point on the axes.

A `scatter plot` can be used to visualize relationships between numerical variables such as the petal measurements and the sepal measurements in the iris data set.  A `catplot()` can capture the relationship between a numeric variable and one (or more) categorical variables, such as the class or species of iris plant. 

The [Visualising dataset structure](http://seaborn.pydata.org/introduction.html#visualizing-dataset-structure) section of the `Seaborn` documentation actually illustrates using the iris data set. 
While `jointplot()` focusses on a single relationship in the data set, `pairplot()` shows all pairwise relationships and the marginal distributions that can be conditioned on a categorical variable.




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

### Note to myself about all the files! 
For  now I am working with several scripts for different sections of the project as I try out different things from the pandas documentation and the book `Python for Data Analysis` by Wes McKinney.
In particular, I am keeping the plots separate so I don't have to generate plots everytime I try something new to me.  
For the project submission though, I intend to put my final script into a single python script.

I am also trying out Jupyter notebook again but being careful this time to make sure that the changes are actually saved before I exit out of it in the Terminal!
Its far easier to run lines of code at a time and to see the output but I will transfer it back into the python script.

I have been working on a Jupyter notebook and downloaded it as a `ipynb` notebook and have also downloaded it as a python script which I will update to my repository.
For the submission, I will tidy all the scripts into one python script and one jupyter notebook.
The main files I am working on are `iris_expl.py`, `project_iris` and `exploring_iris.ipynb`
`project_iris` is the name I am saving my current jupyter notebook to, both as a notebook and as a .py python file.

On exiting the Jupyter notebook 
 file:///Users/angelacorkery/Library/Jupyter/runtime/nbserver-1892-open.html
http://localhost:8889/?token=3e22d6124c915eaecd374f44fc171a0f2eeb49c351331eeb


#### to run the scripts
Make sure you have Python 3 installed. If not go to https://www.python.org/downloads/ and follow the instructions.

To run each python program, first navigate to the folder downloaded from this repository.

At the command line enter python <program_name> for example: $ python isi_expl.py

The python program can also be run inside the environment of an iPython session using the `%run` command.
 `% run iris_expl.py`

