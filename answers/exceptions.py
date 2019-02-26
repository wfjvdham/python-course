while True:
    birth_year = input('What is your year of birth? ')
    try:
        birth_year_int = int(birth_year)
        if birth_year_int > 2019:
            raise Exception('Your birth year cannot be in the future')
        elif birth_year_int < 1909:
            raise Exception('You cannot be older than 100')
        else:
            raise Exception('Your age is', 2019 - birth_year_int)
            break
    except Exception as e:
        print('There was this problem: ', e.args[0])
