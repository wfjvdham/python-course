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

# Functions

1. Create a function that takes 3 arguments and returns the sum of the these arguments.
1. Create a function named `color_car()` that receives a color, and prints out, 'a red car' for example.
1. Create a function named `vehicle_type()` that receives a color, and a code, **1** for a car, **2** for a motorbike. Print 'a blue motorbike' for example when called as `vehicle_type("blue", 2)`
1. Make a list of vehicles, you can add "motorbike", "caravan", "bike", or more.
1. Change the function `vehicle_type()` to use the list of the previous question. So that `vehicle_type("green", 3)` prints out "a green bike".
1. Use the list of vehicles to write an advertisement. So that it prints something like: "Amazing Joe's Garage, we service cars, motorbikes, caravans and bikes.". (Hint: use a for loop.) The output should be correct English with all the punctuation in place (that's the challenge). So plurals for the vehicle types, commas followed by a single space, the word and to replace the final comma and closed off by a period.
1. What if you add one more vehicle to the list, can you have that added to the advertisement without changing the code of the previous question?

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
1. Write a function that receives a country as an argument and prints the capital if present in the dictionary. Otherwise it prints 'No info available'
1. Write a loop that creates a dictionary with as keys the numbers 1 till 10. And as values the key to the power 2.

# List Comprehensions

1. Create a list containing the numbers 1 till 10.
1. Use a for loop to double the odd numbers and filter out the even numbers.
1. Now do the same using a list comprehension

For the next exercises use the following tasks list:

```
tasks = [
  {
    'name': 'Write a summary HTML/CSS',
    'duration': 180
  },
  {
    'name': 'Some web development',
    'duration': 120
  },
  {
    'name': 'Fix homework for class10',
    'duration': 20
  },
  {
    'name': 'Talk to a lot of people',
    'duration': 200
  },
  {
    'name': 'Keep writing summary',
    'duration': 240
  },
  {
    'name': 'Some more web development',
    'duration': 180
  },
  {
    'name': 'Staring out the window',
    'duration': 10
  },
  {
    'name': 'Talk to a lot of people',
    'duration': 200
  },
  {
    'name': 'Look at application assignments new students',
    'duration': 40
  }
]
```

1. Create a list containing the duration in hours for all the tasks.
1. Filter out all tasks that have a duration of less than 2 hours.
