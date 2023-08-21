class Customer(object):

    def __init__(self, name, number, balance=0):
        self.name = name
        self.number = number
        self.balance = balance

    def __str__(self):
        out = []
        out.append(f'Name: {self.name}')
        out.append(f'Number: {self.number}')
        out.append(f'Balance: {self.balance:.2f}')
        return "\n".join(out)
    

class Bank(object):

    def __init__(self):
        self.d = {}

    def add(self, customer):
        self.d[customer.number] = customer

    def remove(self, number):
        if number in self.d:
            del self.d[number]

    def lookup(self, number):
        if number in self.d:
            return self.d[number]
        else:
            return None
        
    def total_funds(self):
        total = 0
        for k, v in sorted(self.d.items()):
            total += v.balance
        return total
        
    def __str__(self):
        out = []
        for k, v in sorted(self.d.items()):
            out.append(f'{v}')
        out.append(f'Total funds: {self.total_funds()}')
        return "\n".join(out)