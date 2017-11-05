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
        """
        Splay the tree around the node until it is the root.  
        O(n), amortized O(log n)
        """

        if self.parent is not None: # case 1: already the root -> do nothing
            grandparent = self.parent.parent

            if grandparent is None: # case 2: one rotation to root
                self._zig()

            else: # case 3: multiple rotations to root
                rightOfLeft = self.parent.right is self and grandparent.left is self.parent
                leftOfRight = self.parent.left is self and grandparent.right is self.parent

                if rightOfLeft or leftOfRight: # case 3a: zigzag
                    self.zig()
                    self.zig()

                else: # case 3b: zigzig
                    self.parent.zig()
                    self.zig()

                self._splay() # recur until case 1 or 2 applies
    
    def _zig(self):
        """
        Perform one zig (or zag) operation to rotate the node upward.
        O(1)
        """
        if self.parent is not None:
            if self is self.parent.left:
                self._rotateClockwise()
            elif self is self.parent.right:
                self._rotateCounterClockwise()

    def _rotateClockwise(self):
        """
        Perform one AVL-style rotation clockwise.  Requires a rightward parent.
        O(1)
        """
        p, g, r = self.parent, self.parent.parent, self.right

        # connect right child to parent
        if r is not None:
            r.parent = p
        p.left = r
        
        # move parent down + right
        p.parent = self
        self.right = p

        # move this node up + right
        self.parent = g
        if g is not None:
            if p is g.left:
                g.left = self
            elif p is g.right:
                g.right = self
    
    def _rotateCounterclockwise(self):
        """
        Perform one AVL-style rotation counterclockwise.  Requires a leftward parent.
        O(1)
        """
        p, g, l = self.parent, self.parent.parent, self.left

        # connect left child to parent
        if l is not None:
            l.parent = p
        p.right = l
        
        # move parent down + left
        p.parent = self
        self.left = p

        # move this node up + left
        self.parent = g
        if g is not None:
            if p is g.left:
                g.left = self
            elif p is g.right:
                g.right = self

    def _uproot(self):
        pass
