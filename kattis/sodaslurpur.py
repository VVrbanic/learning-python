
lis=input()
lis=lis.split()

for i in range(0,len(lis)):
    lis[i]=int(lis[i])

broj_boca=0    
boce=lis[0]+lis[1]

while boce>= lis[2]:
    nova=boce
    boce=boce//lis[2]+boce%lis[2]
    broj_boca=broj_boca+nova//lis[2]
    
print(broj_boca)