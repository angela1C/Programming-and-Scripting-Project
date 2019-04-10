

```python
import numpy as np
import pandas as pd
```

### Object Creation

#### A DataFrame
A dataframe represents a rectangular table of data and contains an ordered collection of columns, each of which can be a different value type. A dataframe has both a row and column index and can be thought of as a dict of Series, all sharing the same index.
A column in a dataframe can be retrieved as a Series.
The columns of the resulting DataFrame have different dtypes.


```python
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = pd.read_csv(csv_url, header = None)
```

The csv file at the UCI repository does not contain the variable names.
They are located in a separate file


```python
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']

# read in the dataset from the UCI Machine Learning Repository link and specify column names to use
# save as iris_df
iris =  pd.read_csv(csv_url, names = col_names)
```


```python
# The columns of the resulting DataFrame have different dtypes.
iris.dtypes
```




    Sepal_Length    float64
    Sepal_Width     float64
    Petal_Length    float64
    Petal_Width     float64
    Species          object
    dtype: object



### Viewing Data
Can view the top and bottom of the DataFrame, the index and the column names


```python
iris.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal_Length</th>
      <th>Sepal_Width</th>
      <th>Petal_Length</th>
      <th>Petal_Width</th>
      <th>Species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python
iris.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal_Length</th>
      <th>Sepal_Width</th>
      <th>Petal_Length</th>
      <th>Petal_Width</th>
      <th>Species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>145</th>
      <td>6.7</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.3</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>146</th>
      <td>6.3</td>
      <td>2.5</td>
      <td>5.0</td>
      <td>1.9</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>148</th>
      <td>6.2</td>
      <td>3.4</td>
      <td>5.4</td>
      <td>2.3</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>149</th>
      <td>5.9</td>
      <td>3.0</td>
      <td>5.1</td>
      <td>1.8</td>
      <td>Iris-virginica</td>
    </tr>
  </tbody>
</table>
</div>




```python
# View the index of the DataFrame
iris.index
```




    RangeIndex(start=0, stop=150, step=1)




```python
# View the columns of the DataFrame
iris.columns
```




    Index(['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width',
           'Species'],
          dtype='object')




```python
# sorting by an axis
iris.sort_index(axis=1, ascending=False).head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Species</th>
      <th>Sepal_Width</th>
      <th>Sepal_Length</th>
      <th>Petal_Width</th>
      <th>Petal_Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Iris-setosa</td>
      <td>3.5</td>
      <td>5.1</td>
      <td>0.2</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Iris-setosa</td>
      <td>3.0</td>
      <td>4.9</td>
      <td>0.2</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Iris-setosa</td>
      <td>3.2</td>
      <td>4.7</td>
      <td>0.2</td>
      <td>1.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Iris-setosa</td>
      <td>3.1</td>
      <td>4.6</td>
      <td>0.2</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Iris-setosa</td>
      <td>3.6</td>
      <td>5.0</td>
      <td>0.2</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Iris-setosa</td>
      <td>3.9</td>
      <td>5.4</td>
      <td>0.4</td>
      <td>1.7</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Iris-setosa</td>
      <td>3.4</td>
      <td>4.6</td>
      <td>0.3</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Iris-setosa</td>
      <td>3.4</td>
      <td>5.0</td>
      <td>0.2</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Iris-setosa</td>
      <td>2.9</td>
      <td>4.4</td>
      <td>0.2</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Iris-setosa</td>
      <td>3.1</td>
      <td>4.9</td>
      <td>0.1</td>
      <td>1.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# sorting by values
iris.sort_values(by='Petal_Width').head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal_Length</th>
      <th>Sepal_Width</th>
      <th>Petal_Length</th>
      <th>Petal_Width</th>
      <th>Species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>32</th>
      <td>5.2</td>
      <td>4.1</td>
      <td>1.5</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>13</th>
      <td>4.3</td>
      <td>3.0</td>
      <td>1.1</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>37</th>
      <td>4.9</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4.9</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>12</th>
      <td>4.8</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>34</th>
      <td>4.9</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.1</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>27</th>
      <td>5.2</td>
      <td>3.5</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>28</th>
      <td>5.2</td>
      <td>3.4</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>29</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.6</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>



### Selection

#### Getting
can select a single column, which yields a Series.
Selecting via [] slices the rows.

It is recommended to use the optimized pandas data access methods, .at, .iat, .loc and .iloc.


```python
# Selecting a single column, which yields a Series, equivalent to df.Sepal_Length

# can use labels in the index to select values or a set of values
iris['Sepal_Length'].head()


```




    0    5.1
    1    4.9
    2    4.7
    3    4.6
    4    5.0
    Name: Sepal_Length, dtype: float64




```python
# Selecting via [], which slices the rows.
# Looking here at the first 5 rows
iris[0:5]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal_Length</th>
      <th>Sepal_Width</th>
      <th>Petal_Length</th>
      <th>Petal_Width</th>
      <th>Species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>



### Selection by Label


```python
# Selecting on a multi-axis by label
iris.loc[0:10, ['Sepal_Length', 'Petal_Length']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal_Length</th>
      <th>Petal_Length</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>1.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.4</td>
      <td>1.7</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4.6</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>5.0</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>4.4</td>
      <td>1.4</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4.9</td>
      <td>1.5</td>
    </tr>
    <tr>
      <th>10</th>
      <td>5.4</td>
      <td>1.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
# reduction in the dimensions of the returned object
iris.loc[0, ['Sepal_Length', 'Petal_Length']]
```




    Sepal_Length    5.1
    Petal_Length    1.4
    Name: 0, dtype: object




```python
# a scalar value
iris.loc[0, 'Petal_Length']
```




    1.4




```python
# retrieve a column of the dataframe using a dict-like notation
iris['Petal_Length'].head()
```




    0    1.4
    1    1.4
    2    1.3
    3    1.5
    4    1.4
    Name: Petal_Length, dtype: float64




```python
# retrieve a column of data by attribute
iris.Sepal_Length.head()
```




    0    5.1
    1    4.9
    2    4.7
    3    4.6
    4    5.0
    Name: Sepal_Length, dtype: float64




```python
# as a series using the loc attribute
iris.loc[0]
```




    Sepal_Length            5.1
    Sepal_Width             3.5
    Petal_Length            1.4
    Petal_Width             0.2
    Species         Iris-setosa
    Name: 0, dtype: object



### Selection by position


```python
# Selection by position
iris.iloc[0:3, 0:4]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sepal_Length</th>
      <th>Sepal_Width</th>
      <th>Petal_Length</th>
      <th>Petal_Width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# getting a scalar value by position using iat
iris.iat[0,0]
```




    5.1




```python

```
