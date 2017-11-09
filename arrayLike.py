#!/usr/bin/python
"""
Class for wrapping array-like structures of variable length.  The underlying 
structure may not be a linear sequence, but the output is.
"""

import splayTree
import myList

class Array():

    def __init__(self):

    def getArray(self):
        raise NotImplementedError

    def add(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError

    def __contains__(self, element):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __str__(self):
        return "["+", ".join(element for element in self.getArray())+"]"


class SplayArray(Array):
    """
    A typed array with a splay tree underlying it.  It is always sorted.
    Most operations are O(n) with amortized O(log n) time.
    """

    def __init__(self, t=None):
        self.root = None
        self.t = None # may delay this and infer upon first addition
        if t is not None:
            if comparable(t):
                self.t = t # the type of the array
            else:
                raise IOError("Type "+str(t)+" is not comparable.")

    def getArray(self):
        return [] if self.root is None else self.root

    def add(self, element):

        # set this object's typing if not previously typed
        if self.t is None:
            self.t = type(element)
        else:
            if type(element) != self.t:
                # TODO allow different yet comparable types 
                raise IOError("Type "+str(t)+" is incompatible with array of " +
                              "type "+self.t+".")
        
        # if successful, add element
        if self.root is None:
            self.root = SplayTree(element)
        else:
            self.root = self.root.insert(SplayTree(element))

    def remove(self, element):

        pass

    def __contains__(self, element):

        self.root = self.root.search(element)

    def __iter__(self):
        return iter(self.a) # already implemented in SplayTree


def comparable(someObject):
    """
    returns whether or not an object is comparable--needed for certain classes
    """
    someClass = type(someObject)
    lessThanIsImplemented = someClass.__lt__ != object.__lt__
    greaterThanIsImplemented = someClass.__gt__ != object.__gt__
    return lessThanIsImplemented or greaterThanIsImplemented

