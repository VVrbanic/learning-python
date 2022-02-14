from user import user

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