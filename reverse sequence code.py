Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def reverse_complement(seq):
    listSeq = list(seq)
    listSeq.reverse()
    output = ''
    for base in listSeq:
        if base == "A":
            output += "T"
        if base == "T":
            output += "A"
        if base == "C":
            output += "G"
        if base == "G":
            output += "C"
    return output


>>> reverse_complement("")
