from sys import exit

n=int(input())
d=input()
d=d.split()
for i in range(0,len(d)):
    d[i] = int(d[i])

d.sort()

for i in range(0,len(d)-2):
    if d[i]+d[i+1]>d[i+2]:
        print("possible")
        exit()

print("impossible")