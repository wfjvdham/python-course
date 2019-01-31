while True:
    birth_year = input('What is your year of birth? ')
    try:
        birth_year_int = int(birth_year)
        if birth_year_int > 2019:
            print('Your birth year cannot be in the future')
        elif birth_year_int < 1909:
            print('You cannot be older than 100')
        else:
            print('Your age is', 2019 - birth_year_int)
            break
    except Exception:
        print('Not a valid integer')
