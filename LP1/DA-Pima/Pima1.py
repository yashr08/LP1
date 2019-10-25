#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


dataset = pd.read_csv("Diabetes.csv")
dataset


# In[3]:


dataset.shape


# In[4]:


dataset.describe()


# In[5]:


print(dataset.isnull().any())


# In[7]:


x = dataset.iloc[: ,: -1].values
y = dataset.iloc[: , -1].values
print('x size: ', x.shape, 'data type of x', type(x))
print('y size: ', y.shape, 'data type of y', type(y))


# In[8]:


from sklearn.model_selection import train_test_split


# In[9]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33 , random_state = 0)


# In[10]:


x_train.shape


# In[11]:


y_train.shape


# In[12]:


x_test.shape


# In[14]:


from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(random_state = 0)
lr.fit(x_train, y_train)
y_pred_lr = lr.predict(x_test)


# In[15]:


from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train, y_train)
y_pred_nb = nb.predict(x_test)


# In[16]:


from sklearn.svm import SVC
svm = SVC(kernel = 'linear' , random_state = 0)
svm.fit(x_train, y_train)
y_pred_svm = svm.predict(x_test)


# In[17]:


from sklearn.metrics import confusion_matrix, accuracy_score, f1_score


# In[18]:


cm_lr = confusion_matrix(y_test, y_pred_lr)
print('Confusion Matrix for Logistic Regression: ', cm_lr, sep = '\n')
cm_nb = confusion_matrix(y_test, y_pred_nb)
print('Confusion Matrix for Naive Bayes: ', cm_nb, sep = '\n')
cm_svm = confusion_matrix(y_test, y_pred_svm)
print('Confusion Matrix for SVC: ', cm_svm, sep = '\n')


# In[19]:


accuracy_lr = accuracy_score(y_test, y_pred_lr)
fscore_lr = f1_score(y_test, y_pred_lr)
print('Logistic Regression\nAccuracy Score: ' , accuracy_lr, '\nF Score: ', fscore_lr)
accuracy_nb = accuracy_score(y_test, y_pred_nb)
fscore_nb = f1_score(y_test, y_pred_nb)
print('NaiveBayes\nAccuracy Score: ' , accuracy_nb, '\nF Score: ', fscore_nb)
accuracy_svm = accuracy_score(y_test, y_pred_svm)
fscore_svm = f1_score(y_test, y_pred_svm)
print('SVC\nAccuracy Score: ' , accuracy_svm, '\nF Score: ', fscore_svm)


# In[ ]:




