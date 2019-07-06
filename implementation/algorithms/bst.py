from .node import Node
from implementation.customer import Customer

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, cust):
        if(self.root is None):
            self.root = Node(cust)
        else:
            self.insertNode(self.root, cust)
    
    def insertNode(self, currentNode, cust):
        if (cust.id < currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.left, cust)
            else:
                currentNode.leftChild = Node(cust)
        elif (cust.id > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, cust)
            else:
                currentNode.rightChild = Node(cust)
    
    def inorder_traversal(self, node):
        customerList = []
        if node:
            customerList = self.inorder_traversal(node.left)
            customerList.append(node.customer)
            customerList = customerList + self.inorder_traversal(node.right)
        return customerList
