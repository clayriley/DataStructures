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
        self.assertIsNone(self.root.right.left)
        self.assertIsNone(self.root.right.right)
    
        # insert third node and test structure of tree
        self.root = self.root.insert(7)
        self.assertEqual(self.root.value, 7)
        self.assertIsNone(self.root.parent)
        self.assertEqual(self.root.left.value, 3)
        self.assertEqual(self.root.left.parent.value, 7)
        self.assertEqual(self.root.left.left.value, 1)
        self.assertEqual(self.root.left.left.parent.value, 3)
        self.assertIsNone(self.root.left.left.left)
        self.assertIsNone(self.root.left.left.right)
        self.assertIsNone(self.root.left.right)
        self.assertIsNone(self.root.right)

        # insert fourth node and test structure of tree
        self.root = self.root.insert(4) 
        self.assertEqual(self.root.value, 4)
        self.assertIsNone(self.root.parent)
        self.assertEqual(self.root.left.value, 3)
        self.assertEqual(self.root.left.parent.value, 4)
        self.assertEqual(self.root.left.left.value, 1)
        self.assertEqual(self.root.left.left.parent.value, 3)
        self.assertIsNone(self.root.left.left.left)
        self.assertIsNone(self.root.left.left.right)
        self.assertIsNone(self.root.left.right)
        self.assertEqual(self.root.right.value, 7)
        self.assertEqual(self.root.right.parent.value, 3)
        self.assertIsNone(self.root.right.left)
        self.assertIsNone(self.root.right.right)

        # insert fifth node and test structure of tree
        # insert sixth node and test structure of tree
        # insert seventh node and test structure of tree
        # insert eighth node and test structure of tree

    #def testDelete(self):
    #def testSearch(self):
    #def testContains(self):
    #def testGetRoot(self):
    #def testStr(self):
    #def testIter(self):
    #def testZig(self):
    #def testFind(self):
        

if __name__ == "__main__":
    unittest.main()

