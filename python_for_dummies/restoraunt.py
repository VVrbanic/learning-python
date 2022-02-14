class restaurants():
    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        
    def describe_restaurant(self):
        print("The name of the restaurant is:", self.restaurant_name.title() + ".")
        print("It serves", self.cousine_type, "type of food.")
        
    def open_restaurant(self):
        print("The restaurant is open everyday from 8am to 11pm.")