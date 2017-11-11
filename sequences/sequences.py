#!/usr/bin/python
"""
Class for wrapping sequences of variable length.  The underlying structure may 
not be a linear sequence, but representations are.
"""

import abc
from .splayTree import *
from .myList import *

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
        return "[ "+" - ".join(str(element) for element in self)+" ]"


class SplaySequence(Sequence):
    """
    A typed sequence with a splay tree underlying it.  It is always sorted.
    Most operations are O(n) with amortized O(log n) time.
    """

    def __init__(self, typing=None):
        self.tree = SplayTree(typing)

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


class ListSequence(Sequence):
    """
    An untyped sequence with a list (wrapper) underlying it.
    """

    def __init__(self):
        self.sequence = List()

    def add(self, element):
        self.sequence.insert(element)

    def remove(self, element):
        self.sequence.remove(element)
    
    def size(self):
        return self.sequence.size

    def __contains__(self, element):
        return element in self.sequence

    def __iter__(self):
        return (item for item in self.sequence)

class TypedListSequence(ListSequence):
    """
    A typed sequence with a wrapper for a list under the hood.
    """

    def __init__(self):
        self.sequence = TypedList()
