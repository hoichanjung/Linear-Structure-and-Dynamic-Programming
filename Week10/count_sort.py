import random

N = 10
lstNumbers = list(range(N))
random.shuffle(lstNumbers)

print(lstNumbers)

def performCountSort(seq):
    max = -9999
    min = 9999
    
    for itr in range(len(seq)):
        if seq[itr] > max:
            max = seq[itr]
        if seq[itr] < min:
            min = seq[itr]
            
    counting = list(range(max-min+1))
    for itr in range(len(counting)):
        counting[itr] = 0
    for itr in range(len(seq)):
        value = seq[itr]
        counting[value-min] = counting[value-min] + 1
    cnt = 0
    for itr1 in range(max-min+1):
        for itr2 in range(counting[itr1]):
            seq[cnt] = itr1 + min
            cnt = cnt + 1
    return seq

print(performCountSort(lstNumbers))