
class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.phone} {self.email}"
    
class Contactlist(object):

    def __init__(self, d=None):
        if d is None:
            d = {}
        self.d = d

    # def __init__(self,):
    #     self.d = {}

    
    def add(self, c):
        if c.name not in self.d:
            self.d[c.name] = c
        

    def remove(self, name):
        if name in self.d:
            del self.d[name]


    def get(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return None
        
    def __str__(self):
        output = []
        output.append("Contact list")
        output.append("------------")
        for k, v in sorted(self.d.items()):
            output.append(f'{v}')
        return "\n".join(output)
    





    # def __str__(self):
    #     output = ["Contact list", "------------"]
    #     for cname in sorted(self.contacts):
    #         output.append(self.contacts[cname].__str__())
    #     return "\n".join(output)
    



    # def __str__(self):
    #     lines = [str(self.dict[key]) for key in sorted(self.dict)]
    #     return 'Contact list\n' + '------------\n' + '\n'.join(lines)



    # def __str__(self):
    #     lines = []
    #     lines.append('Contact list')
    #     lines.append('------------')
    #     for n, c in sorted(self.d.items()):
    #         lines.append('{}'.format(c))
    #     return '\n'.join(lines)




    # def __str__(self):
    #     lines = []
    #     lines.append('Contact list')
    #     lines.append('------------')
    #     for n, c in sorted(self.d.items()):
    #         lines.append(str(c))
    #     return '\n'.join(lines)




