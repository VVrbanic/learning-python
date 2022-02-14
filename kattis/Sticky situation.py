n=int(input())
d=input()
d=d.split()
l=0
m=1
a= False
for i in range(0,len(d)):
    d[i]=int(d[i])

for i in range(0,len(d)-2):
    l=l+1
    for j in range(l,len(d)-1):
        m=m+1
        for k in range(m,len(d)):
            if d[i]+d[j]>d[k] and d[k]+d[j]>d[i] and d[i]+d[k]>d[j]:
                a= True
if a == True:
    print("possible")
else:
    print("impossible")