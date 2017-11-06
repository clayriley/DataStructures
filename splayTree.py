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
        n = self._find(value)
        n._splay()
        return n

    def insert(self, value):
        """
        Inserts a new node with the specified value into the tree, which is then 
        splayed around it.
        O(n), amortized O(log n).
        """
        insertion_point = self._find(value)
        n = Splay(value)
        
        # value already in the tree; add at leftmost position in right subtreepa
        if value == insertion_point.value:
            if insertion_point.right is None:
                insertion_point.right = n
                n.parent = insertion_point
            else:
                insertion_point = insertion_point.right
                while insertion_point.left is not None:
                    insertion_point = insertion_point.left
                insertion_point.left = n
                n.parent = insertion_point

        # value belongs to the left
        elif value < insertion_point.value:
            insertion_point.left = n
            n.parent = insertion_point

        # value belongs to the right
        else:
            insertion_point.right = n
            n.parent = insertion_point

    def delete(self, value):
        """
        Searches for the specified value.  If found, splays the tree around it; 
        removes it from the tree; finds its immediate predecessor; splays the 
        left subtree around that node; and attaches it to the right subtree.  If 
        not found, splays the tree around its nearest parent.  Returns the new 
        root.
        O(n), amortized O(log n).
        """
        n = self._find(value)  # find and splay relevant node
        n._splay()

        if n.value == value:  # only if value actually found
            left, right = n._uproot()
            
            # there is a left child: splay around its maximum, connect to right
            if left is not None: 
                while left.right is not None:
                    left = left.right
                left._splay()
                left.right = right
                if right is not None:   
                    right.parent = left
                n = left

            # there is no left child: all we need is the right
            else:
                n = right

        return n  # new root of the entire tree

    def contains(self, value):
        """
        Returns whether or not the specified value exists in this tree.  Does 
        not splay the tree, since it does not return a node.
        O(n), amortized O(log n).
        """
        n = self._find(value)
        return n.value == value

    def _find(self, value):
        """
        Finds the given value in the tree rooted at this tree, or its would-be 
        parent if not found.  Runs in time linear in the height of the tree.  
        Does not splay the tree.

        O(n), amortized O(log n)
        """ 
        # case 1: look deeper, left
        if self.value > value and self.left is not None:
            return self.left._find(value)

        # case 2: look deeper, right
        if self.value < value and self.right is not None:
            return self.right._find(value)

        # case 3: found it, or nothing to find
        else:
            return self

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
        """
        Detaches the root node from its children and returns them.
        O(1)
        """
        left, right = this.left, this.right
        if left is not None:
            left.parent = None
        if right is not None:
            right.parent = None
        return left, right

    def _successor(self):
        """
        Gets the successor to this node.  Useful for making an inorder 
        traversal, e.g. to print as sorted.
        """
        if self.right is None:
            # get first rightward ancestor
            m = self
            n = m.parent
            while n is not None and m is n.right:
                m = n
                n = n.parent
        else:
            # get leftmost of right child
            n = self.right
            while n.left is not None:
                n = n.left
        return n
