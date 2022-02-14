
#velicina matrice
velicina=input()
velicina=velicina.split()
velicina=[int(velicina[i]) for i in range (0, len(velicina))]
lis=[]
brojac=0
b=[0,0,0,0,0]
#popunjavanje matrice
for i in range(0, velicina[0]): 
    red=input()     
    lis.append(red)
#print(velicina[0])
#print(lis)
for i in range(0, velicina[0]-1):
    for j in range(0, velicina[1]-1):
        a=[]
        a=lis[i][j:j+2]+lis[i+1][j:j+2]
        #print(a)
        brojac=a.count("X")
        #print(brojac)
        
        if "#" in a:
            next
            
        elif brojac==0:
            b[0]=b[0]+1
            
        elif brojac==1:
            b[1]=b[1]+1
            
        elif brojac==2:
            b[2]=b[2]+1
            
        elif brojac==3:
            b[3]=b[3]+1
            
        elif brojac==4:
            b[4]=b[4]+1
            
        #print(brojac)  
        
        brojac=0
      
for i in range(0,len(b)):
    print(b[i])
        
            
        