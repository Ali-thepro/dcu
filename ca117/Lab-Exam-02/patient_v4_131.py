class Patient(object):

    def __init__(self, name, age, doctor, meds=None):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.meds = [] if meds is None else meds
        self.vitals = {}


    def add_medication(self, other):
        if other not in self.meds:
            self.meds.append(other)

    def record_vital(self, v, i):
        self.vitals[v] = i

    def get_vital(self, v):
        if v in self.vitals:
            return self.vitals[v]
        else:
            return f'N/A'

    def __str__(self):
        out = []
        out.append(f'Name: {self.name}')
        out.append(f'Age: {self.age}')
        out.append(f'Medications: {", ".join(self.meds)}')
        out.append(f'Doctor: {self.doctor}')
        return "\n".join(out)
