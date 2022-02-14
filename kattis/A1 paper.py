a=input();
ostalo=input();

ostalo=ostalo.split();
brojac= 0;

#print( type(int(ostalo[0])))

for i in range (2, int(a)+1):
    
    if i == 2:
      brojac = int(ostalo[i-2]) / 2 + brojac;
      
    else:
      brojac = int(ostalo[i-2]) / (i*2) + brojac;
      
      
if brojac > 1:
    print(brojac);
else: 
    print("impossible");