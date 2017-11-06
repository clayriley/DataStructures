#!/usr/bin/python
"""
Tests for splay trees
"""

import unittest
import splayTree

class SplayInsertTests(unittest.TestCase):

    #firstTree = ""

    def setUp(self):
        self.root = splayTree.SplayTree(3)
    
    def testInsert(self):
        
        # test that initial node is correctly set up
        self.assertEqual(self.root.value, 3)
        self.assertIsNone(self.root.parent)
        self.assertIsNone(self.root.left)
        self.assertIsNone(self.root.right)
    
        # insert second node and test structure of tree
        self.root = self.root.insert(1)
        self.assertEqual(self.root.value, 1)
        self.assertIsNone(self.root.parent)
        self.assertIsNone(self.root.left)
        self.assertEqual(self.root.right.value, 3)
        self.assertEqual(self.root.right.parent.value, 1)
        self.assertIsNone(self.root.right.right)
        self.assertIsNone(self.root.right.left)
    
        # insert third node and test structure of tree
        self.root = self.root.insert(7)
        self.assertEqual(self.root.value, 7)
        self.assertIsNone(self.root.parent)
        self.assertEqual(self.root.left.value, 3)
        self.assertEqual(self.root.left.parent.value, 7)
        self.assertIsNone(self.root.left.right)
        self.assertEqual(self.root.left.left.value, 1)
        self.assertEqual(self.root.left.left.parent.value, 3)
        self.assertIsNone(self.root.left.left.left)
        self.assertIsNone(self.root.left.left.right)
        

if __name__ == "__main__":
    unittest.main()

