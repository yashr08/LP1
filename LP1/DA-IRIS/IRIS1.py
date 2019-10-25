#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[2]:


dataset = pd.read_csv("IRIS.csv")
dataset


# In[4]:


dataset.shape


# In[6]:


dataset.info()


# In[7]:


dataset.describe()


# In[8]:


dataset.sepal_length.value_counts()


# In[9]:


dataset.petal_length.value_counts()


# In[11]:


print('Sepal length summary: ', dataset.sepal_length.describe(), '\n', sep = '\n')
print('Sepal width  summary: ', dataset.sepal_width.describe(), '\n', sep = '\n')
print('Petal length summary: ', dataset.petal_length.describe(), '\n', sep = '\n')
print('Petal width  summary: ', dataset.petal_width.describe(), '\n', sep = '\n')


# In[12]:


dataset.head()


# In[20]:


min1 = dataset.sepal_length.min()
max1 = dataset.sepal_length.max()
sum1 = dataset.sepal_length.sum()
count1 = dataset.sepal_length.count()
mean1 = sum1/count1
range1 = min1 = max1
mean = dataset.sepal_length.mean()
median = dataset.sepal_length.median()
mode = dataset.mode(axis = 0, numeric_only = False)
standard_deviation = dataset.loc[: , 'sepal_length'].std()
variance = dataset.var()
percentile = dataset.sepal_length.quantile(0.25)

print('Min1: ', min1)
print('Max1: ', max1)
print('Mean1: ', mean1)
print('Range: ', range1)
print('Mean API: ', mean)
print('Mode API: ', mode)
print('Median API: ', median)
print('Standard Deviation API: ', standard_deviation)
print('Variance: ', variance, sep = '\n')
print('Percentile: ', percentile)


# In[22]:


dataset.hist(xlabelsize = 10, ylabelsize = 10, figsize=(10,10))


# In[24]:


data = np.array(dataset)
for i in range(1,4):
    plt.boxplot(np.array(data[: , i], dtype = 'float'))
    plt.show()


# In[26]:


sns.boxplot(data = dataset.iloc[: , 1:5])


# In[27]:


sns.boxplot(x = dataset.species , y = dataset.sepal_length)


# In[ ]:




