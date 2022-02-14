def find_message(text: str) -> str:

    message=""
    
    for i in range (0, len(text)):
        if text[i].isupper() == True:
            message= message + text[i]
        
    return message