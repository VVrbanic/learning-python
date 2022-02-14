def bigger_price(limit: int, data: list) -> list:
     a=[]
     l=""
     l = sorted(data, key = lambda i: i['price'], reverse= True) 
     
     for i in range (0, limit):
         a.append(l[i])
    
     return a