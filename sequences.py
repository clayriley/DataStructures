#!/usr/bin/python
"""
Class for wrapping sequences of variable length.  The underlying structure may 
not be a linear sequence, but representations are.
"""

import abc
import splayTree as splay
import myList

class Sequence(abc.ABC):

    @abc.abstractmethod
    def add(self):
        """note that behavior will vary by implementation."""
        raise NotImplementedError 

    @abc.abstractmethod
    def remove(self):
        raise NotImplementedError

    @abc.abstractmethod
    def size(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __contains__(self, element):
        raise NotImplementedError

    @abc.abstractmethod
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
        self.tree = splay.SplayTree(typing)

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
        return self.tree.size # implemented as property

    def __contains__(self, element):
        return self.tree.contains(element)

    def __iter__(self):
        return iter(self.tree)



