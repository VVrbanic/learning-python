k=int(input())
n=1
while n<k:
    n=n*2
d=1
br=n/2
b=2
if k%n==0:
   print (n, 0)
else:
    while k!=br:
        d=d+1
        b=b*2
        if k>br:
            br=br+n/b    
        elif k<br:
            br=br-n/b
    print (n, d)
            
              
    
       
      