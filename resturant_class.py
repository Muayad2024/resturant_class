
class Resturant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0    #new attribute 
    def describe_restaurant(self):
        print(f'The resturant name is {self.name} and it has {self.cuisine_type} cuisine.')
    def open_restaurant(self):
        print(f'{self.name} is now open!')
    def set_number_served(self, new_number):
        self.number_served = new_number
    def increment_number_served(self, incr_number):
        self.number_served += incr_number

resturant = Resturant('Pizza Hut', 'Italian Pizza')
"""print(f'The resturant name is {resturant.name}')
print(f'The resturant cuisine type is {resturant.cuisine_type}')"""

resturant.describe_restaurant()
resturant.open_restaurant()
print(f'The customers the resturant served is {resturant.number_served}')
resturant.number_served = 7
print(f'The customers the resturant served is {resturant.number_served}')
resturant.set_number_served(10)
print(f'The customers the resturant served is {resturant.number_served}')
resturant.increment_number_served(9)
print(f'The customers the resturant served is {resturant.number_served}')
"""my_resturant = Resturant('KFC', 'Fried Chicken')
your_resturant = Resturant('McDonalds', 'Burgers')
our_resturant = Resturant('Subway', 'Sandwiches')
my_resturant.describe_restaurant()
your_resturant.describe_restaurant()
our_resturant.describe_restaurant()"""

