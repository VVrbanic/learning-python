not_invited=[]
invitation= ["Lars", "Perl", "Garneth"]

print(len(invitation))

invitation.remove("Lars")
invitation.insert(0,"Steven")
invitation.insert(2,"Connie")
invitation.insert(3,"Sadie")
invitation.append("Amethyst")

print(len(invitation))

while len(invitation)>2:
     elp=invitation.pop()
     not_invited.append(elp)
     
for i in range (0, len(not_invited)):
    print(not_invited[i], "I'm sorry I can’t invite you to dinner.")
     

for i in range(0,len(invitation)):
    print(invitation[i], "please come!")

for i in range(0,len(invitation)-1):
    del invitation[i]
del invitation[0]

print(len(invitation))