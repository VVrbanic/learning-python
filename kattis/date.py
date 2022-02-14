import datetime

a=input()
a=a.split()

x = datetime.datetime(2009,int(a[1]),int(a[0]))

print(x.strftime("%A"))