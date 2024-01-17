class Patient(object):

    def __init__(self, name, age, doctor):
        self.name = name
        self.age = age
        self.doctor = doctor

    def __str__(self):
        out = []
        out.append(f'Name: {self.name}')
        out.append(f'Age: {self.age}')
        out.append(f'Doctor: {self.doctor}')
        return "\n".join(out)