from sys import exit

n=int(input())
d=input()
d=d.split()
for i in range(0,len(d)):
    d[i] = int(d[i])

for i in range(0,len(d)-2):
    for j in range(i+1,len(d)-1):
        for k in range(j+1,len(d)):
            if d[i]+d[j]>d[k] and d[k]+d[j]>d[i] and d[i]+d[k]>d[j]:
                print("possible")
                exit()

print("impossible")