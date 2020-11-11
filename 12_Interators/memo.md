# Iterators and Iterables
--> Python Tutorial: Iterators and Iterables - What Are They and How Do They Work?
https://www.youtube.com/watch?v=jTYiNjvnHZY

a list is interable but it is not a interator.

+ interable means that something can be looped over
```python
>>> nums = [1, 2, 3]
>>>
>>> for num in mums:
>>>     print(num)
```
you can looped over a object, if the object has a iter method \__iter__
```python
>>> nums = [1, 2, 3]
>>>
>>> print(dir(num))
```
+ iterator is an object with a state, so remember whre it is during a iteration. For this a next method is required \__next__
List is withou a next method implementation
```python
>>> nums = [1, 2, 3]
>>> # i_nums = nums.__iter__() # very ugly
>>> i_nums = iter(nums)
>>> print(dir(i_nums))
>>> print(next(i_nums))
1
```
```python
>>> nums = [1, 2, 3]
>>> i_nums = iter(nums)
>>> while True:
>>>   try:
>>>     item = next(i_nums)
>>>     print(item)
>>>   except StopIteration:
>>>     break
```
When the first element, 1, is taken from the “first” iterator, the “second” iterator now starts at 2 since it is just a reference to the “first” iterator and has therefore been advanced one step.
```python
>>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> iters = [iter(nums)] * 2
>>> list(id(itr) for itr in iters)  # IDs are the same.
[139949748267160, 139949748267160]
```

+ Implementation a iterator over a class
```python
class MyRange:

  def __init__(self, start, stop):
    self.value = start
    self.end = end

  def __iter__(self):
    return self

  def __next__(self):
    if self.value >= self.end:
      raise StopIteration
    current = self.value
    self.value += 1
    return current
nums = MyRange(1, 10)
for num in nums:
  print(num)
```
"Returning self from a method simply means that your method returns a reference to the instance object on which it was called. "
https://stackoverflow.com/questions/43380042/purpose-of-return-self-python

+ implementation a iterator over a function with a generator
```python
def my_range(start, end):
  current = start
  while current < end:
    yield current
    current += 1
```
