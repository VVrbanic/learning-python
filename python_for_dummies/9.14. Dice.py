from random import randint

class die ():
    
    def __init__(self,sides = 6):
        #define the number of sides
        self.sides=sides
    
    def roll_die(self):
        #roll a random number 10 times
        for i in range(1, 10):
            x=randint(1, self.sides)
            print(x)

dice10=die(444444)
dice10.roll_die()