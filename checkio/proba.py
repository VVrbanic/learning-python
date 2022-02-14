import string

text=" don't lll "

fcount=-1
lcount=0
a= ""
alfa= list(string.ascii_lowercase + string.ascii_uppercase + "'")

for i in range(0, len(text)):
        if text[i] in alfa:
            if fcount == -1:
                fcount = i
                print(fcount,lcount, 1)
            else:
                print(fcount,lcount, 2)
                next
        if text[i] not in alfa:
            if fcount == -1:
                print(fcount,lcount,3)
                next
            else:
                lcount = i
                print(fcount,lcount, 4)
                break
if lcount == 0: 
        lcount = len(text)              
a= text[fcount:lcount]
print(a)