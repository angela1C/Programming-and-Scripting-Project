Here I just want to throw some extra python things that I have come across but that are not for the project.
Just so I can note them for later!


**BOLD**

cmd + shift + V to see markdown preview



# ipython

The following will bring up some help documentation for seaborn boxplot in a ipython session
get_ipython().run_line_magic('pinfo', 'sns.boxplot')















http://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html
Here are some tips from the essential basic functionality page that I want to keep note of for another time  as they could be useful.

Boolean reductions:
# You can apply the reductions: empty, any(), all(), and bool() to provide a way to summarize a boolean result.
((df > 0).all())
(df > 0).any()
(df > 0).any().any()

Combined with the broadcasting / arithmetic behavior, one can describe various statistical procedures, like standardization (rendering data zero mean and standard deviation 1), very concisely:

ts_stand = (df - df.mean()) / df.std()
 xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)

 You can select specific percentiles to include in the output:
 series.describe(percentiles=[.05, .25, .75, .95])

 he value_counts() Series method and top-level function computes a histogram of a 1D array of values. It can also be used as a function on regular arrays:

 the most frequently occurring value(s) (the mode) of the values in a Series or DataFrame using .mode()
 
#### http://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#aggregation-api
The aggregation API allows one to express possibly multiple aggregation operations in a single concise way. This API is similar across pandas objects, see groupby API, the window functions API, and the resample API. The entry point for aggregation is DataFrame.aggregate(), or the alias DataFrame.agg().

You can pass multiple aggregation arguments as a list. The results of each of the passed functions will be a row in the resulting DataFrame. These are naturally named from the aggregation function.

With .agg() is it possible to easily create a custom describe function, similar to the built in describe function.


http://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#dropping-labels-from-an-axis

A method closely related to reindex is the drop() function. It removes a set of labels from an axis:

## Boxplots
http://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html#box-plots

Boxplot can be colorized by passing color keyword. You can pass a dict whose keys are boxes, whiskers, medians and caps. If some keys are missing in the dict, default colors are used for the corresponding artists. Also, boxplot has sym keyword to specify fliers style.

"""
http://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html
Here are some tips from the essential basic functionality page that I want to keep note of for another time  as they could be useful.

Boolean reductions:
# You can apply the reductions: empty, any(), all(), and bool() to provide a way to summarize a boolean result.
((df > 0).all())
(df > 0).any()
(df > 0).any().any()

Combined with the broadcasting / arithmetic behavior, one can describe various statistical procedures, like standardization (rendering data zero mean and standard deviation 1), very concisely:

ts_stand = (df - df.mean()) / df.std()
 xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)

 You can select specific percentiles to include in the output:
 series.describe(percentiles=[.05, .25, .75, .95])

 he value_counts() Series method and top-level function computes a histogram of a 1D array of values. It can also be used as a function on regular arrays:

 the most frequently occurring value(s) (the mode) of the values in a Series or DataFrame using .mode()


"""
https://www.statisticssolutions.com/discriminant-analysis/

Discriminant analysis is a technique that is used by the researcher to analyze the research data when the criterion or the dependent variable is categorical and the predictor or the independent variable is interval in nature. The term categorical variable means that the dependent variable is divided into a number of categories. 

The objective of discriminant analysis is to develop discriminant functions that are nothing but the linear combination of independent variables that will discriminate between the categories of the dependent variable in a perfect manner. It enables the researcher to examine whether significant differences exist among the groups, in terms of the predictor variables. It also evaluates the accuracy of the classification.

https://www.statisticssolutions.com/regression-analysis-logistic-regression/
Logistic regression is a class of regression where the independent variable is used to predict the dependent variable.  When the dependent variable has two categories, then it is a binary logistic regression.  When the dependent variable has more than two categories, then it is a multinomial logistic regression. 


 Logistic Regression is used when the dependent variable(target) is categorical.

