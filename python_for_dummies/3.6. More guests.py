invitation= ["Lars", "Perl", "Garneth"]

for i in range(0,3):
    print(invitation[i], "please come!")
    
print(invitation[0], "can't come because he is on another planet.")

invitation.remove("Lars")
invitation.insert(0,"Steven")

for i in range(0,3):
    print(invitation[i], "please come!")
    
print("We found a bigger table, we have to invite three more guests!")

invitation.insert(0,"Connie")
invitation.insert(3,"Sadie")
invitation.append("Amethyst")

for i in range(0,6):
    print(invitation[i], "please come!")