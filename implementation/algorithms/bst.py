from .node import Node
from implementation.customer import Customer

#Implementation of a Binary Search Tree for fast addition and lookup of Customers
#Each node in the BST holds its own Customer data, based on Customer id
#Customer ID is used to structure the nodes in the tree, we use the classic version
#with smaller nodes on the left side of the root node and larger nods on the right side
class BST:
    def __init__(self):
        self.root = None
        self.nodeCount = 0

    def insert(self, cust):
        if self.root is None:
            self.root = Node(cust)
        else:
            self.insert_node(self.root, cust)
        self.nodeCount += 1

    def insert_node(self, current_node, cust):
        if cust.id < current_node.val:
            if current_node.left_child:
                self.insert_node(current_node.left_child, cust)
            else:
                current_node.left_child = Node(cust)
        elif cust.id > current_node.val:
            if current_node.right_child:
                self.insert_node(current_node.right_child, cust)
            else:
                current_node.right_child = Node(cust)

    #Display all the nodes in the BST, in ascending order of their ID
    def inorder_traversal(self, node):
        customer_list = []
        if node:
            customer_list = self.inorder_traversal(node.left_child)
            customer_list.append(node.customer)
            customer_list = customer_list + self.inorder_traversal(node.right_child)
        return customer_list
