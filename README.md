# An Eva Interpreter, in Python
This contains the implementation of an interpreter for the small language "Eva",
from Dmitry Soshnikov's "Essentials of Interpretation"
[course](http://dmitrysoshnikov.com/courses/essentials-of-interpretation/).

Of course, I'm using Python here instead of Javascript/node, but overall the
effect should be the same. I've chosen to use PyTest to help manage all the test
code, since it makes life so easy in that respect.

## Usage
```bash
$ ./eva -{ef} source.eva
```

## Tests
(in current directory, requires pytest)
```bash
$ pytest
```
