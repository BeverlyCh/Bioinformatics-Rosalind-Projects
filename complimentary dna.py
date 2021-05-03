Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from Bio import SeqIO
from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC

def match_reverse(seqs):
    count = 0
    for seq in seqs:
        my_seq = Seq(seq)
        reverse_seq = my_seq.reverse_complement()
        if my_seq == reverse_seq:
            count += 1
    return count

if __name__ == "__main__":
    with open (r'C:\Users\Beverly Chigarira\Downloads\rosalind_rvco.txt') as f:
        seqs = [str(record.seq) for record in SeqIO.parse(f, "fasta")]
    count = match_reverse(seqs)
    print(count)
