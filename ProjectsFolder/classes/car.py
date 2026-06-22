# class User():
#     def __init__(self, first_name:str, last_name:str, **):
#         self.name1 = first_name
#         self.name2 = last_name
#         self.name = self.name1 + ' ' + self.name2

#     def describe_user(self):
#         message = {'Full name': self.name}
#         return message
    
#     def greet_user(self):
#         meessage = f'Hi Good morning {self.name}.'
#         return meessage
    


# first_user = User('Alamin', 'Hamza')
# first_user.name

# first_user.describe_user()
# first_user.greet_user()


class User():
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name

        for key, value, in user_info.items():
            setattr(self, key, value)
    
    def describe_user(self):
        print(f'Name: {self.first_name} {self.last_name}')

        for attribute, value in self.__dict__.items():
            if attribute not in ('first_name', 'last_name'):
                print(f'{attribute}: {value}')

    def greet_user(self):
        print(f'Hi Good day {self.first_name} {self.last_name}')


user1 = User('Alamin', 'Nababa', age=20, city='kano', LGA='municipal')

print(user1.last_name.title())
print(user1.describe_user())
print(user1.greet_user())