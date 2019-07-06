import unittest
import random
from implementation.algorithms.bst import BST
from implementation.algorithms.node import Node
from implementation.customer import Customer

class TestBST(unittest.TestCase):
    def setUp(self):
        self.tree=BST()
        for i in range(5,10):
            testCustomer=Customer(random.randint(1, 101), "Customer"+i, lat=i, lon=i+1)
            self.tree.insert(testCustomer)
        for i in range(0,5):
            testCustomer=Customer(random.randint(1, 101), "Customer"+i, lat=i, lon=i+1)
            self.tree.insert(testCustomer)

    def test_tree(self):
        treeContents=[]
        treeContents=self.tree.inorder_traversal(self.tree.root)
        self.assertEqual(10, len(treeContents))
        self.assertIsNot(0 , len(treeContents))
        
if __name__ == "__main__":
    unittest.main()
    print("Everything passed")                