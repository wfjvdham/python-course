# Functions

1. Create a function that takes 3 arguments and returns the sum of the these arguments.
1. Create a function named `color_car()` that receives a color, and prints out, 'a red car' for example.
1. Create a function named `vehicle_type()` that receives a color, and a code, **1** for a car, **2** for a motorbike. Print 'a blue motorbike' for example when called as `vehicle_type("blue", 2)`
1. Make a list of vehicles, you can add "motorbike", "caravan", "bike", or more.
1. Change the function `vehicle_type()` to use the list of the previous question. So that `vehicle_type("green", 3)` prints out "a green bike".
1. Use the list of vehicles to write an advertisement. So that it prints something like: "Amazing Joe's Garage, we service cars, motorbikes, caravans and bikes.". (Hint: use a for loop.) The output should be correct English with all the punctuation in place (that's the challenge). So plurals for the vehicle types, commas followed by a single space, the word and to replace the final comma and closed off by a period.
1. What if you add one more vehicle to the list, can you have that added to the advertisement without changing the code of the previous question?

# Kwargs

Create a function that does a series of calculations on a starting number. The starting number is passed as an 
argument to the function. The series of calculations are passed as a dictionary, for example:

```python
calculations = {
    'add': 5,
    'multiply': 3,
    'subtract': 2,
    'divide': 4,
}
```

Finally the resulting value is returned. At least the for operations in the example should be supported.