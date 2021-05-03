#!/usr/bin/env python
# coding: utf-8

# In[11]:


from Bio import SeqIO

with open(r"C:\Users\Beverly Chigarira\Downloads\rosalind_subo.txt", "r") as input_data:
    dna = [fasta.seq for fasta in SeqIO.parse(input_data, 'fasta')]

# r value is the one with a 100% match between strings in the LaLign tool after executing the sequences
r = 'TAGCGCGAACAACCCCTGCATCGTCATTCGAACGGGCAGG'


print (len(r))

def HammingDistance(string1, string2):
        diffs = 0
        for ch1, ch2 in zip(string1, string2):
                if ch1 != ch2:
                        diffs += 1
        return diffs
for x in range(0, 2):
    count = 0
    stringx = dna[x]
    for i in range(0, len(stringx)-len(r)):
        string = stringx[i:i+len(r)]
        if HammingDistance(r, string) <= 3:
            count += 1
    print (count)


# In[ ]:





# In[ ]:




