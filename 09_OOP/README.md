# Object-oriented programming

> Objects are just another form of code reuse and organisation

- **Field** a variable in an object
- **Method** a function in an object
- **Fields** and **Methods** together are called **Attributes**
- `self` is a keyword used inside the object to reference to itself. By default it is the first parameter of any method.

## Concepts

- **Encapsulation** each object keeps its state inside a class together with some functionalities that are typical for this object
- **Abstraction** hiding unnecessary details from the user
- **Composition** *has-a* relationship
- **Inheritance** *is-type-of* relationship, it can use the functions from other objects
- **Delegation** attributes and methods are accessible by a child object
- **Polymorphism** when multiple object types implement the same functionality

## Basic Instantiation

```python
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
```

## The `__init__` method

The __init__ method is run as soon as an object of a class is instantiated (i.e. created). The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Wim')
p.say_hi()
```

## Inheritance

A teacher is a type of person so when constructing a teacher you call the `Person` `__init__` function.

```python
class Teacher(Person):
    """Represents a teacher."""
    def __init__(self, name, topic):
        Person.__init__(self, name)
        self.topic = topic
        print('(Initialized Teacher: {})'.format(self.name))

    def tellTopic(self):
        print('My topic is: {}'.format(self.topic))
```

This class can be used in the following way:

```python
t = Teacher("Wim", "Python")
t.say_hi()
t.tellTopic()
```

## Copy Objects

By default objects are copied *by-reference* which means that the new object still refers to the attributes of the old 
one. So if you change a *Field* of the old object, it is also changed in the new object. If this behaviour is not wanted
than the `deepcopy()` function from the `copy` library can be used.

```python
t2 = t
t2.tellTopic()

t.topic = "java"
t.tellTopic()
t2.tellTopic()

import copy

t2 = copy.deepcopy(t)
t2.tellTopic()

t.topic = "java"
t.tellTopic()
t2.tellTopic()
```