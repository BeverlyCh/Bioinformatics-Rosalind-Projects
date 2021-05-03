#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Pairwise global alignment solution

from Bio.Seq import Seq, translate
from re import finditer

with open(r'C:\Users\Beverly Chigarira\Downloads\rosalind_orfr.txt','r') as input_data:
	dna = Seq(input_data.read().strip())

# Get the starting position for each ORF in the dna sequence and translate.
ORF = [translate(dna[x.start():], table = 1, stop_symbol = '', to_stop= True) for x in finditer('ATG', str(dna))]
# Get the starting position for each ORF in the reverse complement sequence and translate.
ORF += [translate(dna.reverse_complement()[x.start():], table = 1, stop_symbol = '', to_stop= True) for x in finditer('ATG', str(dna.reverse_complement()))]

# Find the longest ORF.
longest_orf = max(map(str, ORF), key=len)

# Print and save the answer.
print (longest_orf)


# In[ ]:




