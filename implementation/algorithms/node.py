from implementation.customer import Customer

class Node(object):

    def __init__(self, cust):
        self.customer = cust
        self.val = self.customer.id
        self.leftChild = None
        self.rightChild = None
    
    def get(self):
        return self.val
    
    def getChildren(self):
        children = []
        if(self.leftChild != None):
            children.append(self.leftChild)
        if(self.rightChild != None):
            children.append(self.rightChild)
        return children      