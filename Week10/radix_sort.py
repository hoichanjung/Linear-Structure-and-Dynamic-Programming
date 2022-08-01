import math


import random
import math

N = 10
lstNumbers = list(range(N))
random.shuffle(lstNumbers)

def performRadixSort(seq):
    max = -999999
    
    for itr in range(len(seq)):
        if seq[itr] > max:
            max = seq[itr]
        D = int(math.log10(max))
        
        for itr1 in range(D+1):
            buckets = []
            for itr2 in range(10):
                buckets.append([])
            for itr2 in range(len(seq)):
                digit = int(seq[itr2] / math.pow(10, itr1)) % 10
                buckets[digit].append(seq[itr2])
            cnt = 0
            for itr2 in range(10):
                for itr3 in range(len(buckets[itr2])):
                    seq[cnt] = buckets[itr2][itr3]
                    cnt = cnt + 1
    return seq

print(performRadixSort(lstNumbers))