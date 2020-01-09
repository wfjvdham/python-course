class Person:
    def __init__(self, name, age, gender, interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def bio(self):
        response = f"Hi, I am {self.name.first} {self.name.last}. I am a {self.gender} of {self.age} years old. " \
            "My interests are: "
        for idx, interest in enumerate(self.interests):
            if idx == 0:
                response += interest
            elif idx == len(self.interests) - 1:
                response += ' and ' + interest + '.'
            else:
                response += ', ' + interest
        print(response)

    def greeting(self):
        response = 'Hi, I am {} {}.'.format(self.name.first, self.name.last)
        print(response)

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address


class Teacher(Person):
    def __init__(self, name, age, gender, interests, subject):
        Person.__init__(self, name, age, gender, interests)
        self.subject = subject

    def greeting(self):
        print('Hi, I am a teacher in {} and my name is {} {}'.format(self.subject, self.name.first, self.name.last))


class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number


n = Name("Wim", "van der Ham")
p = Person(n, 32, 'male', ['teaching', 'python', 'dancing'])
p.bio()
p.greeting()

n2 = Name("Jaap", "Jansen")
p2 = Person(n2, 23, 'male', ['reading', 'python', 'soccer'])
p2.bio()
p2.greeting()

n3 = Name("Linda", "Beentjes")
t = Teacher(n3, 22, 'female', ['movies', 'cars'], 'Math')
t.bio()
t.greeting()

a = Address('dorpstraat', 1)

p.set_address(a)
p2.set_address(a)

print(p.get_address().__dict__)
print(p2.get_address().__dict__)

p.address.number = 5

print(p.get_address().__dict__)
print(p2.get_address().__dict__)