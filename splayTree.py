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
        pass

    def insert(self, value):
        n = Splay(value)
        pass

    def delete(self, value):
        pass

    def contains(self, value):
        pass

    def _find(self, value):
        pass

    def _splay(self):
        pass
    
    def _zig(self):
        pass

    def _rotateClockwise(self):
        pass
    
    def _rotateCounterclockwise(self):
        pass

    def _uproot(self):
        pass
