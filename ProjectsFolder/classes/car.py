class User():
    def __init__(self, first_name:str, last_name:str):
        self.name1 = first_name
        self.name2 = last_name
        self.name = self.name1 + ' ' + self.name2

    def describe_user(self):
        message = {'Full name': self.name}
        return message
    
    def greet_user(self):
        meessage = f'Hi Good morning {self.name}.'
        return meessage
    


first_user = User('Alamin', 'Hamza')
first_user.name

first_user.describe_user()
first_user.greet_user()