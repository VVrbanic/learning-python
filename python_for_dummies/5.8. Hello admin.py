users = ["LG", "iPhone", "HTC", "Xiaomi", "admin"]

for user in users:
    
    if user == "admin":
        print("\nHello admin, would you like to see a status report?")
    else:
        print("Hello", user)