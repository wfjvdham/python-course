# Strings

1. Use `print()` to print some long and short strings
1. Fix the following problem: `print('I'm awesome')`
1. Assign some information about yourself to some variables. Use this variables to fill in a string and print it.

# Control Flow

1. Write a script that prints all the numbers from 1 to 100. 
1. Create the [Fizz Buzz](https://en.wikipedia.org/wiki/Fizz_buzz) game:
  - When a number is dividable by 3 print 'Fizz' instead of the number
  - When a number is dividable by 5 print 'Buzz' instead of the number
  - When a number is dividable by both print 'Fizz Buzz' instead of the number

# Lists

1. Create a list like `a = [2, 6, 9, 4, 1]` and use the following functions on the list and check the results:

    - `a.sort()`
    - `a.append(5)`
    - `a.pop()`
    
1. Create a list like `a = [2, [6, 9], 1]`. Make a copy of the list using the following 3 methods:

    1. `b = a`
    1. `b = a[:]`
    1. `b = a.copy()`
    1.  Using the copy library:      
            
            import copy
            b = copy.deepcopy(a)
1. Change the first value in `a` `a[0] = 0` and see what happens to `b`
1. Change a value in the sublist of `a` `a[1][0] = 0` and see what happens to `b`

# Dictionary

1. Create a dictionary with some countries and their capitals.
1. Write a loop that creates a dictionary with as keys the numbers 1 till 10. And as values the key to the power 2.
