# functions


def say_hello():
    # block belonging to the function
    print('hello world')
# End of function


say_hello()  # call the function
say_hello()  # call the function again


def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


# directly pass literal values
print_max(3, 4)

x = 5
y = 7


# pass variables as arguments
print_max(x, y)

x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y


print(maximum(2, 3))


def default_values_print_max(a, b=2):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

default_values_print_max()
default_values_print_max(3)
default_values_print_max(1)
default_values_print_max(5, 7)

# mutable vs immutable


def changeme(mylist):
    mylist.append([1, 2, 3])
    print("List inside the function: ", mylist)


mylistouter = [10, 20, 30]
changeme(mylistouter)
print("List outside the function: ", mylistouter)


def increaseme(n):
    n = n + 10
    print('Inside the function: ', n)


b = 5
increaseme(b)
print('Outside the function: ', b)

# *args and **kwargs


def sum_of_two(a, b):
    return a + b


print(sum_of_two(3, 4))


def sum_of_any(*args):
    if isinstance(args[0], int):      # integer?
        total = 0                     # init to zero
    else:
        total = ""                    # use empty slice of arg1
    for arg in args:
        total += arg
    return total


print(sum_of_any(2, 3, 4, 5))
print(sum_of_any("this", "is", "a", "sentence"))


def intro(**data):
    print("\nData type of argument:" + str(type(data)))

    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
