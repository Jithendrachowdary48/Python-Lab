#Program Creating Binary tree with single node
class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        print(self.data)
#Input
root = node(10)
#Output
root.PrintTree()
