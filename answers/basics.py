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
