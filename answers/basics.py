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
    if (i % 3 == 0) and (i % 5 == 0):
        print('Fizz Buzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

# Lists

a = [2, 6, 9, 4, 1]

a.sort()
print(a)

a.append(5)
print(a)

a.pop()
print(a)

a = [2, [6, 9], 1]
print(a)

b = a
c = a[:]
d = a.copy()
import copy
e = copy.deepcopy(a)

a[0] = 0

print(b)
print(c)
print(d)
print(e)

a[1][0] = 0

print(b)
print(c)
print(d)
print(e)

# Dictionary

capitals = {
    'France': 'Paris',
    'Belgium': 'Brussels',
    'Germany': 'Berlin',
}

d = dict()
d = {}
for x in range(1, 11):
    d[x] = x ** 2
print(d)
