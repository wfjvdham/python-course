a = 3
b = 0

try:
    a/b
except Exception:
    print('This is not allowed')
else:
    print('Success')

a = 3
b = 0

try:
    a/b
except Exception as e:
    print('This is not allowed, because: ', e.args)
else:
    print('Success')