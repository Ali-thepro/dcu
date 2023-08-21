class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        r = []
        r.append("Name: {}".format(self.name))
        r.append("ID: {}".format(self.tid))
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
        
    def __str__(self):
        r = "\n".join([f'{t}' for t in sorted(self.d.values(), key=sort_on)])
        return r