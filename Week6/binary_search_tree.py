import sys
sys.path.insert(0, 'C:/Users/danie/Desktop/Jung/Linear_Structure_and_Dynamic_Programming/Week3/')
from queue_ import Queue

class TreeNode:
    nodeLHS = None
    nodeRHS = None
    nodeParent = None
    value = None
    
    def __init__(self, value, nodeParent):
        self.value = value
        self.nodeParent = nodeParent
        
    def getLHS(self):
        return self.nodeLHS
    
    def getRHS(self):
        return self.nodeRHS
    
    def getValue(self):
        return self.value
    
    def getParent(self):
        return self.nodeParent
    
    def setLHS(self,LHS):
        self.nodeLHS = LHS
        
    def setRHS(self, RHS):
        self.nodeRHS = RHS
        
    def setValue(self, value):
        self.value = value
        
    def setParent(self, nodeParent):
        self.nodeParent = nodeParent
            
class BinarySearchTree:
    root = None
    
    def __init__(self):
        pass
    
    def insert(self, value, node = None):
        if node is None:
            node = self.root
            
        if self.root is None:
            self.root = TreeNode(value, None)
            return
        
        if value == node.getValue():
            return
        
        if value > node.getValue():
            if node.getRHS() is None:
                node.setRHS(TreeNode(value, node))
            else:
                self.insert(value, node.getRHS())
        
        if value < node.getValue():
            if node.getLHS() is None:
                node.setLHS(TreeNode(value, node))
            else:
                self.insert(value, node.getLHS())
                
        return
    
    def search(self, value, node = None):
        if node is None:
            node = self.root
        if value == node.getValue():
            return True
        if value > node.getValue():
            if node.getRHS is None:
                return False
            else:
                return self.search(value, node.getRHS())
        if value < node.getValue():
            if node.getLHS is None:
                return False
            else:
                return self.search(value, node.getLHS())
            
        
    def delete(self, value, node = None):
        if node is None:
            node = self.root
        if node.getValue() < value:
            return self.delete(value, node.getRHS())
        if node.getValue() > value:
            return self.delete(value, node.getLHS())
        if node.getValue() == value:
            if node.getLHS is not None and node.getRHS() is not None:
                nodeMin = self.findMin(node.getRHS())
                node.setValue(nodeMin.getValue())
                self.delete(nodeMin.getValue(), node.getRHS())
                return
            parent = node.getParent()
            if node.getLHS() is not None:
                if node == self.root:
                    self.root = node.getLHS()
                elif parent.getLHS() == node:
                    parent.setLHS(node.getLHS())
                    node.getLHS().setParent(parent)
                else:
                    parent.setRMS(node.getRMS())
                    node.getRMS().setParent(parent)
                return
            if node == self.root:
                self.root = None
            elif parent.getLHS() == node:
                parent.setLHS(None)
            else:
                parent.setRHS(None)
            return
    
    def findMax(self, node = None):
        if node is None:
            node = self.root
        if node.getRHS() is None:
            return node
        return self.findMax(node.getRHS())
    
    def findMin(self, node=None):
        if node is None:
            node = self.root
        if node.getLHS() is None:
            return node
        return self.findMax(node.getLHS())
    
    def traverseLevelOrder(self):
        ret = []
        Q = Queue()
        Q.enqueue(self.root)
        while not Q.isEmpty():
            node = Q.dequeue()
            if node is None:
                continue
            ret.append(node.getValue())
            if node.getLHS() is not None:
                Q.enqueue(node.getLHS())
            if node.getRHS() is not None:
                Q.enqueue(node.getRHS())
        return ret

    def traverseInOrder(self, node = None):
        if node is None:
            node = self.root
        ret = []
        if node.getLHS() is not None:
            ret = ret + self.traverseInOrder(node.getLHS())
        ret.append(node.getValue())
        if node.getRHS() is not None:
            ret = ret + self.traverseInOrder(node.getRHS())
        return ret
    
    def traversePreOrder(self, node = None):
        if node is None:
            node = self.root
        ret = []
        ret.append(node.getValue())
        if node.getLHS() is not None:
            ret = ret + self.traversePreOrder(node.getLHS())
        if node.getRHS() is not None:
            ret = ret + self.traversePreOrder(node.getRHS())
        return ret
    
    def traversePostOrder(self, node = None):
        if node is None:
            node = self.root
        ret = []
        if node.getLHS() is not None:
            ret = ret + self.traversePostOrder(node.getLHS())
        if node.getRHS() is not None:
            ret = ret + self.traversePostOrder(node.getRHS())
        ret.append(node.getValue())
        return ret
    
tree = BinarySearchTree()
tree.insert(3)
tree.insert(2)
tree.insert(0)
tree.insert(5)
tree.insert(7)
tree.insert(4)
tree.insert(6)
tree.insert(1)
tree.insert(9)
tree.insert(8)

print(tree.traverseLevelOrder())
print(tree.traverseInOrder())
print(tree.traversePreOrder())
print(tree.traversePostOrder())

tree.delete(5)
print(tree.traverseLevelOrder())

tree.delete(1)
print(tree.traverseLevelOrder())

tree.delete(9)
print(tree.traverseLevelOrder())

tree.delete(3)
print(tree.traverseLevelOrder())
