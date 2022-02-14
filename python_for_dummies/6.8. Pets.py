piroska={"type" : "cat", "owner" : "zad"}
luna={"type" : "dog", "owner" : "ana"}
ozzy={"type" : "dog" , "owner" : "iva"}
bella={"type" : "cat", "owner" : "ella"}

pets=[piroska, luna, ozzy, bella]

for pet in pets:
    print("\n")
    for t, o in pet.items():
        print(t,":", o)