
b=0

stat=input()
b=b+1

stat=stat.split()
for i in range(0,len(stat)):
    stat[i]=int(stat[i])
    
mini=min(stat[1:])
maxi=max(stat[1:])
rangee=maxi-mini

for i in range(0,b):
    print("Case",str(i)+":",str(mini),str(maxi),str(rangee))
    