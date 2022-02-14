def checkio(words: str) -> bool:

    count = 1
    numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    for i in range (0, len(words)):
        if count >= 3:
            break
        
        if words[i] in numbers:
            count = 0
            
        if words[i] == " ":
            
            if words[i+1] in numbers:
                count = 0;
            else: 
                count = count + 1
                
    if count >= 3:
        return True 
    else:
        return False