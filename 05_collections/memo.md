# Collections — Container datatypes
https://docs.python.org/3.8/library/collections.html#ordereddict-examples-and-recipes

## Counter
```python
>>> from collections import Counter
```    
+ traditional dictionary by missing key returns a KeyError.
```python
>>> d = {}
>>> d['dragons']
KeyError: 'dragons'
```
+ improvement the dictionary, same behavior as a dictionary
```python
>>> d = Counter()
>>> d['dragons']
0
>>> d['dragons'] += 1
Counter({'dragons' : 1})
```
+ pass list object and count
```python
>>> Counter('red green red blue red blue green'.split())
Counter({'red': 3, 'green': 2, 'blue': 2})
>>> c = Counter('red green red blue red blue green'.split())
>>> c.most_common(1)
[('red', 3)]
>>> c.most_common(2)
[('red', 3), ('green', 2)]
# multiset, element grouped together. doesn´t remember order but multiplicity
>>> list(c.elements())
['red', 'red', 'red', 'green', 'green', 'blue', 'blue']
# if works like dictionary, you can get the keys
>>> list(c)
# ask of the values of the dictionary
>>> list(c.values())
# ask of the key value pair
>>> list(c.items())
```
