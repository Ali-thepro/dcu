class Student(object):

    def __init__(self, name, sid, marks):
        self.name = name
        self.sid = sid
        self.marks = {module: mark for (module, mark) in marks}

    def average_mark(self):
        return round(sum(self.marks.values()) / len(self.marks))
        # marks = [m for m in self.marks.values]
        # return round(sum(marks) / len(marks))

    
    def __eq__(self, other):
        return self.average_mark() == other.average_mark()
    
    def __lt__(self, other):
        return self.average_mark() < other.average_mark()
    
    def __gt__(self, other):
        return self.average_mark() > other.average_mark()
    
    def __str__(self):
        output = []
        output.append(f'Name: {self.name}')
        output.append(f'ID: {self.sid}')
        output.append(f'Modules: {", ".join(sorted(self.marks.keys()))}')
        # output.append(f'Modules: {", ".join([module for module in self.marks.keys()])}')
        output.append(f'Average mark: {self.average_mark()}')
        return "\n".join(output)
    

  








# class Student(object):

#     def __init__(self, name, sid, modlist=None):
#         self.name = name
#         self.sid = sid
#         if modlist is None:
#             modlist = []
#         self.modlist = modlist



#     def __str__(self):
#         output = []
#         output.append(f'Name: {self.name}')
#         output.append(f'ID: {self.sid}')
#         output.append(f'Modules: {", ".join(sorted([s[0] for s in self.modlist]))}')
#         output.append(f'Average mark: {round(sum([int(n[1]) for n in self.modlist]) / len(self.modlist))}')
#         return "\n".join(output)
    






#!/usr/bin/env python3
 
# class Student(object):

#     def __init__(self, name, sid, mark):
#         self.name = name
#         self.sid = sid
#         self.modlist = []
#         self.marklist = []
#         for line in mark:
#             self.modlist.append(line[0])
#             self.marklist.append(line[1])
#         self.modlist = ", ".join(sorted(self.modlist))
#         t = 0
#         for d in self.marklist:
#             d = int(d)
#             t += d
#         self.mark = t / len(self.marklist)
#     def __str__(self):
#         lines = []
#         lines.append(f"Name: {self.name}")
#         lines.append(f"ID: {self.sid}")
#         lines.append(f'Modules: {self.modlist}')
#         lines.append(f"Average mark: {(round(self.mark))}")     {int(round(self.mark, 0))}
#         return '\n'.join(lines)
    




# class Student(object):
#    def __init__(self, name, uid, modules):
#       self.name = name
#       self.uid = uid
#       self.modules = modules

#    def __str__(self):
#       self.modules = sorted(self.modules)
#       average = round((self.modules[0][1] + self.modules[1][1]) / 2)
#       output = []
#       output.append(f'Name: {self.name}')
#       output.append(f'ID: {self.uid}')
#       output.append(f'Modules: {self.modules[0][0]}, {self.modules[1][0]}')
#       output.append(f'Average mark: {average}')
#       return "\n".join(output)
