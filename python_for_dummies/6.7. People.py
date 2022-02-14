first_presedent={
            "first_name" : "Franjo",
            "last_name" : "Tudjman",
            "age" : 97,
            "city" : "Zagreb",
            }

second_presedent={
            "first_name" : "Stipe",
            "last_name" : "Mesic",
            "age" : 61,
            "city" : "Zagreb",
            }
third_presedent={
            "first_name" : "Ivo",
            "last_name" : "Josipovic",
            "age" : 83,
            "city" : "Zagreb",
            }
            
peoples=[first_presedent, second_presedent, third_presedent]
for people in peoples:
    print("\n")
    for key, value in people.items():
        print(key, ":", value)



