# Insert
x = ['a', 'b', 'd', 'e', 'f']
idxInsert = 2
valInsert = 'c'

y = list(range(6))

for itr in range(0, idxInsert):
    y[itr] = x[itr]
    
y[idxInsert] = valInsert

for itr in range(idxInsert, len(x)):
    y[itr+1] = x[itr]
    
x = y
 
# Delete
idxDelete = 3

y = list(range(5))

for itr in range(0, idxDelete):
    y[itr] = x[itr]
    
for itr in range(idxDelete+1, len(x)):
    y[itr-1] = x[itr]
    
x = y