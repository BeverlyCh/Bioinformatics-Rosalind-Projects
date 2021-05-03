#!/usr/bin/env python
# coding: utf-8

# In[4]:


#GeneBank Introduction
from Bio import Entrez

with open(r'C:\Users\Beverly Chigarira\Downloads\rosalind_gbk.txt') as input_data:
	genus, start_date, end_date = [line.strip() for line in input_data.readlines()]

Entr    
handle = Entrez.esearch(db='nucleotide', term=genus+'[ORGN]', mindate=start_date, maxdate=end_date, datetype='pdat')
record = Entrez.read(handle)

print (record['Count'])


# In[ ]:




