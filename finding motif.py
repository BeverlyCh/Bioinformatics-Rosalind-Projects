Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from string import maketrans
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from string import maketrans
ImportError: cannot import name 'maketrans' from 'string' (C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\lib\string.py)
>>> s='TATGCGCTTCTGCGCTTAAAGTAAGCATGCGCTTCCTGCGCTTTGCGCTTTGCGCTTCTGCGCTTCATCTTGCGCTTTGCGCTTTGCGCTTTGCGCTTCATGCGCTTTGCGCTTAATTGCGCTTCCTGCGCTTGAGGATGCGCTTGGCCTGCGCTTATGCGCTTTATAATACTGCGCTTTAAGTTGCGCTTTGCGCTTTATTTTGCGCTTGGAGTGCGCTTTGCGCTTGCGGTCTGCGCTTTGCGCTTATGCGCTTTGCGCTTGATGCGCTTTTGCGCTTGCACTGCGCTTAACTATCTGCGCTTGTGCGCTTTCCACCTGCGCTTAGGGTCGTGCGCTTTGCGCTTTGCGCTTTCGCTGCGCTTTTGTTTATTGCGCTTCTAGCTTGCGCTTATCATGTTGCGCTTGTGTGCGCTTTGCGCTTCCAGTGCGCTTTGTATGCGCTTACTGCGCTTTGAGGCGGATTGCGCTTGTTGCGCTTTGCGCTTTGCGCTTTCGGTGCGCTTTTGCGCTTTGCGCTTTGCGCTTCTGCGCTTATGCGCTTTGCGCTTTTTGCGCTTGATGCGCTTGTGCGCTTTGCGCTTGTGCGCTTGCGATGCCTGCGCTTTGCGCTTGTGCGCTTTGCGCTTTCTGCGCTTTGCGCTTCTGCGCTTCTGCGCTTCTGCGCTTACTGCGCTTCAGCTGCGCTTAGTCTGCGCTTTGCGCTTCGGTGCGCTTGATACTGCGAATTGCGCTTTGCGCTTGGATGCCTTGCGCTTTCTTCTTGCGCTTGGGTGCGCTTATGCGCTTTGCGCTTGTAGGCTATA'


t='TGCGCTTTG
'
#s=''
#t=''

tlen=len(t)
indeces=''
for i in range(0,len(s)):
    if s[i:i+tlen] == t:
        indeces+=str(i+1)+' '
print (indeces)
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
