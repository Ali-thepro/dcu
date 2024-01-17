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