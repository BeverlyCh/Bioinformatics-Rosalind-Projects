#!/usr/bin/env python
# coding: utf-8

# In[9]:


with open(r"C:\Users\Beverly Chigarira\Downloads\rosalind_subo.txt") as f:
    next(f, None) # ignore first line
    one_big_string = f.read().replace('\n', '')
    
print (one_big_string)


# In[2]:





# In[ ]:




