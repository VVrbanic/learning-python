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
        
man=user("hank", "hill", 45, "male", "redneck")
woman=user("peggy", "hill", 43, "female", "annoying")

man.describe_user()
man.greeting_user()

woman.describe_user()
woman.greeting_user()