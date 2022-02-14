def unix_match(filename: str, pattern: str) -> bool:
    a = True
    brojac=0
    
    for i in range (0,len(pattern)):
        if pattern[i] == "*" or pattern[i] == "?":
            brojac = brojac + 1
            
    
    if len(pattern) > len(filename):
        a = False
        return a
        
    elif brojac==len(pattern):
        return a
                
    elif len(pattern) == 4:
        
        for i in range(1,len(pattern)):
            if filename[-i]!=pattern[-i]:
                a = False
                break
            
    elif len(filename)==len(pattern):
        for i in range (0,len(filename)):
            if pattern[i]=="?":
                next
            elif pattern[i]!=filename[i]:
                a = False
                break
    else:
        for i in range(0,len(pattern)):
            if pattern[i]=="*":
                next
            else:
                if pattern[i] not in filename:
                    a= False
                    break
            
      #  for i in range(0,len(pattern)):
       #     if pattern[i]!= "*":
        #        if pattern[i]!= "?":
         #           a = False
          #          break     
    return a