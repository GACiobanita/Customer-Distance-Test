import unittest
from Node import Node
from Customer import Customer

class TestNode(unittest.TestCase):

    def setUp(self):
        testCustomer = Customer(65, 'George', 53.6, 7.0)
        self.testNode = Node(testCustomer)

    def test_node(self):
        testCustomer = Customer(65, 'George', 53.6, 7.0)
        self.assertEquals(testCustomer, self.testNode.customer) 
    
    def test_children(self):
        testCustomer1 = Customer(66, 'Dude', 53.6, 7.0)
        testCustomer2 = Customer(67, 'Dudette', 53.6, 7.0)
        self.testNode.leftChild = Node(testCustomer1)
        self.testNode.rightChild = Node(testCustomer2)
        self.assertIsNotNone(self.testNode.leftChild)
        self.assertIsNotNone(self.testNode.rightChild)
        self.assertIsNot(self.testNode.leftChild, self.testNode.rightChild)

