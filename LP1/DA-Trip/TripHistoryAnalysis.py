#!/usr/bin/env python
# coding: utf-8

# In[18]:


import glob
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB,MultinomialNB


# In[2]:


path = "./"
data = []
all_files = glob.glob(path+"/*.csv")
for filename in all_files:
    frame = pd.read_csv(filename,index_col=None, header=0)
    data.append(frame)
    
df = pd.concat(data,axis=0,ignore_index=True)


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df = df.drop(labels=['Start station','End station','Start date','End date','Bike number'],axis=1)


# In[6]:


df.head()


# In[7]:


df.isna().any()


# In[8]:


target_data = [df]
target_map = {'Member':1,'Casual':0}
for data in target_data:
    data["Member type"] = data["Member type"].map(target_map)


# In[9]:


df.head(10)


# In[10]:


df.dtypes


# In[11]:


target = df['Member type']
df = df.drop(labels=['Member type'],axis=1)


# In[12]:


X_train,X_test,Y_train,Y_test = train_test_split(df,target,test_size=0.3,random_state=True)


# In[19]:


model = MultinomialNB()


# In[20]:


model.fit(X_train,Y_train)


# In[21]:


pred = model.predict(X_test)


# In[22]:


confusion_matrix(Y_test,pred)


# In[23]:


model.score(X_test,Y_test)


# In[ ]:




