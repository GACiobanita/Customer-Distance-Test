import unittest
from implementation.algorithms.node import Node
from implementation.customer import Customer


class TestNode(unittest.TestCase):

    def setUp(self):
        test_customer = Customer(65, 'George', 53.6, 7.0)
        self.test_node = Node(test_customer)

    def test_nodes_valid(self):
        test_customer = Customer(65, 'George', 53.6, 7.0)
        self.assertEquals(test_customer, self.test_node.customer)

    def test_nodes_invalid(self):
        test_customer = Customer(65, 'Beorge', 53.6, 7.0)
        self.assertEquals(test_customer, self.test_node.customer)

    def test_children(self):
        test_customer1 = Customer(66, 'Dude', 53.6, 7.0)
        test_customer2 = Customer(67, 'Dudette', 53.6, 7.0)
        self.test_node.left_child = Node(test_customer1)
        self.test_node.right_child = Node(test_customer2)
        self.assertIsNotNone(self.test_node.left_child)
        self.assertIsNotNone(self.test_node.right_child)
        self.assertIsNot(self.test_node.left_child, self.test_node.right_child)
