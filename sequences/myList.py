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
    
    def __init__(self, typing=None):
        self.typing = typing # if None, lazy (typed upon first insertion)
        self.container = []
        self._size = 0

    @property
    def size(self):
        return self._size # could also just point to len(self.container)

    def insert(self, element, head=False):

        if self.typing is None: # first insertion: set type
            self.typing = type(element)
        else: # check type
            if type(element) != self.typing:
                raise TypeError("Type " + str(type(element)) + " is " + 
                                "incompatible with list of type " + 
                                str(self.typing) + ".")
        # if no error:
        if head:
            self.container.insert(0, element)
        else:
            self.container.append(element)
        self._size += 1

    def remove(self, element):
        if type(element) == self.typing: # don't waste time if bad type
            for e,i in enumerate(self):
                if e == element:
                    self.container = self.container[:i] + self.container[i+1:]
                    self._size -= 1
                    break

    def __iter__(self):
        return (item for item in self.container)

    def __contains__(self, element):
        if type(element) != self.typing:
            return False # faster return with bad types
        else:
            return element in self.container
    
    def __str__(self):
        return "<" + ", ".join(str(x) for x in self.container) + ">"
