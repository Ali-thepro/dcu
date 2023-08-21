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
    
    def __eq__(self, other):
        return self.total_time() == other.total_time()
    
    def __gt__(self, other):
        return self.total_time() > other.total_time()

    def __str__(self):
        r = []
        r.append("Name: {}".format(self.name))
        r.append("ID: {}".format(self.tid))
        r.append("Race time: {}".format(self.total_time()))
        return "\n".join(r)
    

def sort_on(t):
    return t.name

class Triathlon(object):
    
    def __init__(self):
        self.d = {}

    def add(self, other):
        self.d[other.tid] = other

    def remove(self, other):
        if other in self.d:
            del self.d[other]

    def lookup(self, other):
        if other in self.d:
            return self.d[other]
        else:
            return None
        
    def best(self):
        return min(self.d.values())
        
    def worst(self):
        return max(self.d.values())
        
    def __str__(self):
        r = "\n".join([f'{t}' for t in sorted(self.d.values(), key=sort_on)])
        return r