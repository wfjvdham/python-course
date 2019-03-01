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

> A package is a collection of modules

A package has the following structure:

- A directory containing all the python code and an `__init__.py` file. The `__init__.py` file is usually empty but is required to tell python this is a package.
- A `setup.py` file containing general information about the package.


# pip (Pip Installs Packages)

> Package manager

## Install

When present on [PyPI](https://pypi.org/) (Python Package Index)

`pip install ...`

When developing a local package

`pip install -e path/to/package`

To save dependencies to a file

`pip freeze > requirements.txt`

To install dependencies from a file

`pip install -r requirements.txt`

# Environments

> A way of managing different versions of packages or python for different projects

## Conda

1. Create environment 

    `conda create --name my_env`
    
    or
    
    `conda create --name my_env python=3.4`
    
1. Checking environments

    `conda list`

1. Activate environment

    `conda activate my_env`
    
1. Install packages only in the environment

    `pip install docutils`
    
1. Deactivate environment

    `conda deactivate`
    
1. Remove environment

    `conda remove --name my_env --all`

## Venv

- python built-in library since version 3.3
- Use a environment name that corresponds to your project
- Create the environment in the same directory as your project

1. Create environment 

    `python -m venv my_env`
    
    or 
    
    `python3.4 -m venv my_env`

1. Activate environment

    - bash `source my_env/bin/activate`
    - cmd `my_env/Scripts/activate.bat`
    - powershell `my_env/Scripts/Activate.ps1`
    
1. Install packages only in the environment

    `pip install docutils`
    
1. Deactivate environment

    `deactivate`
    
1. Remove environment

    `rm -r my_env`
    
## Virtualenv

[Documentation](https://virtualenv.pypa.io/en/stable/)

[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/#)