class Memories:
    def __init__(self, **attributes):
        for k, v in attributes.items():
            setattr(self, k, v)

    def remember(self, attribute):
        if attribute in self.__dict__:
            return self.__dict__[attribute]
        else:
            return False
        
    # def remember(self, attribute):
    #     if hasattr(self, attribute):
    #         return getattr(self, attribute)
    #     else:
    #         return False

person1 = Memories(name='Tom', age=32, salary=50000)
print(person1.__dict__) 
print(person1.remember('salary')) 
print(person1.remember('email'))