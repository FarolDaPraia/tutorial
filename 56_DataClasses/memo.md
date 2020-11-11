# Dataclasses
https://www.youtube.com/watch?v=T-TwcmT6Rcw

1. It makes a multable data holder, in the spirit of named tuple
2. it writes boiler-plate code for you, simplifying the process of writing the class

```python
from dataclasses import dataclass
@dataclass
class Color:
  hue: int
  saturation: foat
  lightness: float = 0.5

from typing import NamedTuple
class Color(NamedTuple):
  hue: int
  saturation: foat
  lightness: float = 0.5
```
