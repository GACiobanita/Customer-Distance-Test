from implementation.customer import Customer

#Nodes used by the BST algorithm
#Each node has its own Customer data and a reference to its child nodes
class Node(object):

    def __init__(self, cust):
        self.customer = cust
        self.val = self.customer.id
        self.left_child = None
        self.right_child = None

    def get(self):
        return self.val

    def get_children(self):
        children = []
        if (self.left_child != None):
            children.append(self.left_child)
        if (self.right_child != None):
            children.append(self.right_child)
        return children
