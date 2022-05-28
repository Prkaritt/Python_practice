class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                
        else:
            self.data = data
    
    def printTree(self):
        print (self.data)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

root = Node(10)
root.insert(5)
root.insert(15)
root.insert(4)
root.insert(6)
root.insert(11)
root.insert(16)
root.printTree()