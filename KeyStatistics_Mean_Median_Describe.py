#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load Libraries
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Load Data
df = pd.read_excel('./BlueJaysThreeMonthScores.xlsx', sheet_name='Sheet1')
df.head()


# In[3]:


df['Blue Jays Score'].mean()


# In[4]:


df['Blue Jays Score'].median()


# In[5]:


#Standard Deviation of Blue Jays Score
df['Blue Jays Score'].std()


# In[6]:


#Counts of Outcome
df['Outcome'].value_counts()


# In[7]:


#Key Statistics (Numerical Columns only)
df.describe()


# In[8]:


#Key Statistics - Transposed (Numerical Columns only)
df.describe().T


# In[ ]:




