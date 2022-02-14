import numpy as np
a=input()
b=input()
c=input()
d=input()
w=input()
k=2
a=a.split(" ")
b=b.split(" ")
c=c.split(" ")
d=d.split(" ")
a = list(map(int, a))
b = list(map(int, b))
c = list(map(int, c))
d = list(map(int, d))
m=[a,b,c,d]

x=np.matrix(m)

for i in range (0, 4):
    for j in range (0, 4):
        while x[i,j]==0:
            j=j+1
        while x[i,j+1]==0:
            j=j+k
            k=k+1
        if x[i,j]==x[i,j+1]:
            x[i,j]==x[i,j]*x[i,j]
