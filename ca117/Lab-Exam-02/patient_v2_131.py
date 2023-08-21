class Patient(object):

    def __init__(self, name, age, doctor, meds=None):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.meds = [] if meds is None else meds

    def __str__(self):
        out = []
        out.append(f'Name: {self.name}')
        out.append(f'Age: {self.age}')
        out.append(f'Medications: {", ".join(self.meds)}')
        out.append(f'Doctor: {self.doctor}')
        return "\n".join(out)
