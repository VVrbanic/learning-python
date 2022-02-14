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
        
          
print(preskoci([0,0,0,0],0,1))
print(preskoci([0,1,0,0],1,2))
print(preskoci([2,1,0,0],0,3))
print(preskoci([2,1,0,3],3,4))

##
