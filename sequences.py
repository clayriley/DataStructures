#!/usr/bin/python
"""
Class for wrapping sequences of variable length.  The underlying structure may 
not be a linear sequence, but representations are.
"""

import splayTree as splay
import myList

class Sequence():

    def add(self):
        """note that behavior will vary by implementation."""
        raise NotImplementedError 

    def remove(self):
        raise NotImplementedError

    @property
    def size(self):
        """should be implemented as a property."""
        raise NotImplementedError       

    def __contains__(self, element):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __str__(self): # relies on __iter__ implementation
        return "["+", ".join(str(element) for element in self)+"]"


class SplaySequence(Sequence):
    """
    A typed sequence with a splay tree underlying it.  It is always sorted.
    Most operations are O(n) with amortized O(log n) time.
    """

    def __init__(self, typing=None):
        self._tree = splay.SplayTree(typing)

    @property
    def tree(self):
        return self._tree

    def add(self, element):
        """
        Add item to the sequence.  Automatically place it in sorted position.
        """
        self.tree.insert(element)

    def remove(self, element):
        """
        Removes one instance of the given element from the sequence.
        """
        self.tree.delete(element)

    def size(self):
        return self.tree.size

    def __contains__(self, element):
        return self.tree.contains(element)

    def __iter__(self):
        return iter(self.tree)



