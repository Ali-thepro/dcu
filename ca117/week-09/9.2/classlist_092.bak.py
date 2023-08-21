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
    

class Classlist(object):
    
   def __init__(self):
      self.d = {}

   def add(self, s):
      self.d[s.sid] = s

   def __str__(self):
      return "\n".join([str(v) for v in sorted(self.d.values(), reverse=True)])
      # output = []
      # for v in sorted(self.d.values(), reverse=True):
      #    output.append(f'{v}')
      # return "\n".join(output)

       





# class Student(object):
#    def __init__(self, name, uid, modules, average=0):
#       self.name = name
#       self.uid = uid
#       self.modules = modules
#       self.average = average

#    def getAverage(self):
#       self.average = round((self.modules[0][1] + self.modules[1][1]) / 2)
#       return self.average

#    def __str__(self):
#       self.modules = sorted(self.modules)
#       output = []
#       output.append(f'Name: {self.name}')
#       output.append(f'ID: {self.uid}')
#       output.append(f'Modules: {self.modules[0][0]}, {self.modules[1][0]}')
#       output.append(f'Average mark: {self.average}')
#       return "\n".join(output)

# class Classlist(object):
#    def __init__(self):
#       self.dic = {}

#    def add(self, other):
#       self.dic[other.getAverage()] = other

#    def __str__(self):
#      output = []
#      for k, v in sorted(self.dic.items(), reverse=True):
#         output.append(f'{v}')
#      return "\n".join(output)
   






# class Classlist(object):

#     def __init__(self, d=None):
#         self.d = {} if d is None else d

#     def add(self, student):
#         self.d[student.sid] = student

#     def sort_by_average_mark(self, student_item):
#         return student_item[1].average_mark()

#     def __str__(self):
#         output = []
#         for k, v in sorted(self.d.items(), key=self.sort_by_average_mark, reverse=True):
#             output.append(f'{v}')
#         return "\n".join(output)









# def sort_by_average_mark(student_item):
#     return student_item[1].average_mark()

# class Classlist(object):

#     def __init__(self, d=None):
#         self.d = {} if d is None else d

#     def add(self, student):
#         self.d[student.sid] = student

#     def __str__(self):
#         output = []
#         for k, v in sorted(self.d.items(), key=sort_by_average_mark, reverse=True):
#             output.append(f'{v}')
#         return "\n".join(output)









# class Student(object):

#     def __init__(self, name, sid, modlist=None):
#         self.name = name
#         self.sid = sid
#         if modlist is None:
#             modlist = []
#         self.modlist = modlist



#     def average_mark(self):
#         return round(sum([int(n[1]) for n in self.modlist]) / len(self.modlist))

#     def __str__(self):
#         output = []
#         output.append(f'Name: {self.name}')
#         output.append(f'ID: {self.sid}')
#         output.append(f'Modules: {", ".join(sorted([s[0] for s in self.modlist]))}')
#         output.append(f'Average mark: {self.average_mark()}')
#         return "\n".join(output)
    
# class Classlist(object):

#     def __init__(self, d=None):
#         if d is None:
#             d = {}
#         self.d = d

#     def add(self, student):
#         if student.sid not in self.d:
#             self.d[student.sid] = student

#     def __str__(self):
#         output = []
#         for k, v in sorted(self.d.items(), key=lambda x: x[1].average_mark(), reverse=True):
#             output.append(str(v))  #or f'{v}'    or str(v)  
#         return "\n".join(output)










# class Student(object):

#     def __init__(self, name, sid, modlist=None):
#         self.name = name
#         self.sid = sid
#         if modlist == None:
#             self.modlist = []
#         else:
#             self.modlist = modlist
    
#     def average_mark(self):
#         nums = []
#         for i in self.modlist:
#             nums.append(int(i[1]))
#         t = 0
#         for d in nums:
#             t += d
#         return round(t / len(self.modlist))
#     def get_modules(self):
#         modules = []
#         for i in self.modlist:
#             modules.append(i[0])
#         return sorted(modules)
#     def __gt__(self, other):
#         return self.average_mark() > other.average_mark()
#     def __lt__(self, other):
#         return self.average_mark() < other.average_mark()
#     def __eq__(self, other):
#         return self.average_mark() == other.average_mark()
#     def __str__(self):
#         output = []
#         output.append(f'Name: {self.name}')
#         output.append(f'ID: {self.sid}')
#         output.append(f'Modules: {", ".join(self.get_modules())}')
#         output.append(f'Average mark: {self.average_mark()}')
#         return '\n'.join(output)

# class Classlist(object):

#     def __init__(self, dict=None):
#         if dict == None:
#             self.dict = {}
#         else:
#             self.dict = dict
#     def add(self, student):
#         self.dict[student.sid] = student
#     def __str__(self):
#         output = []
#         for v in sorted(self.dict.values(), reverse=True):
#             output.append(f'{v}')
#         return '\n'.join(output)