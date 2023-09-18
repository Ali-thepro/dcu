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



# class Memories:
#     def __init__(self, **attributes):
#         self.attributes = attributes

#     def remember(self, attribute):
#         if attribute in self.attributes:
#             return self.attributes[attribute]
#         else:
#             return False

# person1 = Memories(name='Tom', age=32, salary=50000)
# print(person1.remember('salary')) 
# print(person1.remember('email')) 







# class Memories:
    
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#method 1    
    # def remember(self, info):
    #     attribute_info = getattr(self, info, False)
    #     return attribute_info

        # if attribute_info:
        #     return attribute_info
        # else:
        #     return False

        # return attribute_info if attribute_info else False

#method 2
    # def remember(self ,info):
    #     try:
    #         attribute_info = getattr(self, info)
    #         return attribute_info
    #     except AttributeError:
    #         return False

# person1 = Memories(name='Tom', age=32, salary=50000)
# print(person1.remember('salary')) 
# print(person1.remember('email')) 






# class Memories():

#     def __init__(self, name, age=0, salary=0):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def remember(self, info):
#         if info == 'name':
#             return self.name
#         elif info == 'age':
#             return self.age
#         elif info == 'salary':
#             return self.salary
#         else:
#             return False
# person1 = Memories(name='Tom', age=32, salary=50000)
# print(person1.remember('salary'))
# print(person1.remember('email'))