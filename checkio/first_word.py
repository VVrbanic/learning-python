def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    a=""
    count=0
    
    for i in range (0, len(text)):
        
        if text[i] == " ":
            break
        else:
            count =count + 1
            
    a = text[:count]  
    
    return a