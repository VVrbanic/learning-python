age=16

if age < 2:
    name = "baby"
elif age >= 2 and age < 4:
    name = "toddler"
elif age >= 4 and age < 13:
     name = "kid"
elif age >= 13 and age < 20:
     name = "teenager"     
elif age >= 20 and age < 65:
     name = "adult"
elif age > 65:
    name = "elder"
print("You are a/an",name,":)")