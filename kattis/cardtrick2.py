def preskoci(lista, index, broj_praznih_mjesta):

    #broji preskocene koji su 0
    a=0
    #idemo na iduci broj
    i=0
    if (index==len(lista)) or (index+1==len(lista)):
        i=-index
    while a<broj_praznih_mjesta:
        #print("a=",a)
        #print("i=",i, "index=",index)
        if lista[index+i]==0:
            a=a+1
            
        if index+i+1==len(lista):
            i=-index
        else:
            i=i+1
            
    while True:
         
        if lista[index+i]==0:
            return(index+i) 
            break
        elif index+i+1==len(lista):
            i=-index
        else:
            i=i+1

t=int(input())
lis=[]
ispis=[]
lislis=[]

#listu broja karata
for i in range (0,t):
    n=int(input())
    lis.append(n)
    
#prolazi za svaki broj karata    
for i in range(0,len(lis)):  
    ispis=[]
    a=1
    #napravi listu s nulama
    for j in range(0,lis[i]):
        ispis.append(0)    
        index=0
    #print(ispis)
    
    #prolazi kroz listu i ubacuj
    for k in range (0,lis[i]): 
        l=preskoci(ispis,index,a)
        ispis[l]=a
        a=a+1
        index=l
    lislis.append(ispis)
    
    
           
for i in range(0,len(lislis)):
    print(*lislis[i])
    

       
       
    