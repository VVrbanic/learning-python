class restaurants():
    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = 0
        
    def set_number_served(self):
        #self.number_served = costumers
        print("This is the number of cosumers you have served todday", str(self.number_served))
    
    def increment_number_served(self, costumers):
        self.number_served = costumers
        print("This is the number of cosumers you have served todday", str(self.number_served))
        
        
    def describe_restaurant(self):
        print("The name of the restaurant is:", self.restaurant_name.title() + ".")
        print("It serves", self.cousine_type, "type of food.")
        
    def open_restaurant(self):
        print("The restaurant is open everyday from 8am to 11pm.")
    
im_hungry = restaurants("Vegehop","vegan")

im_hungry.describe_restaurant()
im_hungry.open_restaurant()

print(im_hungry.number_served)
im_hungry.increment_number_served(22)
im_hungry.set_number_served()