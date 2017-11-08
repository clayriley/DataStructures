# DataStructures
Various data structure implementations.

## Splay Tree
A binary search tree that performs a "splay" operation on the tree at every insertion, deletion, and search.  This operation rotates the node visited at the end of each of these calls to the top of the tree in a way that draws frequently-accessed nodes and their neighbors in the value space upward in the tree, leading to an amortized O(log n) runtime for most operations.

Implementation: Python 3
