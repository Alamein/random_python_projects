class Car():
    '''A simple attempt to create a car class'''
    def __init__(self, make:str, model:str, year:int):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''Return a netly formated descriptive name'''
        long_name = f'{str(self.year)} {str(self.make)} {str(self.model)}'
        return long_name.title()
    

my_car = Car('BMW', 'M4', 2025)
# my_car.make = 'Audi'
print(f'Al-amin Nababa\'s car info: {my_car.get_descriptive_name()}')