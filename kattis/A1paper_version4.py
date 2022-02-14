#upisi namjmanju stranicu
a=input()
#upisi broj ostalih stranica
ostalo=input()
#pretvorimo u listu integera
ostalo=ostalo.split()
#najveća velicina parnih stranice i neparnih stranica
par=-3/4
nepar=-5/4
postalo=ostalo[:]

velicina=[]

kraj=[]
x=0
h1=0
h2=0
k=2

p=0
d=1
n=1
traka=0
b=int(a)-1

#određivanje najveće stranice od A2 do An
for i in range(2, int(a)+1):
    if i%2==0:
       velicina.append(2**par/d)
       d=d*2
    else:
        velicina.append(2**nepar/n)
        n=n*2

#obrni velicinu
velicina.reverse()
#cilj je vidjeti mozemo li dobiti 2 A2 stranice, odnosno je li moguce ispisivanje svih 10 000 decimala broja pi
for i in range(0,len(ostalo)):
    ostalo[i]=int(ostalo[i])

for i in range(1,len(ostalo)+1):
    
    if len(ostalo)-i!=0:
            
        if ostalo[len(ostalo)-i]>=2:
            #traka=traka+ostalo[len(ostalo)-i]//2*velicina[i-1]
            ostalo[len(ostalo)-1-i]=ostalo[len(ostalo)-1-i]+ostalo[len(ostalo)-i]//2
            
            
            if ostalo[len(ostalo)-i]%2 == 0:
                ostalo[len(ostalo)-i]=0
            else:
                ostalo[len(ostalo)-i]=1
    else:
        #traka=traka+ostalo[len(ostalo)-i]//2*velicina[i-1]
        if ostalo[0]<2:
                 p=1

for i in range(0,len(postalo)):
    h1=h2+int(postalo[i])
    if h1 >= k:
       x=k-h2 
       kraj.append(x)
       break
    else:   
        kraj.append(int(postalo[i]))
        h2=h1*2
        k=k*2
       
for i in range(1,len(kraj)+1):
    
    if len(kraj)-i!=0:
            
        if  kraj[len(kraj)-i]>=2:
            traka=traka+kraj[len(kraj)-i]//2*velicina[i-1]
            kraj[len(kraj)-1-i]=kraj[len(kraj)-1-i]+kraj[len(kraj)-i]//2
            
            
            if kraj[len(kraj)-i]%2 == 0:
                kraj[len(kraj)-i]=0
            else:
                kraj[len(kraj)-i]=1
    else:
        traka=traka+kraj[len(kraj)-i]//2*velicina[i-1]
                         
if p==1:
    print("impossible")
else:
     print(traka)
            
        
