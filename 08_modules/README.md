# Modules

> Used for organising your code so you can easily reuse some of your functions across programs

- Have to be imported using the **import** keyword

```python
import sys
import test as t
from math import sqrt
```

- Looks for the file in the `sys.path` directories
- Every python file can be used as a module

# Package

> A package is directory that contains modules

- Useful for providing structure if you have a lot of modules
- An `__init__.py` file must be present but can be empty
- An `setup.py` file must be present in the top directory
