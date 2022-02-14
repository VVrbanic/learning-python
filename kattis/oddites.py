n=int(input())

lis=[]
for i in range(0,n):
    l=int(input())
    lis.append(l)
    
for i in range (0,len(lis)):
    if lis[i]%2==0:
        print(lis[i],"is even")
    else:
        print(lis[i],"is odd")