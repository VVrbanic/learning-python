invitation= ["Lars", "Perl", "Garneth"]
for i in range(0,3):
    print(invitation[i], "please come!")
print(invitation[0], "can't come because he is on another planet.")
invitation.remove("Lars")
invitation.insert(0,"Steven")
for i in range(0,3):
    print(invitation[i], "please come!")
