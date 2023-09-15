class Memories():

    def __init__(self, name, age=0, salary=0):
        self.name = name
        self.age = age
        self.salary = salary

    def remember(self, info):
        if info == 'name':
            return self.name
        elif info == 'age':
            return self.age
        elif info == 'salary':
            return self.salary
        else:
            return False
person1 = Memories(name='Tom', age=32, salary=50000)
print(person1.remember('salary'))
print(person1.remember('email'))