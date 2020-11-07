# Random

```python
>>> from random import *
>>> random()
```
+ if you restart the shell you would get a new random. However if you  seed the random number generator, you can reliably produce the exact same sequence, over and over again. Use case Simulation
```python
>>> seed(8675309)
>>> random()
>>> random()
```
+ choice: if I were to pick a choice of those outcomes, it just gives me a single one, and it's equidistributed.

+ choices: to make multiple choices, and so we just turn this into a plural, and we tell it how many we want. I would like to choose 10 times.

+ Shuffle is a little bit like sort, in that it works in place. So it actually mutates the input, whereas nothing else mutated the input. Now earlier, we saw that when we made multiple choices, if I chose five times, that there might be some duplications in there.

+ If I'd like to choose without duplication, and do sampling without replacement, there is sample, which has a similar format.
