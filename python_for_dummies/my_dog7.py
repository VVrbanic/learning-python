class Dog(): 
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")

my_dog=Dog("willi",6)
print(my_dog.age)