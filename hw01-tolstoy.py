#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re


# In[2]:


resp = requests.get("https://www.gutenberg.org/files/2600/2600-0.txt")
data = resp.text
data = data.lower()


# In[3]:


rule = re.compile(r"\w+")
match = rule.findall(data)


# In[4]:


curr = 0
unique_list = []
for x in match:
    if x not in unique_list:
        unique_list.append(x)
    


# In[5]:


print('Total unique words = ' + str(len(unique_list)))


# In[ ]:




