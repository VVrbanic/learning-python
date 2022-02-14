a=input();
ostalo=input();

ostalo=ostalo.split();
brojac= 0;
traka=0
b=-5/4
c=-3/4
k=2**c;
#print( type(int(ostalo[0])))

for i in range (2, int(a)+1):
    
    if i == 2:
      traka = int(ostalo[i-2])*k+ traka;
      brojac=int(ostalo[i-2])/2 + brojac;             
                  
    elif i == 3:
      traka = int(ostalo[i-2])*k/2+ traka;
      brojac=int(ostalo[i-2])/(i*2) + brojac;
                   
    else:
      traka = int(ostalo[i-2])*k/ (i*2) + traka;
      brojac=int(ostalo[i-2])/(i*2) + brojac;
      
      
if brojac > 1:
    print(traka);
else: 
    print("impossible");
    

