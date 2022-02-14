n=int(input())

lis=[]
for i in range(0,n):
    prijedlog=input()
    prijedlog=prijedlog.split()
    prijedlog = [int(i) for i in prijedlog]
    lis.append(prijedlog)
    
for i in range (0, len(lis)):
    if lis[i][0]+lis[i][2]==lis[i][1]:
        print("does not matter")
    if lis[i][0]+lis[i][2]>lis[i][1]:
        print("do not advertise")
    if lis[i][0]+lis[i][2]<lis[i][1]:
        print("advertise")
    