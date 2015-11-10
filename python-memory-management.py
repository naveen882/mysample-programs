"""

How are variables and memory managed in Python.
Automagically! No, really, you just create an object and the Python Virtual Machine handles the memory needed and where it shall be placed in the memory layout.

Does it have a stack and a heap and what algorithm is used to manage memory?
When we are talking about CPython it uses a private heap for storing objects. From the official Python documentation:

Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager. The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching.
The algorithm used for garbage collecting is called Reference counting. That is the Python VM keeps an internal journal of how many references refer to an object, and automatically garbage collects it when there are no more references refering to it.

NOTE: Please keep in mind that this information is CPython specific. Other python implementations, such as pypy, iron python, jython and others may differ from one another and from CPython when it comes to their implementation specifics. To understand that better, it may help to understand that there is a difference between Python the semantics (the language) and the underlying implementation

Given this knowledge are there any recommendations on memory management for large number/data crunching?
Now I can not speak about this, but I am sure that NumPy (the most popular python library for number crunching) has mechanisms that handle memory consumption gracefully.

If you would like to know more about Python's Internals take a look at these resources:

Stepping through CPython (video)
A presentation about the internals of the Python Virtual Machine
In true hacker spirit, the Python Object Allocator source code

http://stackoverflow.com/questions/14546178/does-python-have-a-stack-heap-and-how-is-memory-managed

"""
