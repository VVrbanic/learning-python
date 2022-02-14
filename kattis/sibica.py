import math

n=input()
n=n.split()
for i in range (0,len(n)):
    n[i]=int(n[i])

velicina=[]  
odgovor=[]
  
for i in range(0,n[0]):
    a=input()
    velicina.append(int(a))


for i in range(0,len(velicina)):
    if velicina[i]>math.sqrt(n[1]**2+n[2]**2):
        odgovor.append("NE")
    else:
        odgovor.append("DA")
        
for i in range(0,len(odgovor)):
    print(odgovor[i])
    
    