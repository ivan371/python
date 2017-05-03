class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Tree:
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, n, x):
        if n.data is None:
            n.data = x
            n.left = Node(None)
            n.right = Node(None)
            #print("node")
        else:
            #print("insert")
            if x > n.data:
                self.insert(n.right, x)
            else:
                self.insert(n.left, x)

    def add(self, data):   
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert(self.root, data)

    def height(self,node):
        if node==None:
            return 0
        else:
            lheight = self.height(node.left)
        rheight = self.height(node.right)
    
        if lheight > rheight:
            return(lheight+1)
        else:
            return(rheight+1)

    def printnode(self, n):
        if n.data == None:
            return
        else:
            self.printnode(n.left)
            print(n.data, end=" ")
            self.printnode(n.right)

    def print(self):
        self.printnode(self.root)
A = [int(x) for x in input().split()]
tree = Tree()
for x in A:
    tree.add(x)
tree.print()
