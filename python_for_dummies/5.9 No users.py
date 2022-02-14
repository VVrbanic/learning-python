users = []
if users:
    
    for user in users:
        
        if user == "admin":
            print("\nHello admin, would you like to see a status report?")
        else:
            print("Hello", user)
        
else:
     print("We need to find more users!")