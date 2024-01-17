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



class Ward(object):

    def __init__(self, d=None):
        self.d = {} if d is None else d

    def add(self, patient):
        self.d[patient.name] = patient

    def remove(self, name):
        if name in self.d:
            del self.d[name]

    def lookup(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None


    def get_patients_by_med(self, med):
        patients = []
        for v in self.d.values():
            if med in v.meds:
                patients.append(v)
        return patients

    def get_least_common_meds(self):
        meds = []
        d = {}
        for v in self.d.values():
            for m in v.meds:
                if m not in d:
                    d[m] = 1
                else:
                    d[m] += 1
            mini = min(d.values())

        for k, v in d.items():
            if v == mini:
                meds.append(k)

        return meds



    def get_most_common_meds(self):
        meds = []
        d = {}
        for v in self.d.values():
            for m in v.meds:
                if m not in d:
                    d[m] = 1
                else:
                    d[m] += 1
            maxi = max(d.values())

        for k, v in d.items():
            if v == maxi:
                meds.append(k)
        return meds