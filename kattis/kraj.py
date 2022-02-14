n=int(input())
if n==1:
    print(1)
elif n==2:
    print(2)
elif n==3:
    print(3)
elif n==4:
    print(3)
else:
    m=n//2
    t=0
    i=1
    while t!=2:
          t=m/i
          i+=1
print(int(i+1))