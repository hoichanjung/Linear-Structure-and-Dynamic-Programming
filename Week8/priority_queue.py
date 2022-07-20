class Node:
    nodeNext = None
    nodePrev = ""
    objValue = ""
    binHead = False
    binTail = False
    
    def __init__(self, objValue = "", nodeNext = None, binHead = False, binTail = False):
        self.nodeNext = nodeNext
        self.objValue = objValue
        self.binHead = binHead
        self.binTail = binTail
        
    def getValue(self):
        return self.objValue
    def setValue(self, objValue):
        self.objValue = objValue
    def getNext(self):
        return self.nodeNext
    def setNext(self, nodeNext):
        self.nodeNext = nodeNext
    def isHead(self):
        return self.binHead
    def isTail(self):
        return self.binTail
       

class SinglyLinkedList:
    nodeHead = ""
    noideTail =""
    size = 0
    
    def __init__(self):
        self.nodeTail = Node(binTail=True)
        self.nodeHead = Node(binHead=True, nodeNext=self.nodeTail)
        
    def insertAt(self, objInsert, idxInsert):
        nodeNew = Node(objValue = objInsert)
        nodePrev = self.get(idxInsert - 1)
        nodeNext = nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size = self.size + 1
        
    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove-1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        return nodeRemove.getValue()
    
    def get(self, idxRetrieve):
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve + 1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn
    
    def printStatus(self):
        nodeCurrent = self.nodeHead
        while nodeCurrent.getNext().isTail() == False:
            nodeCurrent = nodeCurrent.getNext()
            print(nodeCurrent.getValue(), end=" ")
        print(" ")
        
    def getSize(self):
        return self.size
    
class PriorityNode:
    priority = -1
    value = ''
    
    def __init__(self, value, priority):
        self.priority = priority
        self.value = value
    def getValue(self):
        return self.value
    def getPriority(self):
        return self.priority
    
class PriorityQueue:
    
    list = ''
    
    def __init__(self):
        self.list = SinglyLinkedList()
    
    def enqueueWithPrioirty(self, value, priority):
        idxInsert = 0
        for itr in range(self.list.getSize()):
            node = self.list.get(itr)
            if node.getValue() == '':
                idxInsert = itr
                break
            if node.getValue().getPriority() < priority:
                idxInsert = itr
                break
            else:
                idxInsert = itr + 1
        self.list.insertAt(PriorityNode(value, priority), idxInsert)
        
    def dequeueWithPrioirty(self):
        return self.list.removeAt(0).getValue()
    
pq = PriorityQueue()
pq.enqueueWithPrioirty('il-chul moon', 1)
pq.enqueueWithPrioirty('taesik lee', 2)
pq.enqueueWithPrioirty('hayong shin', 3)
pq.enqueueWithPrioirty('tae eog lee', 99)

print(pq.dequeueWithPrioirty())
print(pq.dequeueWithPrioirty())
print(pq.dequeueWithPrioirty())
print(pq.dequeueWithPrioirty())
