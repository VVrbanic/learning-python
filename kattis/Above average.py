n=int(input())

a=[]


for i in range(0,n):
    br=0
    lis=input()
    lis=lis.split()
    for i in range(0,len(lis)):
        lis[i]=int(lis[i])
    brojac=0
    
    for i in range(0, len(lis)):
        brojac=brojac+lis[i]
        k=brojac/lis[0]
        
    for i in range(0,len(lis)):
        if lis[i]>k:
            br=br+1
    a.append(br/lis[0]*100)
    
for i in range(0, len(a)):
    print(a[i],"%")
    