import string

def first_word(text: str) -> str:
    fcount=-1
    lcount=0
    a= ""
    alfa=""
    alfa= list(string.ascii_lowercase + string.ascii_uppercase)
    
    for i in range(0, len(text)):
        if text[i] in alfa:
            if fcount == -1:
                fcount = i
            else:
                next
        if text[i] not in alfa:
            if fcount == -1:
                next
            else:
                lcount = i
                
    if lcount == 0: 
        lcount = len(text)
        
    a= text[fcount:lcount]  
    return a