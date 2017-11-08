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
        self.assertEqual(self.root.right.parent.value, 4)
        self.assertIsNone(self.root.right.left)
        self.assertIsNone(self.root.right.right)

        # insert fifth node and test structure of tree
        self.root = self.root.insert(2) 
        self.assertEqual(self.root.value, 2)
        self.assertIsNone(self.root.parent)
        self.assertEqual(self.root.left.value, 1)
        self.assertEqual(self.root.left.parent.value, 2)
        self.assertIsNone(self.root.left.left)
        self.assertIsNone(self.root.left.right)
        self.assertEqual(self.root.right.value, 4)
        self.assertEqual(self.root.right.parent.value, 2)
        self.assertEqual(self.root.right.left.value, 3)
        self.assertEqual(self.root.right.left.parent.value, 4)
        self.assertIsNone(self.root.right.left.left)
        self.assertIsNone(self.root.right.left.right)
        self.assertEqual(self.root.right.right.value, 7)
        self.assertEqual(self.root.right.right.parent.value, 4)
        self.assertIsNone(self.root.right.right.left)
        self.assertIsNone(self.root.right.right.right)

        # insert sixth node and test structure of tree
        self.root = self.root.insert(6) 
        self.assertEqual(self.root.value, 6)
        self.assertIsNone(self.root.parent)
        self.assertEqual(self.root.left.value, 2)
        self.assertEqual(self.root.left.parent.value, 6)
        self.assertEqual(self.root.left.left.value, 1)
        self.assertEqual(self.root.left.left.parent.value, 2)
        self.assertIsNone(self.root.left.left.left)
        self.assertIsNone(self.root.left.left.right)
        self.assertEqual(self.root.left.right.value, 4)
        self.assertEqual(self.root.left.right.parent.value, 2)
        self.assertEqual(self.root.left.right.left.value, 3)
        self.assertEqual(self.root.left.right.left.parent.value, 4)
        self.assertIsNone(self.root.left.right.left.left)
        self.assertIsNone(self.root.left.right.left.right)
        self.assertIsNone(self.root.left.right.right)
        self.assertEqual(self.root.right.value, 7)
        self.assertEqual(self.root.right.parent.value, 6)
        self.assertIsNone(self.root.right.left)
        self.assertIsNone(self.root.right.right)        

        # insert seventh node and test structure of tree
        self.root = self.root.insert(8) 
        self.assertEqual(self.root.value, 8)
        self.assertIsNone(self.root.parent)
        self.assertEqual(self.root.left.value, 7)
        self.assertEqual(self.root.left.parent.value, 8)
        self.assertEqual(self.root.left.left.value, 6)
        self.assertEqual(self.root.left.left.parent.value, 7)
        self.assertEqual(self.root.left.left.left.value, 2)
        self.assertEqual(self.root.left.left.left.parent.value, 6)
        self.assertEqual(self.root.left.left.left.left.value, 1)
        self.assertEqual(self.root.left.left.left.left.parent.value, 2)
        self.assertIsNone(self.root.left.left.left.left.left)
        self.assertIsNone(self.root.left.left.left.left.right)
        self.assertEqual(self.root.left.left.left.right.value, 4)
        self.assertEqual(self.root.left.left.left.right.parent.value, 2)
        self.assertEqual(self.root.left.left.left.right.left.value, 3)
        self.assertEqual(self.root.left.left.left.right.left.parent.value, 4)
        self.assertIsNone(self.root.left.left.left.right.left.left)
        self.assertIsNone(self.root.left.left.left.right.left.right)
        self.assertIsNone(self.root.left.left.left.right.right)
        self.assertIsNone(self.root.left.left.right)
        self.assertIsNone(self.root.left.right)
        self.assertIsNone(self.root.right)

        # insert eighth node and test structure of tree
        self.root = self.root.insert(5) 
        self.assertEqual(self.root.value, 5)
        self.assertIsNone(self.root.parent)
        self.assertEqual(self.root.left.value, 4)
        self.assertEqual(self.root.left.parent.value, 5)
        self.assertEqual(self.root.left.left.value, 2)
        self.assertEqual(self.root.left.left.parent.value, 4)
        self.assertEqual(self.root.left.left.left.value, 1)
        self.assertEqual(self.root.left.left.left.parent.value, 2)
        self.assertIsNone(self.root.left.left.left.left)
        self.assertIsNone(self.root.left.left.left.right)
        self.assertEqual(self.root.left.left.right.value, 3)
        self.assertEqual(self.root.left.left.right.parent.value, 2)
        self.assertIsNone(self.root.left.left.right.left)
        self.assertIsNone(self.root.left.left.right.right)
        self.assertIsNone(self.root.left.right)
        self.assertEqual(self.root.right.value, 8)
        self.assertEqual(self.root.right.parent.value, 5)
        self.assertEqual(self.root.right.left.value, 6)
        self.assertEqual(self.root.right.left.parent.value, 8)
        self.assertIsNone(self.root.right.left.left)
        self.assertEqual(self.root.right.left.right.value, 7)
        self.assertEqual(self.root.right.left.right.parent.value, 6)
        self.assertIsNone(self.root.right.left.right.left)
        self.assertIsNone(self.root.right.left.right.right)
        self.assertIsNone(self.root.right.right)


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

