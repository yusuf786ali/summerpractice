import sys
import random

genomesize = int(sys.argv[1])
readsize = int(sys.argv[2])
coverage = int(sys.argv[3])
limit = int(sys.argv[4])

genome = []

for i in range(int(genomesize)):
    genome.append(0)

for _ in range(genomesize * coverage//readsize):
    start  = random.randint(0, (len(genome)-(int(readsize))))
    stop = start + int(readsize)
    for j in range(start, stop):
        genome[j] += 1

total = 0
for num in genome:
    if num >= 1:
        total += 1


observed = [0] * limit



for x in genome[readsize:-readsize]:
    observed[x] += 1

for x in range(limit):
    print('The value', x, 'is seen', observed[x],
           'times which is', (observed[x]/(genomesize-readsize*2)*100), 
           'of total genome')

print(observed)
print(genome)

#print('% coverage is', ((total/len(genome))*100))