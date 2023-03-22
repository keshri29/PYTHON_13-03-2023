#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv("ml1.csv")
df


# In[2]:


df.columns.values


# In[3]:


ml1=np.array(df)[:4,:4]
ml1


# In[ ]:


res=np.array(df)[:,-1]
res


# In[7]:


for i in range(0,len(res)):
    if res[i]=='y':
        h=ml1[i].copy()
        break
h


# In[8]:


for i in range(1,len(res)):
    if res[i]=='y':
        h=ml1[i].copy()
        break
h


# In[13]:


for i in range(0,len(ml1)):
    if res[i]=='y':
        for j in range(0,len(ml1[0])):
            if h[j]==ml1[i][j]:
                continue
            else:
                h[j]="?"
            
    
h


# In[11]:


for i in range(1,len(ml1)):
    if res[i]=='y':
        for j in range(1,len(ml1[1])):
            if h[j]==ml1[i][j]:
                continue
            else:
                h[j]="?"
            
    
h


# In[12]:


for i in range(2,len(ml1)):
    if res[i]=='y':
        for j in range(2,len(ml1[2])):
            if h[j]==ml1[i][j]:
                continue
            else:
                h[j]="?"
            
    
h


# In[ ]:




