class restaurants():
    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        
    def describe_restaurant(self):
        print("\nThe name of the restaurant is:", self.restaurant_name.title() + ".")
        print("It serves", self.cousine_type, "type of food.")
        
    def open_restaurant(self):
        print("The restaurant is open everyday from 8am to 11pm.")
    
vegan_hungry = restaurants("Vegehop","vegan")
mcd_hungry = restaurants("McDonalds", "fast food")
sime_hungry=restaurants("Šime", "gableci")



vegan_hungry.describe_restaurant()
mcd_hungry.describe_restaurant()
sime_hungry.describe_restaurant()