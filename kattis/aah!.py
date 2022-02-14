x=input()
n=0
a=""
b=""
c=""
d=""
e=""
for i in range (1,len(x)):
    if i==1:
        a=a+"..#.."
        b=b+".#.#."
        c=c+"#."+x[n]+".#"
        d=d+".#.#."
        e=e+"..#.."
        n+=1
    elif i%2==0:
        a=a+".#.."
        b=b+"#.#."
        c=c+"."+x[n]+"."
        d=d+"#.#."
        e=e+".#.."
        n+=1
    else:
        a=a+".*.."
        b=b+"*.*."
        c=c+"*."+x[n]+".*"
        d=d+"*.*."
        e=e+".*.."
        n+=1
if len(x)%2==1:
    c=c+"#"
print(a)
print(b)
print(c)
print(d)
print(e)