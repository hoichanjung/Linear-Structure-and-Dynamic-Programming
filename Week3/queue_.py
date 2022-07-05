from singly_linked_list import SinglyLinkedList

class Queue:
    lstInstance = SinglyLinkedList()
    
    def dequeue(self):
        return self.lstInstance.removeAt(0)
    
    def enqueue(self, value):
        self.lstInstance.insertAt(value, self.lstInstance.getSize())
        

queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())