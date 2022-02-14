class user():
    def __init__(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        
    def describe_user(self):
        #uređuje i prikazuje dane podatke
        print("\nFirst name:", self.first_name.title(),
              "\nLasta name:", self.last_name.title(), "\nAge:", self.age,
              "\nGender:", self.gender.title(),"\nOccupation:", self.occupation.title())
        
    def greeting_user(self):
        #pozdravlja usera
        print("\nHello", self.first_name.title(), "and welcome to the website.")
    
class privileges():
    
    def __init__(self, privilege=("can add post", "can delete post", "can aprove post")):
        self.privilege = privilege
    
    def show_privileges(self):
        #opisuje što sve admin može raditi 
        print("The admin can:")
        for pri in self.privilege:
            print("-", pri)
        
class admin(user):
    #podklasa admin
    
    def __init__(self, first_name, last_name, age, gender, occupation):
        super().__init__(first_name, last_name, age, gender, occupation)
        self.privilege=privileges()