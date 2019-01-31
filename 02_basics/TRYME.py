# Strings

print('hello world')

print("hello world")

print('''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
''')

age = 20
name = 'Wim'

print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
print('Why is {name} playing with that python?'.format(name=name))

print(f'{name} was {age} years old when he wrote this book')
print(f'Why is {name} playing with that python?')

# Operators

print(3+5)
print(3-5)
print(3/5)
print(3//5)
print(3*5)
print(3**5)
print(3 % 5)

# Control Flow

# if

number = 23
guess = 5

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.

# for

for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

letter_list = ['a', 'b', 'c']

for letter in letter_list:
    print('element: ' + letter)

for idx, letter in enumerate(letter_list):
    print('element: ' + letter + ' at index: ' + str(idx))


# data structures

# list

letter_list = ['a', 'b', 'c']

# tuple, less functionality and not changeable

letter_tuple = ('a', 'b', 'c')

# dictionary, key and value

emails = {
    'wim': 'wfjvdham@gmail.com',
    'piet': 'piet@hotmail.com',
    'kees': 'kees@yahoo.com',
}

print(emails['wim'])

for name, address in emails.items():
    print('Contact {} at {}'.format(name, address))
