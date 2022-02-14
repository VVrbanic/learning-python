x=input()
n=0
m=2
a=""
b=""
c=""
d=""
e=""
for i in range (0,len(x)):
    if i==0:
        a=a+"..#.."
        b=b+".#.#."
        c=c+"#."+x[n]+".#"
        d=d+".#.#."
        e=e+"..#.."
        n+=1
    elif i%3==1:
        a=a+".#.."
        b=b+"#.#."
        c=c+"."+x[n]+"."
        d=d+"#.#."
        e=e+".#.."
        n+=1 
    elif i%3==2:
            a=a+".*.."
            b=b+"*.*."
            c=c+"*."+x[n]+".*"
            d=d+"*.*."
            e=e+".*.."
            n+=1
    else:
        a=a+".#.."
        b=b+"#.#."
        c=c+"."+x[n]+".#"
        d=d+"#.#."
        e=e+".#.."
        n+=1 
if i%3==1:
    c=c+"#"
print(a)
print(b)
print(c)
print(d)
print(e)