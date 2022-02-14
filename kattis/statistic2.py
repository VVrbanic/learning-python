
b=0
lis=[]
mini=[]
maxi=[]
rangee=[]
while True:
    stat=input()
    
    if stat=="":
        break
    else:
        
        b=b+1
        stat=stat.split()
        for i in range(0,len(stat)):
            stat[i]=int(stat[i])
        lis.append(stat)
    
for i in range(0,len(lis)):    
    mini.append(min(lis[i][1:]))
    maxi.append(max(lis[i][1:]))
    rangee.append(max(lis[i][1:])-min(lis[i][1:]))

for j in range(0,b):
    print("Case",str(j+1)+":",str(mini[j]),str(maxi[j]),str(rangee[j]))