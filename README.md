# pands-project
Project 2019 for Programming and Scripting Module

This repository contains my submission for the class project for the Programming and Scripting Module at GMIT as part of the Higher Diploma in Computing and Data Analytics. 
The pdf file containing the problem set instructions is available by clicking on the following link.
- [Programming and Scripting Project 2019](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)  


## Problem Statement <a name="problem-statement"></a>

The project concerns the well-known Fisher's Iris data set. 
The project entails researching the data set, and then writing documentation and code in the Python programming language based on that research.

The project should achieve the following goals:

1. Research background information about the data set and summarise it.    
2. Provide a list of references used in completing the project.  
3. Download the data set using Python code.
4. Investigate the data set using python code  
5. Summarise the data set using python. Provide summary statistics.  
5. Summarise the investigations.
6. Include supporting tables and graphics.

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
- [-] Download the Iris data set  
- [ ] Investigate the Iris data set using python code
- [ ] Summarise the Iris data set - provide statistics such as means, minimum and maximum values
- [ ] Include tables and graphics
- [ ] Clearly document how to run the code used to investigate the Iris data set  
- [ ] Clearly document what the python code used actually does
- [ ] Look at examples of interesting analyses pursued by other people on the Iris data set 
- [ ] Refer to task list as a guideline
- [ ] Use headings as links, maybe create a table of contents
- [ ] keep the jupyter notebook in line with the python script and readme document.
- [ ] get links to images working

# Table of Contents

