dsltools
========

Helpers for creating and traversing recursively nested data structures in Python. Useful for creating simple languages and abstract value domains like type and shape systems. 

Contains:

* *Node*: Base class for building algebraic data types by having each child class declare "\_members = ['x', 'y', 'z']"
* *ScopedDict*: Stack of dictionaries for keeping variable-&gt;value mappings while traversing nested scopes
* *ScopedSet*: Stack of sets for keeping sets of variables while traversing nested scopes
* *NestedBlocks*: Stack of lists for traversing nested scopes of statement sequences
* *dispatch*: calls local functions based on the class name of its argument
