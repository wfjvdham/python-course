def add_numbers(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


print(add_numbers(1, 2, 3))


def color_car(color):
    print(f'A {color} car')


color_car('red')


def vehicle_type(color, code, vehicles_options):
        print(f'A {color} {vehicles_options[code]}')


vehicles = ['car', 'motorbike', 'bike', 'caravan']
vehicle_type("blue", 2, vehicles)

result = "Amazing Joe's Garage, we service "
for idx, vehicle in enumerate(vehicles):
    if idx == len(vehicles) - 1:
        result = result[:-2] + ' and ' + vehicle + 's.'
    else:
        result += vehicle + 's, '
print(result)


def add_10(n):
    return n + 10


a = 5
a = add_10(a)
print(a)


def add_10_list(mylist):
    mylist.append(10)


alist = [3, 5, 9]
add_10_list(alist)
print(alist)


def calculations(initial_number, **calculations_dict):
    for key, value in calculations_dict.items():
        if key == 'add':
            initial_number += value
        elif key == 'subtract':
            initial_number -= value
        elif key == 'divide':
            initial_number = initial_number / value
        else:
            initial_number *= value
    return initial_number


print(calculations(5, **{
    'add': 5,
    'multiply': 3,
    'subtract': 2,
    'divide': 4,
}))