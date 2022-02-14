n=input()
n=int(n)

a= 3
if n!=0:
    for i in range(1,n):
        a = a+ 2**i
        
    
if n == 0:
    print(4)
else:
    print(a**2)
    
