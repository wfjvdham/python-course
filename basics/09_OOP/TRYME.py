import copy


class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Wim')
p.say_hi()


class Teacher(Person):
    """Represents a teacher."""
    def __init__(self, name, topic):
        Person.__init__(self, name)
        self.topic = topic
        print('(Initialized Teacher: {})'.format(self.name))

    def tell_topic(self):
        print('My topic is: {}'.format(self.topic))


t = Teacher("Wim", "Python")
t.say_hi()
t.tell_topic()

t2 = copy.deepcopy(t)
t2.tell_topic()

t.topic = "java"
t.tell_topic()
t2.tell_topic()
