# Strings

print('hello')
print('''this wil print
a long hello string''')
print("I'm awesome")
name = 'Wim'
age = 32
print(f'Hi, I am {name} and I am {age} years old')

# Control Flow

for i in range(1, 101):
    if (i % 3 == 0) & (i % 5 == 0):
        print('Fizz Buzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

# Functions


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

# Dictionary

capitals = {
    'France': 'Paris',
    'Belgium': 'Brussels',
    'Germany': 'Berlin',
}


def get_capital(country):
    if country in capitals:
        print(capitals[country])
    else:
        print('No info available')


get_capital('France')
get_capital('England')

d = dict()
for x in range(1, 11):
    d[x] = x ** 2
print(d)

# List Comprehensions

numbers = list(range(1, 11))
numbers2 = [item * 2 for item in numbers if item % 2 == 1]
print(numbers2)

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

durations_hours = [task['duration'] / 60 for task in tasks]
print(durations_hours)

long_tasks = [task for task in tasks if task['duration'] > 120]
print(long_tasks)
