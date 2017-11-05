#!/usr/bin/python
"""
Implementation of a splay tree.  Splay trees are binary search trees which are 
"splayed" around the most recently-accessed node, an operation that raises it to 
the root.  Frequently-accessed nodes rise to the top of the tree over time, and 
the specific splay algorithm also ensures that they bring their neighborhood of 
node values upward somewhat as well.  Because of this, insertion, deletion, and 
search all are O(n) operations; but they are amortized O(log n).
"""

class SplayTree():

    def __init__(self, value):
        this.value = value
        this.parent = None
        this.left = None
        this.right = None

    def search(self, value):
        return self._find(value)

    def insert(self, value):
        n = Splay(value)
        pass

    def delete(self, value):
        pass

    def contains(self, value):
        """
        Returns whether or not the specified value exists in this tree.  Does 
        not splay the tree, since it does not return a node.
        O(n), amortized O(log n).
        """
        n = self._find(value)
        return n.value == value

    def _find(self, value):
        pass

    def _splay(self):

        # case 1: already the root -> do nothing
        if self.parent is not None:
            grandparent = self.parent.parent

            # case 2: one rotation to root
            if grandparent is None:
                self._zig()

            else: # case 3: multiple rotations to root
                rightOfLeft = self.parent.right is self and grandparent.left is self.parent
                leftOfRight = self.parent.left is self and grandparent.right is self.parent

                # case 3a: zigzag
                if rightOfLeft or leftOfRight:
                    self.zig()
                    self.zig()

                # case 3b: zigzig
                else:
                    self.parent.zig()
                    self.zig()
                self._splay() # recur
    
    def _zig(self):
        pass

    def _rotateClockwise(self):
        pass
    
    def _rotateCounterclockwise(self):
        pass

    def _uproot(self):
        pass
