class car(): 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
        
    def read_odometer(self): 
            print("This car has " + str(self.odometer_reading) + " miles on it.")
            
    def update_odometer(self, mileage): 
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
class battery(): 
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
     
    def upgrade_battery(self):
        if self.battery_size!=85:
            print("Wrong!")
            self.battery_size=85
        else:
            print("bravo, you know your car well!")
        
class electriccar(car): 
    
    def __init__(self, make, model, year): 
        super().__init__(make, model, year)
        self.battery = battery()

        
hybrid = electriccar("Toyota", "A6", 2019)
hybrid.battery.describe_battery()
hybrid.battery.upgrade_battery()
hybrid.battery.describe_battery()
hybrid.battery.upgrade_battery()
