# Create BST
# Insert 12 Values
# Traverse the tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  
        self.right = None 


class BSTree:
    def __init__(self):
        self.root = None

    #BST insert
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left = Node(data) 
        else:
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right = Node(data) 

    #BST find
    def find(self,data):
        if not self.root:
            return False
        else:
            return self.findNode(data,self.root)

    def findNode(self,data,node):
        if not node:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self.findNode(data,node.left)
        if data > node.data:
            return self.findNode(data,node.right)

    #BST traverse
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.left:
            self.traverseInOrder(node.left)
        print(node.data)
        if node.right:
            self.traverseInOrder(node.right)

    #BST remove
    def remove(self,data):
        if self.root:
            self.removeNode(data,self.root)

    def removeNode(self,data,node):
        if not node:
            return node

        if data < node.data:
            node.left = self.removeNode(data,node.left)
        elif data > node.data:
            node.right = self.removeNode(data,node.right)
        else:
            #check no children case
            if not node.left and not node.right:
                print("removing a leaf node ...")
                del node
                return None

            #remove node with single child
            if not node.left:  #remove node with single right child
                print("removing a node with a single right child ...")
                tempnode = node.right
                del node
                return tempnode
            elif not node.right: #remove node with single ledt child
                print("removing a node with a single left child ...")
                tempnode = node.left
                del node
                return tempnode

            #remove node with two children
            print("removing a node with two children...")
            tempnode = self.getPredecessor(node.left)
            node.data = tempnode.data
            node.left = self.removeNode(tempnode.data, node.left)
        
        return node

    def getPredecessor(self, node):
        if node.right:
            return self.getPredecessor(node.right)
        return node

    #BST get min val
    def getMinVal(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.left:
            return self.getMin(node.left)

        return node.data
    def printVal(self):
        return 0

tree = BSTree()
tree.insert(12)
tree.insert(19)
tree.insert(17)
tree.insert(13)
tree.insert(44)
tree.insert(20)
tree.insert(32)
tree.insert(2)
tree.insert(34)
tree.insert(65)
tree.insert(1)
tree.insert(9)


# second order

tree.insert(9)
tree.insert(12)
tree.insert(1)
tree.insert(19)
tree.insert(65)
tree.insert(17)
tree.insert(34)
tree.insert(13)
tree.insert(2)
tree.insert(44)
tree.insert(32)
tree.insert(20)