1. Introduction and problem statement
2. [Background information about the Iris data set](#background) 
3. [python libraries](#pythonlibraries)
4. [Download the Iris data set using python code](#loading)
5. [Exploring the data set](#exploring)
6. [Summarise the data set](#summarise)
7. [conclusions](#conclusions)
8. [Terms uses](#terms)

Taxonomy is the branch of science concerned with classification, especially organisms (Oxford Dictionary)
A sepal is the green part of the flower that protects the petals.

10. [References](#references)


## 1. Background information about the dataset 
<a name="loading"></a> 

Fisher's Iris data set is a famous database consisting of the measurements of parts of 150 iris flowers. It is available from the UCI Machine Learning Repository where it is listed as a multivariate data set with a default machine learning task of classification. The data set consists of 150 instances with 5 attributes. The data set was donated in 1988 by Michael Marshall but the data set was created by R.A. Fisher in 1936. 
http://archive.ics.uci.edu/ml/datasets/Iris.

The data set includes 50 plants each of three classes of iris plant, where each class is a different type or species of iris plant.
The three classes are Iris Setosa, Iris Versicolor and Iris Virginica. 
Four flower measurements are given for each observation in the data set, which are the lengths and widths of the petals and the sepals of the flowers in the sample.


 Iris Setosa,   Iris Versicolor and Iris Virginica
<p float="left">
  <img src="images/iris_setosa.png" height="200" alt="iris setosa" />
  <img src="images/iris_versicolor.png" height="200" alt = "versicolor" />
  <img src="images/iris_virginica.png" height="200" alt ="iris virginica" /> 
</p>

See [iris_flower_description](iris flowers description.md) for more details.

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

Table 1 from Fisher's paper `The Use of Multiple Measurements in Taxonomic Problems` shows the four measurement for each of the three Iris Species. 
- Sepal length
- Sepal width
- Petal length
- Petal Width  
<img src="images/IrisTable1.png" height="200" alt="Fisher Table I">


## How to run the python code

The purpose of this project is to investigate the Fisher Iris data set described above using python code.
Python is a high level interpreted general purpose programming language. The python interpreter and its extensive standard library are freely available to all. Along with the python standard library, there are many libraries that enhance the usage of python and make it a powerful tool for performing data analytics and machine learning.
Make sure you have Python 3 installed. If not go to https://www.python.org/downloads/ and follow the instructions.

To run the python script, first navigate to the folder downloaded from this repository.

At the command line enter python <program_name> for example: $ python project_iris.py

The python program can also be run inside the environment of an iPython session using the `%run` command.
 `% run project_iris.py`

### Loading python libraries

The `pandas` library is the main python library being used in this project. According to the [pandas package overview ](https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html)  

> `pandas` is a `Python` package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python. 

In addition to `pandas`, the `seaborn` library is also used for plotting which requires `matplotlib.pyplot` for some functions.

[seaborn.pydata.org](https://seaborn.pydata.org/index.html)
>Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics

[matplotlib.org](https://matplotlib.org)
>Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms

The pandas library is imported in the script using `import pandas as pd`. Therefore wherever `pd` is used in the script, it is referring to the pandas library. Similarly, the `seaborn` library is imported as `sn` and thereafter referred to using `sn` 

Help can be obtained using the python help function
For example `help(pd)` or `help(pd.DataFrame.describe)`

### Getting help in python
To get help on any function, I can use the python help function https://docs.python.org/3/library/pdb.html?highlight=help#pdbcommand-help with the command in parentheses.
 `help(pd)` will show help on the package pandas.
 I can get more specific help as follows:
 `help(pd.DataFrame.describe())`
 
-[Pandas.pydata documentation](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html)  
-[Matplotlib documentation](https://matplotlib.org/index.html)  
-[Seaborn.pydata documentaion](https://seaborn.pydata.org/index.html)  
-[Python 3 documentation](https://docs.python.org/3/index.html)  


## 3. Download the dataset and investigate it using Python code
<a name="loading"></a>
The Iris Data Set is available in csv format from the UC Irvine Machine Learning Repository at http://archive.ics.uci.edu/ml/datasets/Iris.

The data set itself at the UCI Machine Learning repository does not have the attribute information included in the csv file. However this information can be found under the section [Iris Data Set: Attribute Information](https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names)

 Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      - Iris Setosa  
      - Iris Versicolor  
      - Iris Virginica  


According to [pandas.pydata.org](https://pandas.pydata.org/index.html),the python `pandas` open source library provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language. `pandas` is designed for working with data that is in a tabular format containing an ordered collection of columns where each column can have a different value type.  This makes it ideal for exploring a structured tabular dataset such as Iris which contains several numerical columns and one categorical column. 

Using `pandas` tabular data can be imported as a `DataFrame` object. According to the [pandas docs - DataFrame](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame)
>A `DataFrame` is a two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). Arithmetic operations align on both row and column labels. 
A pandas `DataFrame` represents a rectangular table of data containing an ordered collection of columns and each column can have a different value type.

The pandas `read_csv`function loads delimited data from a file, URL or file-like object using a comma as the default delimiter and  creates a DataFrame. When a pandas `DataFrame`  object is created, it has many attributes and methods available.

The Iris data set can be read in directly from the url at [https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data] (https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)or alternatively it can be saved locally and read in by specifiying the file path.   
In the script, I will download the csv file into python as part of the script. (I haved also saved the csv file containing the Iris data set into this project's repository for convenience). 

The csv file can be inspected on the command line using the `cat` command which prints the raw contents of the file to the screen or the `head` command  which prints just the first 10 rows to the screen. The file has 4 numerical columns and 1 descriptive string column. 

The `pandas.read_csv` function performs type inference. The data types for each column will be inferred by the `read_csv` function. 
A `DataFrame` has both a row and a column index.  When csv data is imported into python using `pandas.read_csv`, an index is added to the `DataFrame` by default if none is provided. This is a range of numbers beginning at 0 for the first observation.

As mentioned earlier, the raw csv file does not contain any headers. However, this information is available on the Iris data set page at the UCI Machine Learning Repository the under 'attribute_information'. I can add the column names to the DataFrame. 

The `pandas` library must first be imported before it can be used as it not part of the Python standard library. 
At the beginning of the script, I import the `pandas` library using `import pandas as pd`, along with any other libraries to be used in this project.
This imports the `pandas` library and allow all of its functions to be used by the script.

My code for reading in the data set does the following:

1. Create `csv_url` and pass to it the url where the data set is available 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'. 
2. Create a list of column names `col_names` using the iris attribute information. 
3. Create a panda's DataFrame object called `iris`.
There are other parameters which can be set for the `read_csv` function and these can be found using `?pd.read_csv`. 

```
      csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
      # using the attribute information as the column names
      col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
      iris =  pd.read_csv(csv_url, names = col_names)
```

Having loaded the iris data set, the resulting `iris` DataFrame can be viewed using the DataFrame methods `head` and `tail` to see the first rows and the last rows respectively. 

## Exploring the dataset - summary results
The `pandas` library has many functions that can be used to explore the Iris data set. Having imported the iris data set from a csv file into a pandas `DataFrame`, all the attributes and methods of `DataFrame` objects can be used on the iris DataFrame object.

##### Attributes of the iris DataFrame 
I looked at the attributes of the `iris` DataFrame in the section # EXPLORING & INVESTIGATING THE IRIS DATA SET of the project_iris.py python script.   

In summary:  
- The iris DataFrame has two dimensions.   (`ndim`)
- It consists of 150 rows and 5 columns corresponding to the 150 rows of observations in the csv data and the five columns of data.(`shape`) 
- The columns on the dataset contain the column names that were specified when reading in the csv file. (`columns`)
'Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width','Species'. (If the csv data set had contained a row of column names at the top of the file, then this could have been used to set the column names.)  
- There are 750 elements in total in the iris dataframe.  (`size`)
- The dataframe is assigned a range index by default on reading in the data set. This index starts at 0 for the first row of observations and goes up to 149 for the last row of observations. The index can be changed if desired.   (`index`)
- The datatypes of the numeric measurement columns are floats.   (`dtypes`)

##### Using `DataFrame` methods to explore the iris data set.

- The `head` and `tail` methods are useful to take a quick look at the observations at the top and bottom rows of the dataframe. The number of rows to display can be specified as an argument. The rows at the top belong to the setosa class. The rows at the bottom belong to the virginica class. This is just the way the observations are ordered in the csv data set. 

![iris_head](images/iris_head.png)
![iris_tail](images/iris_tail.png)

- `pandas` objects have a set of common mathematical and statistical methods. Most of these methods produce a single value such as the mean or the max or standard deviation.  Multiple summary statistics can be obtained in one go using pandas.descibe().

- Using the `describe` method to produce some quick summary statistics produces the following table. These statistics are for the data set as a whole. (Later I look at the descriptive statistics by class or species of iris plant).

- The various statistics that are generated from the `describe` function can also be obtained on their own. For example the mean could be obtained using `iris.mean()`, minimum with `.min()` etc.

![iris_describe](images/iris_describe.png)

- The initial exploration of the Iris DataFrame shows that there are 150 rows and 5 columns of data. 
Each row corresponds to an individual observation of an iris plant. The columns show the individual measurements (in centimetres) of the length of the sepal, the length of the petal, the width of the sepal and the width of the petal.

The mean of the Sepal length is greater than the mean of the other three measurements. 
The measurements of the petal width has the lowest average measurements. 
The standard deviation in the petal lengths shows the highest variability of the four measurements at 1.76 while the standard deviations of the petal width is approx 0.43.

The shortest petal in the data set is 1 cm while the longest petal is 6.9 cm.
The widths of the petals vary from 0.1 cm to 2.5 cm.
The shortest sepal in the data set is 4.3 cm while the longest sepal is 7.9 cm. The narrowest sepal is 2cm while the widest sepal is 4.4 centimetres.

The data can be checked for any missing values. By default the descriptive statistics on pandas objects exclude missing value.  The Iris dataset does not have any missing values. `pandas.isnull` can be used to check for missing data. This returns a True or False for each observation. Boolean values are coerced to 1 for True and 0 for False so the `sum` function can be used to count the number of True values rather than printing all the True and False values.
`notnull()` is the opposite of `isnull` while `notna` is the opposite of `isna`.

#### histogram - insert plot images
A `histogram`is a representation of the distribution of data. The pandas hist function calls `matplotlib.pyplot.hist` on each series in
the DataFrame, resulting in one histogram per column.

#### histogram - insert plot images
The histograms show the distribution of the measurements with one plot for each type of measurement.
The histogram for the petal lengths show a clear group of observations having petal lengths that are much smaller than the rest of the observations. Similarly with the petal widths. The sepal lengths show quite a bit of variation with a number of peaks while sepal widths seem to be centred around 3 cms but with a few smaller peaks at both sides of 3 cms.

There are three classes or species of iris flower in this data set, the Iris Setosa, the Iris Versicolor and the Iris Virginica.
It is possible to look at the summary statistics as the class or species level which I will describe later on.
For now I will continue with exploring the data set over all.

# I AM HERE! 
As mentioned earlier, Fisher's iris dataset is a well known data set in pattern recognition literature. One class / species of the three iris classes is linearly separable from the other two classes, which are not linearly separable from each other. 
Therefore I will now look at the different classes on their own. To do so, I will need to be able to separate the observations into three groups based on their known class.   

`pandas` has a groupby function that can be used to group the data by a Series of columns. 
A `groupby` operation involves some combination of splitting the data into groups based on some criteria and applying a function to each group independently. 
I can do this to the iris data set and then look at the characteristics and statistics of each subset group. The observations will be grouped by Class or species of iris plant.

(An aternative option would be to create subsets of the iris DataFrame for each class or species of Iris plant and then perform the operations on each subset dateFrame.)


## GroupBy statistics

GroupBy objects are returned by groupby calls. Descriptive statistics and computations can be applied to these GroupBy objects,

### Interpreting Summary Statistics of the Iris data set
The pandas `describe` function shows the count number of the non-NA/null observations in the dataset. There are 50 observations in each class. The `max` shows the maximum of the values and the `min` shows the minimum of the values. The `mean` shows the mean of the values, the `std` shows the standard deviation of the observations. The `describe` function also shows the 25th, 50th and 75th percentiles. The 25th percentile shows the percentage of values falling below that percentile. The 50th percentile shows the same information as the median would, that is where 50% of the values fall above and 50% fall below the value.

The statistics at the class level show that the average petal length for a Setosa is much smaller at 1.464 cm than the other two classes. The average petal length for the Versicolor is 4.26 while the iris Virginica has the largest average petal length of 5.552 centimetres which is almost four times greater than the petal length of the Iris Setosa.
The standard deviation of the setosa petal length is quite small compared to the standard deviation of the other two species. The petal measurements of the iris setosa is much less variable than that of the other two species. 

The average petal width of the setosa is also much smaller than the average petal width of the other two species. In fact the petal width of the setosa is twelve times smaller than the petal width of the virginica. There is less variability in petal widths in all three species though compared to the variability in the petal length.
There is not such a large difference between the sepal lengths of the three iris species, although the setosa is again showing the smallest average measurements.
The average sepal width of the setosa however is actually larger than the averages for the other two species. The average sepal width for the setosa is 3.42 centimetres compared to an average of 2.77 cm for the Versicolor and 2.97 for the virginica. This is also shown in the minimum and maximum measurements for the three species.

From the summary statistics of the sepal and petal measurements by class type it would seem that the iris setosa is very different from the other two species, the versicolor and the virginica.

There are several tables in Fisher's paper which I will try to reproduce.
The first table, Table 1 shows the 4 measurement variables for each observation of the three iris species.
The equivalent data is shown in the iris DataFrame resulting from reading in the csv file, although the layout is slightly different.

Table II in Fisher's paper is entitled *Observed means for two species and their difference (cm.)*
This table displays the means for each of the 4 measurements for the Iris-Versicolor and Iris-Setosa species. It also shows the differences between the Versicolor means and the Setosa means for each of the 4 measurement variables.

I will try  to get the same information as in Table 2 of Fisher's paper.


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



## 10. References
<a name="references"></a>

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
