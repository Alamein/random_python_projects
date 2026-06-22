class Dog():
    '''A simple attempt top model a dog.'''
    def __init__(self, name, age):
        '''Initialize name and age attribute.'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate a dog sitting in respond to a command.'''
        print(f'{self.name.title()} is now sitting.')
    
    def roll_over(self):
        '''Simulate rolling over in response to a command.'''
        print(f'{self.name.title()} is rolled over!')

my_dog = Dog('Lucy', 3)
print('My dog mane is ' + my_dog.name.title())
print(my_dog.name.title() + ' is ' + str(my_dog.age) + ' years old.')
my_dog.sit()

# wecan create as many instance as we want
# even morethans thounsand of instances

class Restaurant():
    '''An attempt to model a restaurant.'''
    def __init__(self, restaurant_name: str, cuisine_type:str):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        '''Return the restaurant name and cuisine type'''
        print('The restaurant name is: ' + self.name.title() + '.')
        print('The restaurant cuisine type is: ' + self.cuisine.title() + '.')
    
    def open_restaurant(self):
        message = 'Welcome to the ' + self.name.title() + '. Please what do you want to order? '
        print(message)


restaurant = Restaurant('A Nababa Chicken', 'Dinner and Jollof rice')
print(restaurant.name.title())
print(restaurant.cuisine.title())

print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())