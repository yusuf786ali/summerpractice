import sys

#seq ACGTCGTATGTA
seq = sys.argv[1]
k = 0
for i in range(0, len(seq)-2):
    codon = seq[i:i+3]
    print(i+1, i%3 + 1, codon)