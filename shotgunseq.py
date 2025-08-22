import sys
import random

genomesize = sys.argv[1]
reads = sys.argv[2]
times = sys.argv[3]

genome = []

for i in range(int(genomesize)):
    genome.append(0)

for i in range(0, int(times)):
    value  = random.randint(0, (len(genome)-(int(reads))))
    value2 = value + int(reads)
    for j in range(0, len(genome)):
        if j in range(value, value2):
        #if (j >= value) and (j <= value2):
            genome[j] += 1
    print(value, value2)

total = 0
for num in genome:
    if num >= 1:
        total += 1

print('% coverage is', ((total/len(genome))*100))
print(genome)