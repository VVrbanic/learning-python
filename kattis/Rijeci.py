k=int(input())
a=1
b=1
c=0
if k==0:
    print(1,0)
elif k==1:
    print(0,1)
elif k==2:
    print(1,1)
else:
    for i in range (3,k+1):
        c=a
        a=b
        b=b+c
    print(a, b)
        