# special methods (dunder)

https://docs.python.org/3/reference/datamodel.html#special-method-names

### Python Coding Problem: Creating Your Own Iterators - Corey Schaefer
https://www.youtube.com/watch?v=C3Z9lJXI6Qw

+ Technically, any Python object that implements the .__iter__() or .__getitem__() methods is iterable.
The iter() built-in function, when called on an iterable, returns an iterator object for that iterable:
```python
>>> iter([1, 2, 3, 4])
<list_iterator object at 0x7fa80af0d898>
```
