#!/usr/bin/python
"""
Tests for splay trees
"""

import unittest
import splayTree

class SplayInsertTests(unittest.TestCase):

    def setUp(self):
        self.root = splayTree.SplayTree(3)
        print("\nTesting method:", self._testMethodName[5:] + "...")
    
    def test_insert(self):
        """testing insertion"""
        
        # test that initial node is correctly set up
        self.assertEqual(self.root.value, 3)
        self.assertIsNone(self.root.parent)
        self.assertIsNone(self.root.left)
        self.assertIsNone(self.root.right)
    
        # insert second node and test structure of tree
        # (implicitly tests find case: element not found)
        # (implicitly tests splay case: zig CW)
        self.root = self.root.insert(1)
        self.assertEqual(self.root.value, 1)
        self.assertIsNone(self.root.parent)
        self.assertIsNone(self.root.left)
        self.assertEqual(self.root.right.value, 3)
        self.assertEqual(self.root.right.parent.value, 1)
        self.assertIsNone(self.root.right.left)
        self.assertIsNone(self.root.right.right)
    
        # insert third node and test structure of tree
        # (implicitly tests find case: element not found)
        # (implicitly tests splay case: zigzig CCW)
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
        # (implicitly tests find case: element not found)
        # (implicitly tests splay case: zigzag CCW-CW)
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
        # (implicitly tests find case: element not found)
        # (implicitly tests splay case: zigzag-zig CCW+CW-CW)
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
        # (implicitly tests find case: element not found)
        # (implicitly tests splay case: zigzag-zig CW+CCW-CCW)
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
        # (implicitly tests find case: element not found)
        # (implicitly tests splay case: zigzig CCW)
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
        # (implicitly tests find case: element not found)
        # (implicitly tests splay case: zigzig-zigzig-zig CCW-CW-CW)
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

        # test insertion failure
        # (implicitly tests find case: tree datatype error) 
        self.assertRaises(TypeError,self.root.insert, "1")


    def test___str__(self):
        """testing string printing"""
        
        # test setup root
        self.assertEqual(str(self.root), "(3)")

        # insert and test
        self.root = self.root.insert(1)
        self.assertEqual(str(self.root), "(1(3))")
        self.root = self.root.insert(7)
        self.assertEqual(str(self.root), "(((1)3)7)")
        self.root = self.root.insert(4)
        self.assertEqual(str(self.root), "(((1)3)4(7))")
        self.root = self.root.insert(2)
        self.assertEqual(str(self.root), "((1)2((3)4(7)))")
        self.root = self.root.insert(6)
        self.assertEqual(str(self.root), "(((1)2((3)4))6(7))")
        self.root = self.root.insert(8)
        self.assertEqual(str(self.root), "(((((1)2((3)4))6)7)8)")
        self.root = self.root.insert(5)
        self.assertEqual(str(self.root), "((((1)2(3))4)5((6(7))8))")

        # search and test
        self.root = self.root.search(1)
        self.assertEqual(str(self.root), "(1((2((3)4))5((6(7))8)))")

        # delete and test
        self.root = self.root.delete(6)        
        self.assertEqual(str(self.root), "((1(2((3)4)))5((7)8))")

    # assuming both insertion and str pass:
    # we can use str from here on out as a shorthand.

    def test_delete(self):
        """test deletion"""

        # test setup root
        self.assertEqual(str(self.root), "(3)")
        
        # delete only node
        # (implicitly tests find case: element found)
        # (implicitly tests splay case: already root)
        deleted = self.root.delete(3)
        self.assertIsNone(deleted)

        # delete deeper node
        # (implicitly tests find case: element found)
        # (implicitly tests splay case: zigzag-zig CW+CCW-CCW)
        # (implicitly tests splay case: zig CCW)
        self.root = self.root.insert(1)
        self.root = self.root.insert(7)
        self.root = self.root.insert(4)
        self.root = self.root.insert(2)
        self.root = self.root.insert(6)
        self.root = self.root.insert(8)
        self.root = self.root.insert(5)
        self.root = self.root.search(1)
        self.root = self.root.delete(6)        
        self.assertEqual(str(self.root), "((1(2((3)4)))5((7)8))")

        # deletion failures
        # (implicitly tests find case: tree data type error)
        # (implicitly tests find case: element not found)
        # (implicitly tests splay case: zigzag CW+CCW)
        self.assertRaises(TypeError, self.root.delete, "1")
        self.root = self.root.delete(6)
        self.assertEqual(str(self.root), "(((1(2((3)4)))5)7(8))")
        
        
    def test_search(self):
        """searching tests"""

        # test setup root
        self.assertEqual(self.root.value, 3)

        # search for root
        # (implicitly tests find case: element found)
        # (implicitly tests splay case: already root)
        self.root = self.root.search(3)
        self.assertEqual(self.root.value, 3)

        # search deeper
        # (implicitly tests find case: element found)
        # (implicitly tests splay case: zigzig-zig CW+CW-CW)
        self.root = self.root.insert(1)
        self.root = self.root.insert(7)
        self.root = self.root.insert(4)
        self.root = self.root.insert(2)
        self.root = self.root.insert(6)
        self.root = self.root.insert(8)
        self.root = self.root.insert(5)
        self.root = self.root.search(1)
        self.assertEqual(self.root.value, 1)
        self.assertEqual(str(self.root), "(1((2((3)4))5((6(7))8)))")

        # search failure
        # (implicitly tests find case: element not found)
        # (implicitly tests splay case: zigzig CCW+CCW)
        self.root = self.root.search(10)
        self.assertEqual(self.root.value, 8)
        self.assertEqual(str(self.root), "(((1(2((3)4)))5(6(7)))8)")
        self.assertRaises(TypeError, self.root.search, "1")

    def test_contains(self):
        """containment searches"""
        
        # test setup root
        self.assertEqual(self.root.value, 3)
        self.assertTrue(self.root.contains(3)) # returns a bool, so no splaying
        self.assertEqual(self.root.value, 3)
        self.assertFalse(self.root.contains(2))
        self.assertEqual(self.root.value, 3)

        # test more complex tree
        self.root = self.root.insert(1)
        self.root = self.root.insert(7)
        self.root = self.root.insert(4)
        self.root = self.root.insert(2)
        self.root = self.root.insert(6)
        self.root = self.root.insert(8)
        self.root = self.root.insert(5)
        self.root = self.root.search(1)
        self.root = self.root.delete(6)
        self.assertTrue(self.root.contains(5))
        self.assertEqual(str(self.root), "((1(2((3)4)))5((7)8))")
        self.assertTrue(self.root.contains(2))
        self.assertEqual(str(self.root), "((1(2((3)4)))5((7)8))")
        self.assertFalse(self.root.contains(6))
        self.assertEqual(str(self.root), "((1(2((3)4)))5((7)8))")
        self.assertFalse(self.root.contains(100))
        self.assertEqual(str(self.root), "((1(2((3)4)))5((7)8))")

        # containment failure
        self.assertRaises(TypeError, self.root.contains, "1")
        self.assertEqual(str(self.root), "((1(2((3)4)))5((7)8))")

    def test_getRoot(self):

        # test setup root
        self.assertEqual(self.root.value, 3)
        self.root = self.root.getRoot()
        self.assertEqual(self.root.value, 3)
        self.root = self.root.insert(1)
        self.root = self.root.insert(7)
        self.root = self.root.insert(4)
        self.root = self.root.insert(2)
        self.root = self.root.insert(6)
        self.root = self.root.insert(8)
        self.root = self.root.insert(5)
        self.root.search(1) # without storing returned node!
        self.assertEqual(str(self.root), "((2((3)4))5((6(7))8))")
        self.root = self.root.getRoot()
        self.assertEqual(str(self.root), "(1((2((3)4))5((6(7))8)))")
        
    def test___iter__(self):  
        self.root = self.root.insert(1)
        self.root = self.root.insert(7)
        self.root = self.root.insert(4)
        self.root = self.root.insert(2)
        self.root = self.root.insert(6)
        self.root = self.root.insert(8)
        self.root = self.root.insert(5)
        asList = list(self.root)
        for i in range(len(asList)):
            self.assertEqual(asList[i], [1, 2, 3, 4, 5, 6, 7, 8][i])

if __name__ == "__main__":
    unittest.main()

