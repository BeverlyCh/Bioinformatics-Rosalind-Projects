Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from Bio import Entrez, SeqIO, pairwise2

with open(r"C:\Users\Beverly Chigarira\Downloads\rosalind_need.txt", "r") as f:
    genbank_ids = ", ".join(f.readline().strip().split())
Entrez.email = "**@******"
handle = Entrez.efetch(db="nucleotide", id=[genbank_ids], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
print(pairwise2.align.globalms(records[0].seq, records[1].seq, 5, -4, -10, -1)[0][2])
