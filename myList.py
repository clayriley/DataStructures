#!/usr/bin/python
"""
Wrappers for the Python list.
"""

class List():
    
    def __init__(self):
        self.container = []
        self._size = 0

    @property
    def size(self):
        return self._size # could also just point to len(self.container)

    def insert(self, element, head=False):
        if head:
            self.container.insert(0, element)
        else:
            self.container.append(element)
        self._size += 1

    def remove(self, element):
        for e,i in enumerate(self):
            if e == element:
                self.container = self.container[:i] + self.container[i+1:]
                self._size -= 1
                break

    def __iter__(self):
        return (item for item in self.container)

    def __contains__(self, element):
        return element in self.container
    
    def __str__(self):
        return "<" + ", ".join(self.container) + ">"


class TypedList():
    
    def __init__(self, t=None):
        if t is not None:
            self.t = t
        self.container = []

    def insert(self, element):
        pass
