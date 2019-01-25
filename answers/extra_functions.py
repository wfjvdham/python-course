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