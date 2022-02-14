class user():
    def __init__(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        
    def describe_user(self):
        print("\nFirst name:", self.first_name.title(),
              "\nLasta name:", self.last_name.title(), "\nAge:", self.age,
              "\nGender:", self.gender.title(),"\nOccupation:", self.occupation.title())
        
    def greeting_user(self):
        print("\nHello", self.first_name.title(), "and welcome to the website.")
        
class admin(user):
    
    def __init__(self, first_name, last_name, age, gender, occupation):
        super().__init__(first_name, last_name, age, gender, occupation)
    
    def show_privileges(self):
        privileges=("can add post", "can delete post", "can aprove post")
        print("The admin can:")
        for privilege in privileges:
            print("-",privilege)
            
        
man=user("hank", "hill", 45, "male", "redneck")
woman=admin("peggy", "hill", 43, "female", "annoying")

woman.show_privileges()

#man.describe_user()
#man.greeting_user()

#woman.describe_user()
#woman.greeting_user()

