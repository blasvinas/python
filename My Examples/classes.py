class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print("{} is a {} restaurant.  Customer server: {}".format(self.name, self.cuisine, self.number_served))

    def open_restaurant(self):
        print ("{} is open".format(self.name))

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_serverd(self,number):
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine):
        super().__init__(name,cuisine)
        self.flavors = []

    def set_flavors(self,flavors):
        self.flavors = flavors

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

restaurant1 = Restaurant("Little China","Chineesse")
restaurant2 = Restaurant("Pasta Palace","Italian")
restaurant3 = Restaurant("Super Burger","American")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant2.set_number_served(5)
restaurant2.describe_restaurant()
restaurant2.increment_number_serverd(3)
restaurant2.describe_restaurant()

ice_cream_restaurant = IceCreamStand("The big cone","Ice Cream")
ice_cream_restaurant.set_flavors(['vanilla','strawberry','chocolate'])
ice_cream_restaurant.show_flavors()