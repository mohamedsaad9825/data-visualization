#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv('E:\Machinfy\secion 10/housing2.csv - housing2.csv.csv')
df.head(10)


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.isnull().sum()


# In[6]:


sns.heatmap(df.isnull(),cmap='viridis',cbar=True,yticklabels=False)


# In[12]:


df.hist(bins=10,figsize=(15,10))


# In[16]:


plt.figure(figsize=(15,10))
sns.heatmap(data=df.corr(),cbar=True,annot=True,cmap='coolwarm').set_title('correlation')


# In[40]:


sns.pairplot(df,size=2.5)


# In[28]:


x=df.iloc[:,2] 
y=df.iloc[:,3] 
plt.scatter(x,y)


# In[32]:


x=df.iloc[:,2]
plt.hist(x,bins=15)


# In[34]:


x=df.iloc[:,2]
sns.distplot(x,bins=15)


# In[37]:


sns.boxplot(df['median_house_value'])


# In[ ]:




