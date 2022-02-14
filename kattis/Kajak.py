x=input()
s=input() #strgani
v= input() #visak

s=s.split()
s=[int(z) for z in s]
v=v.split()
v=[int(z) for z in v]

p=[y+1 for y in s] + [y-1 for y in s] #potencijalni
p=set(p)

h=p.intersection(v)


if len(h)>len(s):
    print(0)
else:
    print(len(s)-len(h))
    

