#upisi namjmanju stranicu
a=input()
#upisi broj ostalih stranica
ostalo=input()
#pretvorimo u listu integera
ostalo=ostalo.split()
#najveća velicina parnih stranice i neparnih stranica
par=-3/4
nepar=-5/4

velicina=[]
potrebno=int(ostalo)
d=1
n=1
c=0
b=1
p=1
traka=0


#određivanje najveće stranice od A2 do An
for i in range(2, int(a)+1):
    if i%2==0:
       velicina.append(2**par/d)
       d=d*2
    else:
        velicina.append(2**nepar/n)
        n=n*2

#cilj je vidjeti mozemo li dobiti 2 A2 stranice, odnosno je li moguce ispisivanje svih 10 000 decimala broja pi
for i in range(0,len(potrebno)):
    potrebno[i]=int(potrebno[i])

    if potrebno[i]>=2**b:
        ostalo[i]=2**b-c
        brojac=i
        p=0
        break
    
    else:
        c=potrebno[i]*2
        potrebno[i+1]=potrebno[i+1]+c
        b=b*2
        
if p==1:
    print("impossible")
    
else:
    for i in range(0,brojac):
        traka=traka+ostalo[i]*velicina[i]
    print(traka)

