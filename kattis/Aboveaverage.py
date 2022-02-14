n=int(input())

a=[]


for i in range(0,n):
    br=0
    lis=input()
    lis=lis.split()
    for i in range(0,len(lis)):
        lis[i]=int(lis[i])
    brojac=0
    
    for i in range(1, len(lis)):
        brojac=brojac+lis[i]
        k=round(brojac/lis[0],3)
        
        
    for i in range(1,len(lis)):
        if lis[i]>k:
            br=br+1
    if brojac==0:
        a.append(0)
    else:
        a.append(br/lis[0])
    
for i in range(0, len(a)):
    print('{:.3%}'.format(a[i]))
    