Logistic regression is a predictive analysis and is used to describe data and to explain the relationship between one dependent binary variable and one or more nominal, ordinal, interval or ratio-level independent variables. (https://www.statisticssolutions.com/what-is-logistic-regression/)
Logistic regression is a regression method when there are two categorical classes to be classified into. However when the classes are well separated then the parameter estimates for logistic regression method are unstable. Linear discriminat analysis does not have this problem and is also more stable than logistic regression when the sample is small and the predictors are approxinately normally distributed. Linear discriminant analysis is popular when we have more than two response classes as it provides low-dimensional views of the data.

# my summary
Fisher proposed discriminant analysis in 1936 to predict qualitative values.
Discriminant analysis is a method used in statistics when the dependent variable is categorical. Discriminant analysis looks for the best linear combination of independent variables that will discriminate between the categories of the dependent variables and to see if significant differences exists among the groups of predictor variables. 
It is a popular technique in statistics when there are more than two responses classes and is considered more stable than logistic regression (another statistical method for classifying qualitative or categorical variables) when the predictor classes are well separated. (also considered better when the sample size is small and the predictors are approximately normally distributed.).
The distribution of the predictor variables are modelled separately in each of the response classes or dependent variables.


# An introduction to statistical learning with applications in R by Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani
In order to predict qualitative values, such as whether a patient survives or dies, or whether the stock market increases or decreases, Fisher proposed linear discriminant analysis in 1936.

Logistic regression involves directly modeling Pr(Y = k|X = x) using the logistic function, given by (4.7) for the case of two response classes. In statistical jargon, we model the conditional distribution of the response Y , given the predictor(s) X. We now consider an alternative and less direct approach to estimating these probabilities. In this alternative approach, we model the distribution of the predictors X separately in each of the response classes (i.e. given Y ), and then use Bayes’ theorem to flip these around into estimates for Pr(Y = k|X = x). When these distributions are assumed to be normal, it turns out that the model is very similar in form to logistic regression.



Supervised learning is a well-understood area. In fact, if you have read the preceding chapters in this book, then you should by now have a good
G. James et al., An Introduction to Statistical Learning: with Applications in R, 373 Springer Texts in Statistics, DOI 10.1007/978-1-4614-7138-7 10,
© Springer Science+Business Media New York 2013
 
374 10. Unsupervised Learning
grasp of supervised learning. For instance, if you are asked to predict a binary outcome from a data set, you have a very well developed set of tools at your disposal (such as logistic regression, linear discriminant analysis, classification trees, support vector machines, and more) as well as a clear understanding of how to assess the quality of the results obtained (using cross-validation, validation on an independent test set, and so forth).
In contrast, unsupervised learning is often much more challenging. The exercise tends to be more subjective, and there is no simple goal for the analysis, such as prediction of a response. Unsupervised learning is often performed as part of an exploratory data analysis. Furthermore, it can be hard to assess the results obtained from unsupervised learning methods, since there is no universally accepted mechanism for performing cross- validation or validating results on an independent data set. The reason for this difference is simple. If we fit a predictive model using a supervised learning technique, then it is possible to check our work by seeing how well our model predicts the response Y on observations not used in fitting the model. However, in unsupervised learning, there is no way to check our work because we don’t know the true answer—the problem is unsupervised.


Anderson was interested in the variation in plant species or a group of species, and in evolution in general. Andersons's interest in the iris plants was for morphological reason and he was trying to find out how one species of Iris could have evolved from another species.

He had observed in his work that there was a lot of genetic variation within most populations of plants.  He set out to find a few easily recognisable, well-differentiated species. Anderson chose the Iris Versicolor (also known as the northern blue flags) because they were a 'comparatively simple, stable and well marked group'. He first selected Iris Versicolor as he believed it was clearly defined but then he found the Versicolor was actually two species which he could tell apart after some preliminary analysis. He then set out to find how one species could have evolved from another and collected a very large sample to analyse.... He had to find a third species that would provide an alternate parent for one of those studied and came across the Iris Setosa, native to Alaska. His research indicated that the Iris Versicolor of northeastern North America had arisen as an amphiploid, one parent being Iris Virginica of the Mississippi Valley and the Southeast Coast and the other being the I Setosa of the Yukon Valley Alaska.
From further study he showed that the variation with respect to leaves, stems and other vegetative charactersitics was due largely to phenotypic modification but that *reproductive charactersitics were remarkably constant for a genotype* and exhibited a large amount of genotypic variation within populations.
[Biographical Memoir of Edgar Anderson by G Ledyard Stebbins](nasonline.org)