class Car():
    '''A simple attempt to create a car class'''
    def __init__(self, make:str, model:str, year:int):
        self.make = make
        self.model = model
        self.year = year
        # adding the mile age attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a netly formated descriptive name'''
        long_name = f'{str(self.year)} {str(self.make)} {str(self.model)}'
        return long_name.title()
    
    def read_odometer(self):
        '''Print a statement showing the car's mileage.'''
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    # method to update the odometer directly
    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value.
           Reject the change if it attempts to roll the odometer back.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer!.")

    def increment_odometer(self, miles):
        ''''Add the given amount to the odometer reading.'''
        self.odometer_reading += miles

my_car = Car('BMW', 'M4', 2025)
# my_car.make = 'Audi'
print(f'Al-amin Nababa\'s car info: {my_car.get_descriptive_name()}')
my_car.odometer_reading = 32
# my_car.read_odometer()
# my_car.update_odometer(21)
my_car.increment_odometer(20)
my_car.read_odometer()