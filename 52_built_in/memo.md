## filter()  
https://www.w3schools.com/python/ref_func_filter.asp  
https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function   

returns an iterator were the items are filtered through a function to test if
the item is accepted or not
filter(function, iterable)  
see: filter.py  

referen
The filter() function provides a way of filtering values that can often be
more efficient than a list comprehension, especially when we’re starting
to work with larger data sets. For example, a list comprehension will
make a new list, which will increase the run time for that processing.
This means that after our list comprehension has completed its
expression, we’ll have two lists in memory. However, filter() will make a
simple object that holds a reference to the original list, the provided
function, and an index of where to go in the original list, which will
take up less memory.  

Learning Decorator?
```python
aquarium_creatures = [
  {"name": "sammy", "species": "shark", "tank number": "11", "type": "fish"},
  {"name": "ashley", "species": "crab", "tank number": "25", "type": "shellfish"},
  {"name": "jo", "species": "guppy", "tank number": "18", "type": "fish"},
  {"name": "jackie", "species": "lobster", "tank number": "21", "type": "shellfish"},
  {"name": "charlie", "species": "clownfish", "tank number": "12", "type": "fish"},
  {"name": "olly", "species": "green turtle", "tank number": "34", "type": "turtle"}
]
def filter_set(aquarium_creatures, search_string):
    def iterator_func(x):
        for v in x.values():
            if search_string in v:
                return True
        return False
    return filter(iterator_func, aquarium_creatures)
```
