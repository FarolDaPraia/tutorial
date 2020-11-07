# F-Strings

```python
>>> x = 10
>>> print('The answer is %d today' %10)
The answer is 10 today
>>> print('The answer is {0} today'.format(x))
The answer is 10 today
>>> print('The answer is {x} today'.format(x=x))
The answer is 10 today
>>> print(f'The answer is {x} today')
The answer is 10 today
>>> print(f'The answer is {x :08d} today')
The answer is 00000010 today
>>> print(f'The answer is {x ** 2 :08d} today')
The answer is 00000100 today
```
```python
>>> raise ValueError(f'Expected {x!r} to a float not a {type(x).__name__}')
ValueError: Expected 10 to a float not a int
```
