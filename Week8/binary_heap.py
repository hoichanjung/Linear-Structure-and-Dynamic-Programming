class BinaryHeap:
    
    arrPriority = {}
    arrValue = {}
    size = 0
    
    def __init__(self):
        self.arrPriority = {}
        self.arrValue = {}
        self.size = 0
        
    def enqueueWithPrioirty(self, value, priority):
        self.arrPriority[self.size] = priority
        self.arrValue[self.size] = value
        self.size = self.size + 1
        self.percolateUp(self.size - 1)
        
    def percolateUp(self, idxPercolate):
        if idxPercolate == 0:
            return
        parent = int((idxPercolate-1)/2)
        if self.arrPriority[parent] < self.arrPriority[idxPercolate]:
            self.arrPriority[parent], self.arrPriority[idxPercolate] = self.arrPriority[idxPercolate], self.arrPriority[parent]
            self.arrValue[parent], self.arrValue[idxPercolate] = self.arrValue[idxPercolate], self.arrValue[parent]
            self.percolateUp(parent)
            
    def dequeueWithPrioirty(self):
        if self.size == 0:
            return ''
        retPriority = self.arrPriority[0]
        retValue = self.arrValue[0]
        
        self.arrPriority[0] = self.arrPriority[self.size - 1]
        self.arrValue[0] = self.arrValue[self.size - 1]
        self.size = self.size - 1
        self.percolateDown(0)
        return retValue
        
    def percolateDown(self, idxPercolate):
        if 2*idxPercolate + 1 >= self.size:
            return
        else:
            leftChild = 2*idxPercolate+1
            leftPriority = self.arrPriority[leftChild]
        if 2*idxPercolate + 2 >= self.size:
            rightPriority = -99999
        else:
            rightChild = 2*idxPercolate+2
            rightPriority = self.arrPriority[rightChild]
        if leftPriority > rightPriority:
            biggerChild = leftChild
        else:
            biggerChild = rightChild
            
        if self.arrPriority[idxPercolate] < self.arrPriority[biggerChild]:
            self.arrPriority[idxPercolate], self.arrPriority[biggerChild] = self.arrPriority[biggerChild], self.arrPriority[idxPercolate]
            self.arrValue[idxPercolate], self.arrValue[biggerChild] = self.arrValue[biggerChild], self.arrValue[idxPercolate]
            self.percolateDown(biggerChild)
            
    def build(self, arrInputPrioirty, arrInputValue):
        for itr in range(len(arrInputPrioirty)):
            self.arrPriority[itr] = arrInputPrioirty[itr]
            self.arrValue[itr] = arrInputValue[itr]
        self.size = len(arrInputPrioirty)
        for itr in range(self.size-1, -1, -1):
            self.percolateDown(itr)
            
pq = BinaryHeap()
pq.enqueueWithPrioirty('il-chul moon', 1)
pq.enqueueWithPrioirty('taesik lee', 2)
pq.enqueueWithPrioirty('hayong shin', 3)
pq.enqueueWithPrioirty('tae eog lee', 99)

print(pq.dequeueWithPrioirty())
print(pq.dequeueWithPrioirty())
print(pq.dequeueWithPrioirty())
print(pq.dequeueWithPrioirty())

pq2 = BinaryHeap()
pq2.build({0:1, 1:2, 2:3, 3:99},
          {0:'il-chul moon', 1:'taesik lee', 2:'hayong shin', 3:'tae eog lee'})

print(pq2.dequeueWithPrioirty())
print(pq2.dequeueWithPrioirty())
print(pq2.dequeueWithPrioirty())
print(pq2.dequeueWithPrioirty())

