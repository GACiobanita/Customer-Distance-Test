import unittest
import random
from implementation.algorithms.bst import BST
from implementation.algorithms.node import Node
from implementation.customer import Customer

class TestBST(unittest.TestCase):
    def set_up(self):
        self.tree=BST()
        for i in range(5,10):
            test_customer=Customer(random.randint(1, 101), "Customer"+i, lat=i, lon=i+1)
            self.tree.insert(test_customer)
        for i in range(0,5):
            test_customer=Customer(random.randint(1, 101), "Customer"+i, lat=i, lon=i+1)
            self.tree.insert(test_customer)

    def test_tree(self):
        tree_contents=[]
        tree_contents=self.tree.inorder_traversal(self.tree.root)
        self.assertEqual(10, len(tree_contents))
        self.assertIsNot(0 , len(tree_contents))
        
if __name__ == "__main__":
    unittest.main()
    print("Everything passed")                