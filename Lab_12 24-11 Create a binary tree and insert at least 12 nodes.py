#Program creating binary tree and inserting nodes
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()
#Inputs
root = Node(10)
root.insert(20)
root.insert(30)
root.insert(40)
root.insert(50)
root.insert(60)
root.insert(70)
root.insert(80)
root.insert(90)
root.insert(100)
#Outputs
root.PrintTree()
