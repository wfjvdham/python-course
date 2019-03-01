# Input and Output

`python` supports multiple input and output.

- Interacting with the user using `input()` and `print()`
- Reading and writing files
- Communicating with a database

## Reading and writing files

Using the `open()` function, which can have some of the following modes:

- **r** read mode, which is used when the file is only being read (Default)
- **w** write mode, for overwriting a file (any existing files with the same name will be erased when this mode is activated) 
- **a** appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 
- **r+** for reading and writing a file

Combined with the following file type:

- **t** text file (Default)
- **b** binary file

## Pickle

Using the `pickle` module you can store and retrieve any python object in a binary file format. Add a **b** to the `open()` function.

```
f = open("file.data", "wb")

pickle.dump(data, f)
data = pickle.load(f)
```


## DB API

> A standard interface for database communication influences by ODBC and JDBC

- Compatible with most popular databases (MySQL, PostgreSQL, ...)
- Each database type has its own module, but implements largely the same functions.
- Use a `Connection` object for the connection with the database. 
- Use a `Cursor` object for manipulating the database and retrieve the results.

## with

The `with` keyword in python is a more compact way to put frequently used operations in a try..finally loop. It uses the `__enter__` and `__exit__` methods on the object that is used. These methods are implemented for the File object and for the different database connectors. No try..finally is needed,  the `__exit__` function is always called to do the cleaning up. See more details [here](http://effbot.org/zone/python-with-statement.htm) and an example in the TRYME file.