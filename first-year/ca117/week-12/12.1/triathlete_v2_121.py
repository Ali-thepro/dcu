class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}

    def add_time(self, discipline, time):
        self.times[discipline] = time

    def get_time(self, discipline):
        return self.times[discipline]

    def total_time(self):
        return sum(self.times.values())

    def __str__(self):
        r = []
        r.append("Name: {}".format(self.name))
        r.append("ID: {}".format(self.tid))
        r.append("Race time: {}".format(self.total_time()))
        return "\n".join(r)